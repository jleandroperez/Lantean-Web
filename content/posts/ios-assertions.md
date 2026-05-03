---
title: "iOS Assertions"
date: 2012-03-08T23:03:28+00:00
slug: "ios-assertions"
categories:
  - "iOS"
tags:
  - "iOS"
---

So... you write a new piece of code. You run it. Test it. Ship it!. And in two weeks, you end up flooded by iTunes Connect Crash Reports.

What happened?. It turned out that an attribute parsed from a backend response ended up being a NSString instead of an NSNumber. And it was only after an untested-and-specific-workflow that your application actually used that field.

How do we prevent this?. ASSERTIONS!. A good friend of mine teached me that... great software blows everywhere before getting published. If your code works perfectly... you should be scared!.

What are assertions?. Simple. Checkpoints that will produce controlled crashes while your app is in Debug mode. How do you use them?.

Well, you'll need to declare few macros first. Say... we name this include 'LADebug.h':
```
#ifdef DEBUG
#   define ASSERT(x)            assert(x)
#   define ASSERT_CLASS(x, y)   assert([x isKindOfClass:[y class]])
#else
#   define ASSERT(x)           
#   define ASSERT_CLASS(x, y) 
#endif

```

So.. those macros will be available only if the DEBUG flag is present. How do you use them?.... this is just a simple example...

```
- (void)processResponse:(NSArray*)array callback:(id)callback
{ 
    ASSERT_CLASS(array, NSArray);
    ASSERT(callback);
    ...
}

```

This example will procude a controlled crash if the parameter 'array' is not an instance of NSArray. Or if the 'callback' parameter is not present.

This will make your debug target a little heavier. But if you use this app-wide, you'll be able to detect problems early in the development stages, and you'll have the chance of fixing them!.

Cool, ha?. (Thanks Tincho!).

&nbsp;