---
title: "UIView with Rounded Corners"
date: 2012-04-15T19:33:42+00:00
slug: "uiview-with-rounded-corners"
categories:
  - "iOS"
---

Sooner rather than later, you'll probably end up with a simple yet tricky requirement: an UIView with rounded corners.

iOS SDK has no 'radius' property. Ohhh wait!. Yeah, it actually has!. But the catch to it is that you need to import Quartz framework, first:

```
#import <QuartzCore/QuartzCore.h>

```

Also, you need to link the 'QuartzCore.framework'. Otherwise the import won't work.

So... how do you actually display an UIView with rounded corners?. Easy!

```
[_someView.layer setCornerRadius:6];

```

See?. Just a line of code. Kung fu isn't about a lot of spaghetti code. It's about knowing what to do!