---
title: "Fixing '\"A newer version of this app is already installed on this computer\" Alert"
date: 2014-02-04T10:23:39+00:00
slug: "fixing-a-newer-version-of-this-app-is-already-installed-on-this-computer-alert"
categories:
  - "OSX"
---

I've just got a nice alert, while trying to install a Mac App from the AppStore, saying the following:

```
"A newer version of this app is already installed on this computer."
```

<strong>Solutions?</strong>

1. Nuke the app's Xcode build folder.
   `Location: ~/Library/Developer/Xcode/DerivedData/`
2. Execute the following command:
   `/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user`

Now you should be good to go!