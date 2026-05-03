---
title: "Fixing \"iTunes was unable to load dataclass” Error"
date: 2012-12-04T13:34:15+00:00
slug: "fixing-itunes-was-unable-to-load-dataclass-error"
categories:
  - "iOS"
  - "OSX"
---

I've been dealing with the "iTunes was unable to load dataclass" for several hours.
I've uninstalled iTunes, Xcode, deleted the Mobile Device Support... reinstalled everything, booted the system, and nothing seemed to work.

After searching for quite some time, i've found <a href="http://ktula.com/2009/03/20/how-to-fix-itunes-was-unable-to-load-dataclass-error/" rel="nofollow">this</a> post. Long short story, if you delete this framework:

```
/System/Library/PrivateFrameworks/MobileDevice.framework
```

...and right afterwards you relaunch Xcode (which will, as a result, reinstall such framework)... you should be able to get rid of this... annoooooooooying problem.

&nbsp;