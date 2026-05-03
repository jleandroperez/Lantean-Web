---
title: "Grand Central Dispatch: Perform Block After Delay"
date: 2012-03-20T02:06:21+00:00
slug: "grand-central-dispatch-perform-block-after-delay"
categories:
  - "iOS"
---

We have seen <a title="GCD Singletons" href="/grand-central-dispatch-singletons/">in a previous post </a>the proper way to write a singleton, with the help of our good friend Grand Central Dispatch.

In this opportunity, i´d like to share a goodie i´ve learnt few days ago. I suppose many of you had problems with the following scenario. You have to perform a task, which is time consuming, and you need to place, onscreen, an Activity Indicator.

Although the Activity Indicator performs the animation on its own thread, you need to "spare some time" in the main thread for it to begin working. I mean... you can execute [indicator startAnimating] right away. But... if you don´t release the main thread, even for a short moment, surprise!. The spinner won´t work.

So... the common solution is to split that method into two parts, and execute 'performSelector: withObject: afterDelay:'. That´s where GCD comes in.
We can do the exact same thing... but with blocks!!. That´s SO MUCH COOL...!

```
dispatch_time_t popTime = dispatch_time(DISPATCH_TIME_NOW,
                                        0.1f * NSEC_PER_SEC);

dispatch_after(popTime, dispatch_get_main_queue(), ^(void)
{
     // ...  Your code
});

```

Note: The delay, in this example, is of about 0.1 seconds.