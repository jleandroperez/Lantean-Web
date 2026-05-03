---
title: "Using 'performSelector: withObject: afterDelay:'!"
date: 2012-04-15T21:26:10+00:00
slug: "preventing-freeze-in-main-thread"
categories:
  - "iOS"
---

Sometimes, when developing an iOS application, we need to do something like 'displaying a spinner', and right after that, do a tedious task, such as query'ing a database, sorting a file, or hitting a backend.

As you may (or may not know)... all of the UIKit framework works on the Main Thread (with several exceptions, set aside). A common problem we might encounter is that... if you begin a long process after initializing an ActivityIndicatorView, the main thread will remain locked out, and thus... the spinner will never begin.

The easiest solution i could come up with looks something like this:

<p class="brush: actionscript3; gutter: true">

```
[_spinner startAnimating];
...
[self performSelector:@selector(doSomething:) withObject:someObject afterDelay:0.1f];
...

```

</p>

<p class="brush: actionscript3; gutter: true">What's this??. Simple!. We're scheduling the 'doSomething' selector, in the current runloop, to be executed after 0.1 seconds. That 'leaves room' for the mainThread to initialize the spinner (which, internally, will spawn another thread).</p>

<p class="brush: actionscript3; gutter: true">That way your app won't get a nasty freeze ... and the spinner will keep on rocking!</p>