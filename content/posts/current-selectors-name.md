---
title: "Current Selector's Name"
date: 2012-06-04T16:07:11+00:00
slug: "current-selectors-name"
categories:
  - "iOS"
---

So... suppose you wanna log the name of the 'current' method. You could hardcode the method name, right there... virtually everywhere... or you can do this:

```
NSLog(@"[ %@ ] did something", NSStringFromSelector(_cmd));

```

It's simple. Yet, its something i didn't know... three days ago!.