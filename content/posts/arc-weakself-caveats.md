---
title: "ARC: weakSelf Caveats"
date: 2015-11-16T12:13:40+00:00
slug: "arc-weakself-caveats"
categories:
  - "iOS"
  - "OSX"
---

Here's an interesting ARC scenario. Consider the following snippet:

```
__weak __typeof(self) weakSelf = self;
int64_t delay = (int64_t)(0.1 * NSEC_PER_SEC);
dispatch_after(dispatch_time(DISPATCH_TIME_NOW, delay), dispatch_get_main_queue(), ^{
    [weakSelf doSomething];
});

```

Whenever the block gets executed... <em>weakSelf</em> might have a valid reference, or not. Right?.
Now, what happens with the following snippet?

```
__weak __typeof(self) weakSelf = self;
int64_t delay = (int64_t)(0.1 * NSEC_PER_SEC);
dispatch_after(dispatch_time(DISPATCH_TIME_NOW, delay), dispatch_get_main_queue(), ^{
    [weakSelf doSomething];
    [weakSelf doSomethingElse];
});

```

This is where it gets interesting!. There's a possibility that <em>doSomething</em> might get executed, while <em>doSomethingElse</em> might not.

If you need to prevent such scenario, a possible workaround is:

```
__weak __typeof(self) weakSelf = self;
int64_t delay = (int64_t)(0.1 * NSEC_PER_SEC);
dispatch_after(dispatch_time(DISPATCH_TIME_NOW, delay), dispatch_get_main_queue(), ^{
    __typeof(self) strongSelf = weakSelf;
    [strongSelf doSomething];
    [strongSelf doSomethingElse];
});

```

This snippet warrantees that: if (at the moment of the block's execution) weakSelf is not nil, it won't be for the rest of the snippet.

Another interesting note (for future reference) is: <em>self</em> is considered <em>strong</em>, and it may not get invalidated at the middle of a method execution. Okay?

P.s.: <a href="https://dhoerl.wordpress.com/2013/04/23/i-finally-figured-out-weakself-and-strongself/">Thanks to this Blog Post</a>