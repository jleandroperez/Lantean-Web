---
title: "Generating a Mac Iconset"
date: 2013-07-24T21:06:24+00:00
slug: "generating-a-mac-iconset"
categories:
  - "iOS"
  - "OSX"
---

You'll need to create PNG assets with the following sizes and filenames:

```
icon_16x16.png
icon_16x16@2x.png
icon_32x32.png
icon_32x32@2x.png
icon_128x128.png
icon_128x128@2x.png
icon_256x256.png
icon_256x256@2x.png
icon_512x512.png
icon_512x512@2x.png

```
All of those assets should go into a folder named 'Icon.iconset'.
Afterwards, just fire Terminal and type the following command:

```
iconutil -c icns

```

If all went well, you should have a .icns file right there!.

Reference: <a href="https://developer.apple.com/library/mac/#documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Optimizing/Optimizing.html">Apple's Guidelines</a>.