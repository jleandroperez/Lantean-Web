---
title: "Checking the UUID of a DSYM file"
date: 2013-02-05T12:43:35+00:00
slug: "checking-the-uuid-of-a-dsym-file"
categories:
  - "iOS"
---

So... you've got a crashlog, and you don't know if a given DSYM actually matches with the original executable?. Well, there is a super easy way to verify this. Simply type the following, in your console:

```
dwarfdump -u Project.app.dSYM/Contents/Resources/DWARF/Project
```

Ideally, mdfind should help you locate the matching DWARF. But sometimes... symbolication requires extra debugging.