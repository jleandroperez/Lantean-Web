---
title: "Fix: macOS 27 Mission Control Shortcuts"
date: 2026-10-22T23:37:42Z
slug: "fix-macos-27-mission-control-shortcuts"
issue: 11
---

<img width="1632" height="994" alt="macOS 27" src="/images/posts/fix-macos-27-mission-control-shortcuts/macos-27.png" />

<br/>

There's a bug affecting macOS 27, which causes the `Switch to Desktop x` shortcut to stop working.
Hopefully fixed in the next release. In the meantime, this is my workaround:

```
sudo killall Dock
```

😢
