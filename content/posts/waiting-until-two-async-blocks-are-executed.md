---
title: "Waiting until two async blocks are executed"
date: 2013-04-09T22:42:33+00:00
slug: "waiting-until-two-async-blocks-are-executed"
categories:
  - "iOS"
---

The following snippet of code.. which is super interesting, is based on <a href="http://stackoverflow.com/questions/11909629/waiting-until-two-async-blocks-are-executed-before-starting-another-block">this</a> post. This allows to dispatch a block, on Main Thread, once two async operations are completed.

```
dispatch_group_t group = dispatch_group_create();

dispatch_group_async(group, dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^ {
  NSLog(@"Block1");
  [NSThread sleepForTimeInterval:5.0];
  NSLog(@"Block1 End");
});

dispatch_group_async(group, dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^ {
  NSLog(@"Block2");
  [NSThread sleepForTimeInterval:8.0];
  NSLog(@"Block2 End");
});

dispatch_group_notify(group, dispatch_get_main_queue(), ^ {
  NSLog(@"Block3 :: %d", [NSThread isMainThread]);
});

dispatch_release(group);

```