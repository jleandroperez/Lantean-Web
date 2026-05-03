---
title: "Removing Cocoapods Integration"
date: 2016-05-11T10:47:54+00:00
slug: "removing-cocoapods-integration"
categories:
  - "OSX"
---

I've recently stumbled upon a huge Cocoapods annoyance. By recently i mean: 5 minutes ago. And by annoyance i mean: i've been struggling with this for an hour.

After switching over to CocoaPods 1.0, i began getting the following error:

```
ld: library not found for -lPods
```

Luckily, my friend Aaron shared this dark knowledge:

```
sudo gem install cocoapods-deintegrate
pod deintegrate
pod install
```

Thanks Aaron. Seriously. Thank you.