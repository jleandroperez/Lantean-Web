---
title: "Resetting the Push Notifications Permissions Alert on iOS "
date: 2012-08-27T19:11:45+00:00
slug: "resetting-the-push-notifications-permissions-alert-on-ios"
categories:
  - "iOS"
---

I'm just pasting this from <a href="http://developer.apple.com/library/ios/#technotes/tn2265/_index.html">Apple's Technical note</a>... it's soooo useful, yet, everytime i need to debug this, i spend at least 15 minutes with google...!.

<blockquote>The first time a push-enabled app registers for push notifications, iOS asks the user if they wish to receive notifications for that app. Once the user has responded to this alert it is not presented again unless the device is restored or the app has been uninstalled for at least a day.<br/>

If you want to simulate a first-time run of your app, you can leave the app uninstalled for a day. You can achieve the latter without actually waiting a day by setting the system clock forward a day or more, turning the device off completely, then turning the device back on.</blockquote>