---
title: "Shrinking EBS Volume"
date: 2014-03-06T10:06:17+00:00
slug: "shrinking-ebs-volume"
categories:
  - "Offtopic"
---

It took me a while to shrink my EBS volume, but <a href="http://wiki.jokeru.ro/shrink-amazon-ebs-root-volume">this post</a> helped quite a lot.
For further reference, this are the exact steps i've performed:

1. Created a snapshot of the EBS volume, for backup reasons.
2. Added a new volume, based on the snapshot.
3. Added another volume with the desired size.
4. Attached both, the Normal and Shrunken volumes.
5. Check the big volume, and resize it:
   ```
   e2fsck -f /dev/bigvolume
   resize2fs -M -p /dev/bigvolume
   ```- Note that 'resize2fs' will say something like:
     ```
     Resizing the filesystem on /dev/xvdg to 1035624 (4k) blocks.
     ```
   - Let's calculate how many 16MB blocks we'll need:
     ```
     x = 1035624 * 4 / 1024 / 16 = 253
     ```
   - Proceed copy'ing blocks to the small volume:
     ```
     dd bs=16M if=/dev/bigvolume of=/dev/smallvolume count=253
     ```
   - Resize + Check the small volume:
     ```
     resize2fs -p /dev/smallvolume
     e2fsck -f /dev/smallvolume
     ```
   - Stop the instance.
   - Detach the 3 volumes: Root, Big and Small.
   - Attach the *Small* volume at the same location as the previous root volume was. In my case, /dev/sda1.
   - **Ready!**
