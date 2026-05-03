---
title: "CoreGraphics: Drawing Dashed Lines"
date: 2012-06-13T22:31:08+00:00
slug: "coregraphics-drawing-dashed-lines"
categories:
  - "iOS"
---

Suppose you wanna draw a dashed line all around a control. What should we do?. Well... simple. We need to invoke some CoreGraphics dark magic... it's pretty self explanatory. The catch to it is that it'll draw a dashed line. Play with it..!

```
static CGFloat const kDashedBorderWidth     = (2.0f);
static CGFloat const kDashedPhase           = (0.0f);
static CGFloat const kDashedLinesLength[]   = {4.0f, 2.0f};
static size_t const kDashedCount            = (2.0f);

- (void)drawRect:(CGRect)rect
{
    [super drawRect:rect];

    CGContextRef context = UIGraphicsGetCurrentContext();

    CGContextSetLineWidth(context, kDashedBorderWidth);
    CGContextSetStrokeColorWithColor(context, [UIColor grayColor].CGColor);

    CGContextSetLineDash(context, kDashedPhase, kDashedLinesLength, kDashedCount) ;

    CGContextAddRect(context, rect);
    CGContextStrokePath(context);
}

```