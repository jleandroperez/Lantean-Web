---
title: "Loading NIBs stored inside a bundle"
date: 2013-01-16T20:27:07+00:00
slug: "loading-nibs-stored-inside-a-bundle"
categories:
  - "iOS"
---

When does it make sense to store your NIBs inside a bundle?. As we've discussed <a title="Making an iOS Assets Bundle" href="/making-an-ios-assets-bundle/">before</a>... this becomes handy when you're distributing a framework which has some custom NIB files.

But wait.... how do you tell a UIViewController to load its nib file from a bundle?. Short answer... we'll rely on UIViewController's 'initWithNibName: bundle:' constructor.

Before doing that... we need to take care about a small detail, which is, how to load a NSBundle object (to pass on as the 'bundle' parameter).

We'll show you the required code below, encapsulated into a nice helper class:

```
@interface LABundles
+ (NSBundle*)someResourcesBundle;
@end

@implementation LABundles
NSString* const kSomeResourcesBundleName = @"SomeResources.bundle";

+ (NSBundle*) someResourcesBundle
{
	static NSBundle* someResourcesBundle = nil;
	if ( someResourcesBundle == nil )
	{
           @synchronized(self)
           {
               if ( someResourcesBundle == nil )
               {
                   NSString* bundlePath = [[[NSBundle mainBundle] resourcePath] stringByAppendingPathComponent:kSomeResourcesBundleName];
                   someResourcesBundle = [[NSBundle bundleWithPath:bundlePath] retain];
               }
           }
	}

    return someResourcesBundle;
}
@end

```

Finally, in order to alloc an UIViewController, and load its nib from the SomeResources bundle, we need to do the following:

```
    SomeViewController* someVC = [[SomeViewController alloc] initWithNibName:NSStringFromClass([SomeViewController class])
                                                                      bundle:[LABundles someResourcesBundle]];

```

That's it!. SomeViewController should be loading its nib file from the someResources bundle.