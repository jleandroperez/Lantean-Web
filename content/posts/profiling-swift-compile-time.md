---
title: "Profiling: Swift Compile Time"
date: 2016-10-06T19:04:00+00:00
slug: "profiling-swift-compile-time"
categories:
  - "iOS"
  - "OSX"
---

```
xcodebuild -scheme TARGET clean build OTHER_SWIFT_FLAGS="-Xfrontend -debug-time-function-bodies" | grep .[0-9]ms | grep -v ^0.[0-9]ms | sort -nr > culprits.txt
```

<a href="http://irace.me/swift-profiling">Reference Here</a>