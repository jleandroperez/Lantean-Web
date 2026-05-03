---
title: "Xcode: Number of lines"
date: 2012-03-16T21:52:49+00:00
slug: "xcode-number-of-lines"
categories:
  - "iOS"
---

I've been unable to figure out how to do this, actually, within Xcode. But this can also be accomplished by means of this short script:

```
find . "(" -name "*.m" -or -name "*.mm" -or -name "*.cpp" ")" -print | xargs wc -l
```
