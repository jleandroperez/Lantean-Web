---
title: "Grand Central Dispatch Singletons"
date: 2012-03-08T22:46:41+00:00
slug: "grand-central-dispatch-singletons"
categories:
  - "iOS"
tags:
  - "iOS"
---

So... what's the recommended way (thread safety + performance) to implement a singleton?

Well.. it looks pretty much like this!
```
+ (instancetype)sharedInstance
{
  static dispatch_once_t pred;
  static Foo* bar = nil;

  dispatch_once(&pred, ^{ bar = [[Foo alloc] init]; });
  return bar;
}
```