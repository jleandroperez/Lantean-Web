---
title: "Twitter iOS SDK"
date: 2012-05-19T11:49:08+00:00
slug: "twitter-ios-sdk"
categories:
  - "iOS"
---

I recently had to integrate one of my apps with Twitter. Let me say you something. I HATE TWITTER guys. Why?. Because everything is soooo complicated. Although there is a direct integration between Twitter and iOS 5, they have made it really hard for developers.

Why?. If you need to post tweets, backend side, you need to ask for '<a href="https://dev.twitter.com/docs/ios/using-reverse-auth" rel="nofollow">Reverse Auth</a>' permissions.. and it's not something that can be done automatically. They have to personally approve this.

So... if you're like me, stressed dealing with those guys, check this out: <a href="https://github.com/bengottlieb/Twitter-OAuth-iPhone" rel="nofollow">https://github.com/bengottlieb/Twitter-OAuth-iPhone</a>.

What is that?. A nice iOS library, which implements OAuth authentication against twitter servers. I'm tuning it, just a little bit. There is a 'PIN' mechanism implemented right there, which i'm not particular fond of. But besides that, it'll help you open a WebView as a modalViewController, and authenticate the user into twitter.

Not the best i've imagined.. but the problem is solved. My idea is to implement a hybrid. If the user has no credentials stored in iOS 5, then i'll fall back to this framework. Makes sense.. right?.