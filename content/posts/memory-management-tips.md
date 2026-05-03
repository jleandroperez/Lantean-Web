---
title: "Memory Management Tips!"
date: 2012-03-08T23:26:27+00:00
slug: "memory-management-tips"
categories:
  - "iOS"
tags:
  - "iOS"
---

It's REALLY recommended that you set to nil any pointer that has a reference to a released object. But it's tedious, right?. [pointer release]; pointer = nil;.

Why don't we use a macro instead??
```
#define LAWipe(x)         [x release]; x = nil;

```

Simple. Nice. This should help you lower down the BAD_ACCESS crashes!.

&nbsp;