---
title: "Preventing crashes: JSON Parsers &amp; Null entries!"
date: 2012-03-09T16:35:06+00:00
slug: "preventing-crashes-json-parsers-null-entries"
categories:
  - "iOS"
tags:
  - "iOS"
---

How many times you got to parse a backend response, and tested if a given value is != nil?. Well, as it turns out, many parsers (such as JSONKit) will parse 'null' values into an instance of NSNull. That might cause a crash... unless you write eeeverywhere... '!= nil &amp;&amp; != [NSNull null]'.

So... a good idea would be to implement an NSDictionary extention, to do that. Right?.
The method would look like this:
```
- (id)objectForKeyNotNull:(id)key 
{
    id object = [self objectForKey:key];
    if (object == [NSNull null])
    {
        return nil;
    }
    else
    {
        return object;
    }
}
```