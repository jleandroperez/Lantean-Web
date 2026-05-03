---
title: "Using Xcode 7.x with an iOS 10 Device"
date: 2016-06-16T16:17:45+00:00
slug: "using-xcode-7-x-with-an-ios-10-device"
categories:
  - "iOS"
---

Trick of the month....

1. Upgrade your device to iOS 10
2. Install Xcode 8 (Beta)
3. Hook up your device and launch Xcode. It'll download debugging symbols.
4. Run this command in bash:

```
sudo ln -s /Applications/Xcode-beta.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/10.0\ (14A5261u) /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/10.0\ (14A5261u)
```

And now you can use your iOS 10 device with Xcode 7. Phew