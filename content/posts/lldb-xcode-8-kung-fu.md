---
title: "LLDB + Xcode 8 Kung Fu"
date: 2017-03-14T10:34:54+00:00
slug: "lldb-xcode-8-kung-fu"
categories:
  - "iOS"
  - "OSX"
---

<strong>Printing Arrays</strong>
```
parray  number pointer
poarray number pointer
```

<strong>Reading Method Parameters</strong>
```
register read $arg1 $arg2
memory read $arg1
```

<strong>Printing Objects in Swift</strong>
```
expr -O --language objc -- 0x1003183e0
```

<strong>Disassembling the current frame</strong>
```
disassemble --frame
```

<strong>Module Image</strong>
```
image list ModuleName
```