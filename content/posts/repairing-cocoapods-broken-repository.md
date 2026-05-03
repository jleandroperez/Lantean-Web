---
title: "Repairing CocoaPods Broken Repository"
date: 2014-02-04T16:02:32+00:00
slug: "repairing-cocoapods-broken-repository"
categories:
  - "iOS"
  - "OSX"
---

It seems that CocoaPods fellows had an <a href="http://blog.cocoapods.org/Repairing-Our-Broken-Specs-Repository/">issue with libgit</a>, and their public repository broke down.

In order to fix it, you'll need to....

```
pod repo remove master
pod setup
```