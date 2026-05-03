---
title: "macOS: Format as FAT32"
date: 2017-10-15T19:18:32+00:00
slug: "macos-format-as-fat32"
categories:
  - "OSX"
---

<strong>Find the device path:</strong>

```
diskutil list
```

<strong>Format as FAT32:</strong>

```
sudo diskutil eraseDisk FAT32 NAME MBRFormat /dev/disk2
```

<em>Thanks Apple, for having FAT32 as an option in the Disk Utility app. It's so much nicer than having to remember a CLI command.&lt;/sarcasm&gt;</em>
