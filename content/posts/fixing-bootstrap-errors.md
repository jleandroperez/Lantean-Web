---
title: "Fixing Bootstrap Errors"
date: 2012-05-09T23:40:38+00:00
slug: "fixing-bootstrap-errors"
categories:
  - "iOS"
---

I've been having this error... A LOT...:

"Couldn't register com.yourcompany.yourapp with the bootstrap server. Error: unknown error code. This generally means that another instance of this process was already running or is hung in the debugger."

The bad side of this is that.. ps aux will not show anything useful. Thankfully, Mike Ash has solved this... i'm pasting below his script:

```
launchctl list|grep UIKitApplication|awk '{print $3}'|xargs launchctl remove

```

Source: <a href="http://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html" target="_blank">Mike Ash Blog</a>