---
title: "Raspbian + Flash Drive + fstab"
date: 2017-04-19T18:53:27+00:00
slug: "raspbian-flash-drive-fstab"
categories:
  - "Raspberry"
---

<p>First off, you need to figure out the path of your flash drive:</p>

```
fdisk -l
```

<p>Then... edit <b>/etc/fstab</b> as follows:</p>

```
/dev/sda1 /mnt/flash vfat rw,user,umask=0002,uid=1001,gid=121 0 0
```

<p>Note that umask is... the "inverted" regular file mask. This represents 665 (because we're evil). As per <b>uid + gid</b>, you can figure it out by means of this command:</p>

```
id username
```

<p><strong>Update:</strong></p>

<p>The best filesystem to use, if you need to maintain compatibility between the Flash Drive you'll use with your Raspberry, and macOS, is probably ExFat. Now, problem is: Linux doesn't really support ExFat by default.</p>

<p>So, we'll need to install it, as follows:</p>

```
sudo apt-get install exfat-fuse
```

<p>In such case, your <b>/etc/fstab</b> file should look like this:</p>

```
/dev/sda1 /mnt/flash exfat. rw,user,umask=0002,uid=1001,gid=121 0 0
```