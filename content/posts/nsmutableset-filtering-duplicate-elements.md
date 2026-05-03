---
title: "NSMutableSet: Filtering Duplicate Elements"
date: 2012-03-20T02:16:28+00:00
slug: "nsmutableset-filtering-duplicate-elements"
categories:
  - "iOS"
---

Suppose that your app has X amount cached objects. And suppose that there is a slight chance that.. since the backend doesn´t actually know what it is exactly that you have cached (and what you don´t have cached), it might send duplicates.

So... what do we do?. Shall we write a for routine checking dupes?. No way. There is a far more performant way to achieve this, and it requires less lines of code.

Steps...

- Implement your own 'isEquals' and 'hash' methods, in your model object. For instance...

```
- (BOOL)isEqual:(id)object
{
    SomeClass* secondObject = (SomeClass*)object;
    return ([secondObject isKindOfClass:[self class]] &amp;&amp; 
            [[secondObject id] isEqual:[self id]]);
}

- (NSUInteger)hash 
{
    return [_id hash];
}

```

- Simply instantiate a NSMutableSet and add the cached objects plus the objects retrieved from the backend. If the set already has an object for any given ID, and you attempt to insert a new one... but with the same id, it´ll just not work.

So... no more filtering things by hand. NextSTEP's code will do the trick, from now on!