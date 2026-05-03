---
title: "Debugging Autolayout"
date: 2014-12-11T12:06:37+00:00
slug: "debugging-autolayout"
categories:
  - "iOS"
---

If you need to debug the constraints that produced any view layout, just hit LLVM, and type:

```
po [[UIWindow keyWindow] _autolayoutTrace]

```

This will help you get the Autolayout Trace. Pick up the troublesome view, find its memory address, and then try:

```
po [0x12341234 constraintsAffectingLayoutForAxis:1]

```

Note that you should replace <strong>0x12341234</strong> with the memory address of the view you'd like to debug. AxisX = 0, while AxisY = 1.

Props to <a href="https://blog.safaribooksonline.com/2012/10/31/tip-ambiguous-auto-layouts-in-ios-6/">this extremely useful post</a>.
