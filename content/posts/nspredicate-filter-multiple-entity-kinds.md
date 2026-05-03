---
title: "NSPredicate: Filter multiple entity kinds"
date: 2020-08-26T15:53:44+00:00
slug: "nspredicate-filter-multiple-entity-kinds"
categories:
  - "OSX"
---

```
let predicate = NSCompoundPredicate(orPredicateWithSubpredicates: [

    NSCompoundPredicate(andPredicateWithSubpredicates: [
        NSPredicate(format: "entity = %@", Note.entity()),
        NSPredicate(format: "content CONTAINS[cd] %@", "1")
    ]),
    
    NSCompoundPredicate(andPredicateWithSubpredicates: [
        NSPredicate(format: "entity = %@", Tag.entity()),
        NSPredicate(format: "name CONTAINS[c] %@", "tag")
    ])
])
```

<p>Now, this yields another problem: there is no API to limit the number of entities to fetch "per group".</p>

<p>If you do need this feature, you're probably better of with multiple NSFetchRequest(s).</p>
