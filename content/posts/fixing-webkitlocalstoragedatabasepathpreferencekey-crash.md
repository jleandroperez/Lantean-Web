---
title: "Fixing WebKitLocalStorageDatabasePathPreferenceKey crash"
date: 2013-01-07T15:46:53+00:00
slug: "fixing-webkitlocalstoragedatabasepathpreferencekey-crash"
categories:
  - "iOS"
---

I've been getting a lot of crashes with the following signature:

```
Exception Type:  SIGABRT
Exception Codes: #0 at 0x351be32c
Crashed Thread:  0

Application Specific Information:
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[__NSCFDictionary setObject:forKey:]: attempt to insert nil value (key: WebKitLocalStorageDatabasePathPreferenceKey)'

```

What is this?. It's pretty well explained <a href="http://www.mail-archive.com/callback-dev@incubator.apache.org/msg03468.html" rel="nofollow">here</a>.
My workaround?. Quite simple. Call this method as soon as your app launches:

```
-(void)fixWebkitCrash
{
    NSUserDefaults* defaults = [NSUserDefaults standardUserDefaults];
    NSString* webkitPath = [defaults objectForKey:@"WebKitLocalStorageDatabasePathPreferenceKey"];
    NSString* bundlePath = [[[NSBundle mainBundle] bundlePath] stringByDeletingLastPathComponent];
    
    if([webkitPath containsString:bundlePath] == NO)
    {
        [defaults removeObjectForKey:@"WebKitLocalStorageDatabasePathPreferenceKey"];
        [defaults synchronize];
    }
}

```

Hopefully, this will save you a couple hours!.