---
title: "OSX: Fixing SSH hangs!"
date: 2013-05-23T00:41:46+00:00
slug: "osx-fixing-ssh-hangs"
categories:
  - "OSX"
---

This glitch is pretty annoying. You're following a log, while connected to a server (through ssh), and after a while, your ssh connection hangs.
The solution?.

Fire up Terminal, and type the following: nano ~/.ssh/config

Once there, fill up the following:

```
ServerAliveInterval 300
ServerAliveCountMax 120

```

That should keep your connection alive for the next 10 hours, without further issues.
