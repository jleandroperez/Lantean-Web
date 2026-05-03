---
title: "iOS and JavaScript Bridge"
date: 2012-04-21T13:22:45+00:00
slug: "ios-and-javascript-bridge"
categories:
  - "iOS"
---

What if you need to write a completely dynamic app, and you need to have the ability of updating the App's contents remotely, without the need of pushing a new build to the AppStore?.

What if you need to write javascript code, which needs to interact with your iOS code?.
Yeah. I had that problem. Long short story, i'm testing a nice framework called <a title="Clutch" href="https://clutch.io/" rel="nofollow">clutch</a>.

Clutch has a nice JavaScript and iOS SDK, which smoothens the interaction between those two technologies. When you ship the app, you bundle a version of the webApp in it.

If the app has no internet access, it will rely on that bundled web. And as soon as you launch it, it gets sync'ed with the backend. (You can actually push 'new version' to the Clutch backend).

So far... i'm loving it. Go, try it... and let me know what you think!.

If you just need to build a dumb iOS and JS bridge, i suggest you also check out <a title="WebViewJavascriptBridge" href="https://github.com/marcuswestin/WebViewJavascriptBridge" rel="nofollow">this github project</a>, and <a title="GAJavaScript" href="https://github.com/newyankeecodeshop/GAJavaScript" rel="nofollow">this one</a>.

<a href="/wp-content/uploads/2012/04/Screen-Shot-2012-04-21-at-1.18.43-PM.png"><img class="aligncenter size-full wp-image-314" title="Screen Shot 2012-04-21 at 1.18.43 PM" src="/wp-content/uploads/2012/04/Screen-Shot-2012-04-21-at-1.18.43-PM.png" alt="" width="399" height="288" /></a>