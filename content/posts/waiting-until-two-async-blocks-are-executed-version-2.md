---
title: "Waiting until two async blocks are executed (Version #2)"
date: 2013-06-26T15:58:10+00:00
slug: "waiting-until-two-async-blocks-are-executed-version-2"
categories:
  - "iOS"
---

This is a nice variant to <a href="/waiting-until-two-async-blocks-are-executed/">this</a> other post. It gives you... way too much flexibility!

```
dispatch_group_t group = dispatch_group_create();

dispatch_group_enter(group);
dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^ {
  NSLog(@"Block1");
  [NSThread sleepForTimeInterval:5.0];
  dispatch_group_leave(group);
  NSLog(@"Block1 End");
});

dispatch_group_enter(group);
dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^ {
  NSLog(@"Block2");
  [NSThread sleepForTimeInterval:8.0];
  dispatch_group_leave(group);
  NSLog(@"Block2 End");
});

dispatch_group_notify(group, dispatch_get_main_queue(), ^ {
  NSLog(@"Group Notify Block3 :: %d", [NSThread isMainThread]);
});

```