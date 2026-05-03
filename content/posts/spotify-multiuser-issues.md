---
title: "Spotify: Multiuser Issues"
date: 2017-04-12T19:30:53+00:00
slug: "spotify-multiuser-issues"
categories:
  - "OSX"
---

<p>I've recently hit an annoying issue: if you share your mac with, say, your brother... you'll figure out that Spotify will only work in one of the two accounts.</p>

<p>It doesn't really matter if you actually have two seats or not. It won't run at all.</p>

<p>Solution?. As ever... bash and...</p>

```
cd /Applications
sudo chmod -R 755 Spotify.app/
```

<p></p>
