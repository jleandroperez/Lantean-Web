---
title: "Xcode 8: Disabling Networking Logs"
date: 2016-09-17T18:27:25+00:00
slug: "xcode-8-disabling-networking-logs"
categories:
  - "iOS"
  - "OSX"
---

Xcode 8 seems to be printing, for whatever reason, lots and lots of extra debug information.
We can shut it down by means of an environment variable:

```
OS_ACTIVITY_MODE = disable
```

<a href="http://stackoverflow.com/questions/37800790/hide-strange-unwanted-xcode-8-logs/39461256#39461256">Reference Here</a>
