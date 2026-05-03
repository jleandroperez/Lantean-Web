---
title: "Fixing 'Show in Finder'"
date: 2012-12-31T18:06:50+00:00
slug: "fixing-show-in-finder"
categories:
  - "OSX"
---

I've been dealing with an annoying glitch in OSX 10.8.2. For some reason, 'show in finder' breaks down... on its own.

The workaround is...

```
sudo killall -KILL appleeventsd
```

Let's just hope a real fix shows up, sooner rather than later.