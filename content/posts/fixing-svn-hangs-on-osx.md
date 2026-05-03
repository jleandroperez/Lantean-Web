---
title: "Fixing SVN hangs on OSX"
date: 2013-03-19T21:02:23+00:00
slug: "fixing-svn-hangs-on-osx"
categories:
  - "OSX"
---

I'm writing this, right here, so i know where to pick it up next time i get the same issue. Thanks to Jonathan, who wrote <a href="http://focusritedevelopmentteam.wordpress.com/2012/08/08/fixing-svn-hangs-on-os-x-an-exercise-in-troubleshooting/">this</a> awesome post, and saved me quite a lot of time.

Long short story, it seems there is a buggy library on OSX, that produces broken SSL connections to hang for quite some time. Workaround?

```
sudo port install neon
```

That should upgrade the faulty library, and fix this annoying issue.</pre>