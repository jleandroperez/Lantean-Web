---
title: "Using NSLocalizedString with a dictionary stored inside a bundle"
date: 2013-01-16T20:29:52+00:00
slug: "using-nslocalizedstring-with-a-dictionary-stored-inside-a-bundle"
categories:
  - "iOS"
---

We've seen before <a title="Making an iOS Assets Bundle" href="/making-an-ios-assets-bundle/">how to create an iOS Assets bundle</a>. Today, we'll try to localize a string, using a dictionary stored in a bundle. In order to do so... we'll rely on the following helper method:

```
@interface LABundles
+ (NSBundle*)someResourcesLocalizationBundle
@end

@implementation LABundles
+ (NSBundle*)someResourcesLocalizationBundle
{
	static NSBundle* someResourcesLocalizationBundle = nil;

	if ( someResourcesLocalizationBundle == nil )
	{
	    // This double check increases efficiency. Don't you get bored of asking the same thing twice?.
        @synchronized(self)
        {
            if ( someResourcesLocalizationBundle == nil )
            {
	            // Figure out the current language.
         		NSUserDefaults* defs = [NSUserDefaults standardUserDefaults];
                NSArray* languages = [defs objectForKey:@"AppleLanguages"];

                NSString* currentLanguage = [languages objectAtIndex:0];

	            // Map the current language's folder within the bundle
                NSBundle* bundle = [NSBundle someResourcesBundle];
                NSString* path = [bundle pathForResource:currentLanguage ofType:@"lproj"];

	            // Okay, let's go with the default bundle
                if ( path == nil )
                {
                    someResourcesLocalizationBundle = bundle;
                }
	            // Bingo!
                else
                {
                    someResourcesLocalizationBundle = [NSBundle bundleWithPath:path];
                }

                [someResourcesLocalizationBundle retain];
            }
        }
	}

    return someResourcesLocalizationBundle;
}
@end

```

&nbsp;
What's that all about?. Well... it turns out that order to resolve localized strings, first of all we need to figure out what's the device's language.

After that, we need to load a NSBundle object mapped to the folder inside the bundle, which contains the localized strings file. And then we can begin talking about resolving a localized string.

The code pasted above has been tested, of course!. But how do you use it ????

Supposing that you need to localize the string 'Testing1', and that you intend to use a dictionary named 'InfoPlist.strings', you need to do the following:

```
[[NSBundle someResourcesLocalizationBundle] localizedStringForKey:@"Testing1" value:nil table:@"InfoPlist"]

```

Of course, you can customize that. If your dictionary file is named 'Localized.strings', you don't even need to specify the 'table' parameter.

I hope you find this useful!