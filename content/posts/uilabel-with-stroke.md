---
title: "UILabel with Stroke!"
date: 2012-05-04T20:40:29+00:00
slug: "uilabel-with-stroke"
categories:
  - "iOS"
---

Time to invoke some... dark magic. For some reason, UILabel doesn't support stroke. So, if you're... by chance... working on a videogame, or a simple iOS app, and you actually need to render an UILabel with a stroke, in a given color, you have come to the right place.

Let's begin with the header file:

```
@interface LAStrokeLabel : UILabel
{
    NSUInteger _strokeWidth;
    UIColor* _strokeColor;
}

@property (nonatomic, assign) NSUInteger strokeWidth;
@property (nonatomic, retain) UIColor* strokeColor;

@end

```

So far so good... right?. Nothing weird. Just a simple UILabel subclass, with two extra properties.

Now, let's get to business. We're gonna need to link 'CoreGraphics' framework. Otherwise this won't work. The .m file should look like this:

```
static NSUInteger kDefaultStrokeWidth = 1;

@implementation LAStrokeLabel

@synthesize strokeWidth = _strokeWidth;
@synthesize strokeColor = _strokeColor;

-(void)dealloc
{
    [_strokeColor release];
    _strokeColor = nil;

    [super dealloc];
}

-(id)init
{
   if((self = [super init]))
   {
      _strokeWidth = kDefaultStrokeWidth;
      _strokeColor = [[UIColor blackColor] retain];
   }

   return self;
}

-(id)initWithFrame:(CGRect)frame
{
   if((self = [super initWithFrame:frame]))
   {
      _strokeWidth = kDefaultStrokeWidth;
      _strokeColor = [[UIColor blackColor] retain];
   }

   return self;
}

-(void)awakeFromNib
{
   _strokeWidth = kDefaultStrokeWidth;
   _strokeColor = [[UIColor blackColor] retain];

   [super awakeFromNib];
}

-(void)drawTextInRect:(CGRect)rect
{
   CGSize shadowOffset = self.shadowOffset;
   UIColor* textColor = self.textColor;
   BOOL highlighted = self.highlighted;

   CGContextRef c = UIGraphicsGetCurrentContext();

   // Draw the stroke
   if( _strokeWidth > 0 )
   {
      CGContextSetLineWidth(c, _strokeWidth);
      CGContextSetTextDrawingMode(c, kCGTextStroke);

      self.textColor = _strokeColor;
      self.shadowColor = _strokeColor;
      self.shadowOffset = CGSizeMake(0, 0);
      self.highlighted = NO;

      [super drawTextInRect:rect];
   }

   // Revert to the original UILabel Params
   self.highlighted = highlighted;
   self.textColor = textColor;

   // If we need to draw with stroke, we're gonna have to rely on the shadow
   if(_strokeWidth > 0)
   {
      self.shadowOffset = CGSizeMake(0, 1); // Yes. It's inverted.
   }

   // Now we can draw the actual text
   CGContextSetTextDrawingMode(c, kCGTextFill);
   [super drawTextInRect:rect];

   // Revert to the original Shadow Offset
   self.shadowOffset = shadowOffset;
}

@end

```

If you figured out... you just got an extra point. Yes. For some reason, CoreGraphics's stroke wasn't drawing anything 'below the bottom line'. That's the reason why i've implemented a workaround: the 'bottom' of the stroke is actually a shadow.

A bit hacky, but i promess, it will work great.
