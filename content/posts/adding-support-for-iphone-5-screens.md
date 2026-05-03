---
title: "Adding support for iPhone 5 screens"
date: 2013-01-16T18:18:20+00:00
slug: "adding-support-for-iphone-5-screens"
categories:
  - "iOS"
---

Not long ago, i had to extend an app to support iPhone 5. Yes... iOS has autolayout functionality, that should aid the development of UIView's.

But how about assets?. How do you load assets specially crafted for 568px height screens?. Furthermore.. how do you patch classes that inherit from UITableViewCell, to return dynamic height, according to the device?.

Simple!. By means of a super short UIScreen extension. The header should look like this...:

```
@interface UIScreen (Lantean)
+(BOOL)isH568;
@end

```

Write the following snippet in the .m file:

```
@implementation UIScreen (Lantean)
+(BOOL)isH568
{
    static BOOL isH568 = NO;
    static dispatch_once_t _once;

    dispatch_once(&_once, ^
                  {
                      isH568 = ([UIScreen mainScreen].bounds.size.height == 568);
                  });
    return isH568;
}
@end

```

Fair enough. By checking [UIScreen isH568], you should be able to proceed as required... if the current device has the new 4 inches screen!.