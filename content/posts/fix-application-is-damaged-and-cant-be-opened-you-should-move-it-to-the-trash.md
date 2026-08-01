---
title: "Fix: [Application] is damaged and can't be opened. You should move it to the Trash"
date: 2026-08-01T21:30:04Z
slug: "fix-application-is-damaged-and-cant-be-opened-you-should-move-it-to-the-trash"
issue: 7
---

<img width="372" height="392" alt="Image" src="/images/posts/fix-application-is-damaged-and-cant-be-opened-you-should-move-it-to-the-trash/630181053-5c5e541c-d07c-4b53-92d5-70b3ca3ad2e1.png" />

<br/>

This error is triggered by macOS's Gatekeeper, and it means the OS cannot verify its signature.
You can bypass this check by stripping the quarantine flag in the application itself:

```
xattr -cr Application.app
```
