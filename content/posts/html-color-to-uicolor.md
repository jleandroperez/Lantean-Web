---
title: "HTML Color to UIColor"
date: 2012-04-06T14:30:03+00:00
slug: "html-color-to-uicolor"
categories:
  - "iOS"
---

This is a nice tool i'd like to share with you. While skinning your app, you might need to convert HTML color codes into those that are actually accepted by UIKit framework (which, by the way, is HEX!).

So... you need to fire Photoshop, or find a website that does that for you. Well, i just found a nice app called HexColors. It's in the Mac AppStore, and it's free (go get it!).

It allows you to convert html colors, straightforward, into an ObjectiveC NSColor... which, by the way, looks like this:

```
[NSColor colorWithCalibratedRed:0xFF/255.0 green:0xFF/255.0 blue:0xFF/255.0 alpha:0xFF/255.0]/* FFFFFFFF */

```

So... if you're also working on iOS, you just need to weak that sentence to look like this:

```
[UIColor colorWithRed:0xFF/255.0 green:0xFF/255.0 blue:0xFF/255.0 alpha:0xFF/255.0]/* FFFFFFFF */

```

I know. That's an extra step you have to take. There is also another version that actually has UIColor support, but it's a paid app... and... i don't mind replacing two words... it's not THAT much, right?.

I hope you find it useful!