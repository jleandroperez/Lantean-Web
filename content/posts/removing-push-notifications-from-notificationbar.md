---
title: "Removing Push Notifications from NotificationBar"
date: 2012-04-11T12:24:03+00:00
slug: "removing-push-notifications-from-notificationbar"
categories:
  - "iOS"
---

I have come up with a weird problem.... which goes as follows:

1. The app receives a Push Notification.
2. You tap over the PN (in the iOS notification center).
3. The app gets launched... and you handle the notification
4. **Problem**: the notification remains in the 'notification bar'.

How do you clean it ?. Well... this isn't in Apple's docs. But i've figured out that if you execute the following line of code, the notification 'gets acknowledged':

```
[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];

```

Nice, ha?.

&nbsp;