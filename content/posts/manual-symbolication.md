---
title: "Manual Symbolication"
date: 2021-01-22T20:23:51+00:00
slug: "manual-symbolication"
categories:
  - "OSX"
---

<p>I keep loosing this snippet, over an over, apparelty.</p>

<p>If you ever need to symbolicate (manually) a memory address, you'll just need the dSYM file:</p>

```
xcrun atos -l LOAD_ADDRESS SYMBOL_ADDRESS -o dSYMs/APP-NAME.dSYM/Contents/Resources/DWARF/APP-NAME
```

<p>🔥🔥🔥</p>
