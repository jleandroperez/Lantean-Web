---
title: "Pushing a new CocoaPods Version with Trunk"
date: 2014-06-30T12:15:04+00:00
slug: "pushing-a-new-cocoapods-version-with-trunk"
categories:
  - "iOS"
---

CocoaPods is a useful dependency management tool for OSX and iOS. They've recently introduced some changes, to ease the process of publishing new versions of your Framework.

Just in case you're lost, just like me, these are the commands required to push a new release:

```
pod trunk register EMAIL@HERE.COM 'Your Name' --description='MBP 15'
pod trunk me
pod trunk push FrameworkName.podspec.json

```

Note that after hitting <strong>trunk register</strong>, you'll get an email to confirm your identity.
