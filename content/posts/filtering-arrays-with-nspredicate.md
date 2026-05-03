---
title: "Filtering arrays with NSPredicate!"
date: 2012-03-09T12:24:42+00:00
slug: "filtering-arrays-with-nspredicate"
categories:
  - "iOS"
tags:
  - "iOS"
---

Suppose you wanna filter a collection of objects. Normally, you'd write a while loop, implement a comparison, and add the matching objects to a collection.

Well, there is an easier way!!. For the sake of this example, say you wanna filter the objects that have the BOOL 'isEnabled set to YES. So, you could do the following:

```
NSPredicate* predicate = [NSPredicate predicateWithFormat:@"isEnabled == YES"]; NSArray *filteredArray = [myArray filteredArrayUsingPredicate:predicate];

```

Yet another powerful example of NSPredicate would be... remember 'SELECT* WHERE FIELD IN(1, 2)' ?. Guess what!

```
NSPredicate* filterPredicate = [NSPredicate predicateWithFormat:@"field IN %@", desiredFieldValues];
NSArray* filteredObjects = [allObjects filteredArrayUsingPredicate:filterPredicate];

```