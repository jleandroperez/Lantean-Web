---
title: "Manually Symbolicating iOS Crashlogs"
date: 2013-01-16T19:39:23+00:00
slug: "manually-symbolicating-ios-crashlogs"
categories:
  - "iOS"
---

I've been facing this problem for as long as i've been developing iOS apps. What's the deal with crashlogs????.....

Apple allows you to download crashlogs through iTunesConnect. What are crashlogs you may say. Well, crashlogs are simply text files that allows us to debug crashes. You get to see the Stack Dump at the moment of the crash, as well as the architecture, and loaded libraries.

What is symbolication??... well, the crashes you download in iTunesConnect aren't useful, unless you've got the dSYM file matching that crashlog. If you do, you'll be able to symbolicate it. That means that... instead of seeing memory addresses in the stack dump, you'll get to see method and class names.

You can symbolicate crashlogs using Xcode Organizer. Why would you wanna do it manually?. Because sometimes the crashlogs don't get symbolicated, and.. if you do it manually, you get access to the verbose mode... and you miiight stand a chance of fixing the glitch that prevents symbolication.

<strong>So, let's begin.... we assume the following:</strong>

- You've got a horrible .crashlog file.
- You've got the dSYM file that matches the binary that crashed.
- You've got Xcode 4.3 or superior.

<strong>Steps... steps!!</strong>

1. Check and Fix Xcode Path. Fire up a terminal, and type:
   ```
   /usr/bin/xcode-select -print-path
   ```
   If it says anything but '/Applications/Xcode.app/Contents/Developer/', then it's wrong. In order to fix it, you should type:
   ```
   sudo /usr/bin/xcode-select -switch /Applications/Xcode.app/Contents/Developer/
   ```
2. Locate the 'symbolicatecrash' script. You can do so by typing:
   ```
   find /Applications/Xcode.app -name symbolicatecrash -type f
   ```
3. In your home directory (cd ~), you should edit the .profile file, and type the following:
   ```
   SYMBOLICATECRASH="Type the path returned by find"export SYMBOLICATECRASH
   export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
   PATH=":${SYMBOLICATECRASH}:${PATH}"
   export PATH
   ```

That's it. Now, you should simply go to the folder where the .crash file is located, and you should type...

```
symbolicatecrash NAME.crash
```
If everything goes fine, the stack dump should he human-readable!