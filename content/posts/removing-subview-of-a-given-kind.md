---
title: "Removing subviews that match any given criteria!"
date: 2012-05-09T22:50:27+00:00
slug: "removing-subview-of-a-given-kind"
categories:
  - "iOS"
---

So... suppose that you have a container view. And for some reason, you need to remove the subviews that match any given criteria.

The straightforward solution would be to write a foreach loop, by hand, and remove the target subviews with a method call. Guess what!. There is a kung fu solution to this..!!. Check this out:

```
NSPredicate* predicate      = [NSPredicate predicateWithFormat:@"self isKindOfClass: %@", [SomeView class]];
NSArray* viewsToRemove = [[self subviews] filteredArrayUsingPredicate:predicate];
[viewsToRemove makeObjectsPerformSelector:@selector(removeFromSuperview)];

```

Less code is better. Always.