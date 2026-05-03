---
title: "CoreAnimation: Bounce animation... like the Camera button"
date: 2012-06-14T20:11:52+00:00
slug: "coreanimation-bounce-animation-like-camera-button"
categories:
  - "iOS"
---

Have you seen the animation in which the lockscreen bounces... if you tap over the camera button?. Guess what!. That can be done, quite easily, with Core Animation.

We'll implement this as an extension to UIView. So.. add a file named 'UIView+CoreAnimation.h/m', and paste the following code:

REF: Thanks to the <a href="http://www.cocoanetics.com/2012/06/lets-bounce">Cocoanetics</a> author for sharing this. I've tweaked his code just a little bit.

```
#import <QuartzCore/QuartzCore.h>

+ (CAKeyframeAnimation*)dockBounceAnimationWithViewHeight:(CGFloat)viewHeight
{
	NSUInteger const kNumFactors    = 22;
	CGFloat const kFactorsPerSec    = 30.0f;
	CGFloat const kFactorsMaxValue  = 128.0f;
	CGFloat factors[kNumFactors]    = {0,  60, 83, 100, 114, 124, 128, 128, 124, 114, 100, 83, 60, 32, 0, 0, 18, 28, 32, 28, 18, 0};

	NSMutableArray* transforms = [NSMutableArray array];

	for(NSUInteger i = 0; i < kNumFactors; i++)
	{
		CGFloat positionOffset  = factors[i] / kFactorsMaxValue * viewHeight;
		CATransform3D transform = CATransform3DMakeTranslation(0.0f, -positionOffset, 0.0f);

		[transforms addObject:[NSValue valueWithCATransform3D:transform]];
	}

	CAKeyframeAnimation* animation = [CAKeyframeAnimation animationWithKeyPath:@"transform"];
	animation.repeatCount           = 1;
	animation.duration              = kNumFactors * 1.0f/kFactorsPerSec;
	animation.fillMode              = kCAFillModeForwards;
	animation.values                = transforms;
	animation.removedOnCompletion   = YES; // final stage is equal to starting stage
	animation.autoreverses          = NO;

	return animation;
}

- (void)jump
{
	CGFloat midHeight = self.frame.size.height * 0.5f;
	CAKeyframeAnimation* animation = [[self class] dockBounceAnimationWithViewHeight:midHeight];
	[self.layer addAnimation:animation forKey:@"bouncing"];
}

```