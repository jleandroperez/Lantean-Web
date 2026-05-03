---
title: "OSX Lion: Refresh Launchpad Contents"
date: 2012-06-13T23:57:43+00:00
slug: "osx-lion-refresh-launchpad-contents"
categories:
  - "OSX"
---

I recently came across a problem. The contents of the launchpad, somehow, got corrupt. I was seeing files that shouldn't be there. So... how did i fix it?

Open this folder:

```
~/Library/Application Support/Dock
```

(CMD + Shift + G... and paste that!). Once you're right there... you'll need to delete delete the ".db" file. Last step... relaunch the dock!

```
killall Dock
```

That's it!