---
title: "Targetting iPhone 3gs and superior"
date: 2012-04-21T12:36:16+00:00
slug: "targetting-iphone-3gs-and-superior"
categories:
  - "iOS"
---

I recently had a problem with one of the apps i'm working on. (Yeah, yet another problem!). The first release supported ARMv6 (which is handy when targetting older devices, as well, such as 1st and 2nd iPod generations, and the old iPhone 3g).

As it turns out, you cannot change the requirements of an app after pushing an update. I mean, you cannot simply remove 'ARMv6' support. Apple's policy is that ... you should continue supporting all of the target platforms you've enabled in the very first release.

So far so good. But what happens if you need to link a library which is built for ARMv7, without ARMv6 support?. Two options... one... weak linking. The second, would be to simply deprecate ARMv6. But apple... doesn't want this.

Hey... wait... there is a catch to it!!. If you update the 'target iOS platform' to iOS 4.3 (or higher)... you can safely drop ARMv6 architecture.

Why?. iOS 4.3 cannot be installed on older devices, such as the iPhone 3g. It doesn't support ARMv6 architecture.

So... long short story... the only way to safely drop armv6 support is by setting an upper target platform (4.3+).

Who's using anything older than that???. Go on... deprecate those old devices!. They have already fulfilled their cycle...

&nbsp;

<a href="/wp-content/uploads/2012/04/iphone2g.jpg"><img class="aligncenter size-full wp-image-288" title="iphone2g" src="/wp-content/uploads/2012/04/iphone2g.jpg" alt="" width="600" height="350" /></a>