#!/usr/bin/env python3
"""Convert a GitHub issue (from $GITHUB_EVENT_PATH) into a Hugo post.

Downloads any user-attachment / user-images images referenced in the body
into static/images/posts/<slug>/ and rewrites the body to point at the
local copies. Idempotent: re-running on an edited issue overwrites the
post and any renamed file (matched by `issue:` frontmatter field)."""

import hashlib
import json
import os
import pathlib
import re
import sys
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = REPO_ROOT / "content" / "posts"
IMAGE_ROOT = REPO_ROOT / "static" / "images" / "posts"
PUBLISH_LABEL = "post"

# user-attachments (current) + user-images.githubusercontent.com (legacy, public + private)
IMG_HOST_RE = re.compile(
    r"https://(?:github\.com/user-attachments/assets|"
    r"(?:private-)?user-images\.githubusercontent\.com)/[^\s\"')>\]]+"
)
CD_FILENAME_RE = re.compile(r"filename\*?=(?:UTF-8'')?\"?([^\";]+)\"?", re.IGNORECASE)
SAFE_NAME_RE = re.compile(r"[^a-zA-Z0-9._-]")
MD_IMG_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<url>https?://[^)\s]+)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HTML_ATTR_RE = re.compile(r"""(\w+)\s*=\s*(?:"([^"]*)"|'([^']*)'|(\S+))""")
DEFAULT_ALT_TEXTS = {"image", "img", "picture", "screenshot", ""}
CTYPE_EXT = {"image/png": "png", "image/jpeg": "jpg", "image/gif": "gif",
             "image/webp": "webp", "image/svg+xml": "svg", "image/avif": "avif"}


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[\s_-]+", "-", s)
    return s.strip("-") or "post"


def _html_attrs(tag: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in HTML_ATTR_RE.finditer(tag):
        out[m.group(1).lower()] = m.group(2) or m.group(3) or m.group(4) or ""
    return out


def alt_hints_from_body(body: str) -> dict[str, str]:
    """Map url -> first non-default alt text from markdown ![alt](url) and
    HTML <img alt="..." src="..."> in the issue body."""
    hints: dict[str, str] = {}
    for m in MD_IMG_RE.finditer(body):
        url = m.group("url").strip()
        alt = m.group("alt").strip()
        if alt.lower() not in DEFAULT_ALT_TEXTS and url not in hints:
            hints[url] = alt
    for m in HTML_IMG_RE.finditer(body):
        attrs = _html_attrs(m.group(0))
        url = (attrs.get("src") or "").strip()
        alt = (attrs.get("alt") or "").strip()
        if url and alt.lower() not in DEFAULT_ALT_TEXTS and url not in hints:
            hints[url] = alt
    return hints


def download_image(url: str, dest_dir: pathlib.Path,
                   name_hint: str | None = None) -> str:
    """Download url into dest_dir, return the local filename. If name_hint is
    given, use a slugified version of it as the filename base; otherwise fall
    back to Content-Disposition / URL basename / Content-Type."""
    req = urllib.request.Request(url, headers={"User-Agent": "lantean-publish-bot"})
    with urllib.request.urlopen(req) as resp:  # noqa: S310 (trusted GH host)
        cd = resp.headers.get("Content-Disposition", "")
        m = CD_FILENAME_RE.search(cd)
        served = m.group(1) if m else pathlib.Path(resp.url).name.split("?")[0]
        ctype = resp.headers.get("Content-Type", "").split(";")[0].strip()
        data = resp.read()

    served_ext = pathlib.Path(served or "").suffix.lstrip(".").lower()
    ext = served_ext or CTYPE_EXT.get(ctype, "bin")

    if name_hint:
        base = slugify(name_hint)
    elif served and "." in served:
        base = pathlib.Path(SAFE_NAME_RE.sub("_", served)).stem
    else:
        base = ""
    if not base:
        base = hashlib.sha1(url.encode()).hexdigest()[:10]

    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{base}.{ext}"
    n = 2
    while dest.exists() and dest.read_bytes() != data:
        dest = dest_dir / f"{base}-{n}.{ext}"
        n += 1
    if not dest.exists():
        dest.write_bytes(data)
    return dest.name


def remove_old_post_for_issue(issue_number: int, keep_path: pathlib.Path) -> None:
    """If a previous run wrote this issue to a different filename, drop it."""
    if not CONTENT_DIR.exists():
        return
    needle = f"\nissue: {issue_number}\n"
    for md in CONTENT_DIR.glob("*.md"):
        if md == keep_path:
            continue
        try:
            head = md.read_text(encoding="utf-8")[:1024]
        except OSError:
            continue
        if needle in head:
            md.unlink()


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("GITHUB_EVENT_PATH not set", file=sys.stderr)
        return 2
    event = json.loads(pathlib.Path(event_path).read_text())
    issue = event.get("issue")
    if not issue:
        print("No issue payload — nothing to do.")
        return 0

    labels = [lab["name"] for lab in issue.get("labels", [])]
    if PUBLISH_LABEL not in labels:
        print(f"Issue #{issue['number']} missing '{PUBLISH_LABEL}' label — skipping.")
        return 0

    title = issue["title"].strip()
    slug = slugify(title)
    body = issue.get("body") or ""
    created = issue["created_at"]  # ISO 8601
    number = issue["number"]
    categories = [lab for lab in labels if lab != PUBLISH_LABEL]

    image_dir = IMAGE_ROOT / slug
    alt_hints = alt_hints_from_body(body)
    url_to_local: dict[str, str] = {}
    for url in dict.fromkeys(IMG_HOST_RE.findall(body)):
        try:
            filename = download_image(url, image_dir, name_hint=alt_hints.get(url))
        except Exception as e:  # noqa: BLE001 — log and keep the original URL
            print(f"Failed to download {url}: {e}", file=sys.stderr)
            continue
        url_to_local[url] = f"/images/posts/{slug}/{filename}"

    new_body = body
    for url, local in url_to_local.items():
        new_body = new_body.replace(url, local)

    front = ["---", f'title: "{title.replace(chr(34), chr(39))}"',
             f"date: {created}", f'slug: "{slug}"', f"issue: {number}"]
    if categories:
        front.append("categories:")
        for c in categories:
            front.append(f'  - "{c}"')
    front.append("---\n")

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = CONTENT_DIR / f"{slug}.md"
    out_path.write_text("\n".join(front) + "\n" + new_body.strip() + "\n",
                        encoding="utf-8")
    remove_old_post_for_issue(number, out_path)

    print(f"Wrote {out_path.relative_to(REPO_ROOT)} "
          f"({len(url_to_local)} image(s) localized)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
