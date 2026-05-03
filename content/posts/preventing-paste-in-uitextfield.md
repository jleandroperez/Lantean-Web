---
title: "Preventing Paste in UITextField"
date: 2012-04-15T19:43:39+00:00
slug: "preventing-paste-in-uitextfield"
categories:
  - "iOS"
---

Suppose that your app has a custom keyboard (or component) which populates an UITextField. So... suppose that you need to enable the User Interaction with that control. However, you don't wanna anyone pasting values right there... because you wanna force the user to rely on your custom keyboard.

UITextField lacks a 'disablePaste' property. In order to do this, we're gonna need to subclass UITextField. Our subclass should look like this...

```
@interface MyTextField : UITextField
{
BOOL _disablePaste;
    BOOL _disableCut;
    BOOL _disableSelect;
}

@property (nonatomic, assign) BOOL disablePaste;
@property (nonatomic, assign) BOOL disableCut;
@property (nonatomic, assign) BOOL disableSelect;

@end

```

Nice, ha!?. Let's see the actual implementation, now!:

```
@implementation MyTextField

@synthesize disablePaste    = _disablePaste;
@synthesize disableCut      = _disableCut;
@synthesize disableSelect   = _disableSelect;

- (BOOL)canPerformAction:(SEL)action withSender:(id)sender
{
    if ( _disablePaste && action == @selector(paste:) )
    {
        return NO;
    }
    else if ( _disableCut && action == @selector(cut:) )
    {
        return NO;
    }
    else if ( _disableSelect && (action == @selector(select:) || action == @selector(selectAll:)) )
    {
        return NO;
    }
    else
    {
        return [super canPerformAction:action withSender:sender];
    }
}

@end

```