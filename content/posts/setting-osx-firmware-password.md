---
title: "Setting OSX Firmware Password"
date: 2013-01-18T15:14:13+00:00
slug: "setting-osx-firmware-password"
categories:
  - "Security"
---

OSX is a strong and secure system. Until you realize there is a feature called 'single user login'... which virtually grants you ROOT access, provided that you have physical access to the target machine.

1. Boot the system.
2. Press CMD + S.
3. You should get a bash shell, with ROOT permissions.

That sucks, pretty much. There is just no single password screen. If you have the machine, you can access its files. How do we prevent this????.

In Lion, and Mountain Lion...:

1. Open Terminal and type:
   ```
   defaults write com.apple.DiskUtility DUDebugMenuEnabled 1
   ```
2. Open DiskUtility and choose "Show every partition", from the 'Debug' menu you have just unlocked.
3. Mount the 'Recovery HD' hidden partition.
4. In Terminal, type:
   ```
   open /Volumes/Recovery\ HD/com.apple.recovery.boot/BaseSystem.dmg
   ```
5. In the BaseSystem DMG you've just mounted, locate: Applications/Utilities.
6. Launch 'Firmware Password Utility', and simply follow the instructions.

That should, at the very least, enhance a little bit your security.