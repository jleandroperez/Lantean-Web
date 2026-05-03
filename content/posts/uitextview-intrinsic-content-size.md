---
title: "UITextView + Intrinsic Content Size"
date: 2016-08-29T11:19:14+00:00
slug: "uitextview-intrinsic-content-size"
categories:
  - "iOS"
---

Note to future self: the trick to get intrinsicContentSize to properly work, in UITextView instances, is to simply disable scrolling in the UITextView instance.

That way... the intrinsic size will be properly calculated.