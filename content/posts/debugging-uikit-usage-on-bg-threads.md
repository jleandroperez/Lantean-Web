---
title: "Debugging UIKit Usage on BG Threads"
date: 2014-07-10T17:08:38+00:00
slug: "debugging-uikit-usage-on-bg-threads"
categories:
  - "iOS"
---

Based on <a href="http://www.cocoanetics.com/2013/02/uiview-background-queue-debugging/">this awesome cocoanetics post</a>, and updated to work <a href="https://github.com/rentzsch/jrswizzle">with JRSwizzle</a>, you might find the UIView+Debug category very handy, specially when debugging die hard bugs.

```
#import "JRSwizzle.h"

@interface UIView (Debug)

@end

@implementation UIView (Debug)

- (void)methodCalledNotFromMainQueue:(NSString *)methodName
{
    NSLog(@"-[%@ %@] being called on background queue. Break on -[UIView methodCalledNotFromMainQueue:] to find out where", NSStringFromClass([self class]), methodName);
}

- (void)_setNeedsLayout_MainQueueCheck
{
    if (![NSThread isMainThread])
    {
        [self methodCalledNotFromMainQueue:NSStringFromSelector(_cmd)];
    }
    
    // not really an endless loop, this calls the original
    [self _setNeedsLayout_MainQueueCheck];
}

- (void)_setNeedsDisplay_MainQueueCheck
{
    if (![NSThread isMainThread])
    {
        [self methodCalledNotFromMainQueue:NSStringFromSelector(_cmd)];
    }
    
    // not really an endless loop, this calls the original
    [self _setNeedsDisplay_MainQueueCheck];
}

- (void)_setNeedsDisplayInRect_MainQueueCheck:(CGRect)rect
{
    if (![NSThread isMainThread])
    {
        [self methodCalledNotFromMainQueue:NSStringFromSelector(_cmd)];
    }
    
    // not really an endless loop, this calls the original
    [self _setNeedsDisplayInRect_MainQueueCheck:rect];
}

+ (void)toggleViewMainQueueChecking
{
    NSError *error = nil;
    [UIView jr_swizzleMethod:@selector(setNeedsLayout)
                    withMethod:@selector(_setNeedsLayout_MainQueueCheck)
                         error:&error];
    
    [UIView jr_swizzleMethod:@selector(setNeedsDisplay)
                    withMethod:@selector(_setNeedsDisplay_MainQueueCheck)
                         error:&error];
    
    [UIView jr_swizzleMethod:@selector(setNeedsDisplayInRect:)
                    withMethod:@selector(_setNeedsDisplayInRect_MainQueueCheck:)
                         error:&error];
}

@end

```
