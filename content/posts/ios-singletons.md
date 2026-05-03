---
title: "iOS Singletons"
date: 2012-03-08T23:08:53+00:00
slug: "ios-singletons"
categories:
  - "iOS"
tags:
  - "iOS"
---

<a href="/wp-content/uploads/2012/03/ios3.jpeg"><img class="aligncenter size-full wp-image-1066" alt="ios3" src="/wp-content/uploads/2012/03/ios3.jpeg" width="400" height="311" /></a>

Suppose that... for whatever reason, you need to target iOS 3.x. Yes. You need to build an app that should run on any possible device. Or say that... you simply don't wanna use GCD.

What's the alternative to write a singleton?
```
+ (id)sharedInstance
{
   if(_instance = nil)
   {
      @synchronized(self)
      {
         if(_instance == nil)
         {
            _instance = [[[self class] alloc] init];
         }
      }
   }
   return _instance;
}
```
This is a nice alternative to the GCD option. The first time the instance is created, you'll suffer the lag caused by the @synchronized block. But after that. it's just an if. No context switch. No whatsoever! REALLY performant!