---
title: "Disabling Num Lock on startup (or why Windows makes me sick)"
date: 2017-05-04T10:25:35+00:00
slug: "disabling-num-lock-on-startup-or-why-windows-makes-me-sick"
categories:
  - "OSX"
---

- Launch Regedit
- <strong>HKEY_USERS\Default\Control Panel\Keyboard</strong>
- Set <strong>InitialKeyboardIndicators</strong> to Zero

Now, next time you boot... your beautiful small keyboard won't have Num Lock enabled by default, AND you should be able to enter your password without further issues.
