---
title: "Burning Kali in macOS High Sierra!"
date: 2017-11-21T22:05:27+00:00
slug: "burning-kali-in-macos-high-sierra"
categories:
  - "OSX"
---

To my future self: this is how you can 'burn' an ISO file into a flashdrive, so that it's bootable!

```
hdiutil convert -format UDRW -o destination.img kali-linux-2017.2-amd64.iso 
diskutil list
diskutil partitionDisk /dev/disk2 1 "Free Space" "unused" "100%"
sudo dd if=destination.img.dmg of=/dev/disk2 bs=1m
diskutil eject /dev/disk2
```
