---
title: "Detecting taps in any UIView subclass"
date: 2012-05-09T22:46:55+00:00
slug: "detecting-taps-in-any-uiview-subclass"
categories:
  - "iOS"
---

This one is a quick and easy trick. How do you detect taps in any UIView?.
Simple. You need to use the UITapGestureRecognizer class... this way:

```
// Alloc the gesture recognizer
UITapGestureRecognizer* tapGestureRecognizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(viewTapped)];
[tapGestureRecognizer setNumberOfTapsRequired:1];
[anyRandomView addGestureRecognizer:tapGestureRecognizer];
[anyRandomView setUserInteractionEnabled:YES];

[tapGestureRecognizer release];
tapGestureRecognizer = nil;

```