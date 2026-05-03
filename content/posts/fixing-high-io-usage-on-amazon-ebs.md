---
title: "Fixing High I/O usage on Amazon EBS"
date: 2013-04-01T23:48:42+00:00
slug: "fixing-high-io-usage-on-amazon-ebs"
categories:
  - "Offtopic"
---

This humble wordpress blog is running on an AWS micro instance. We've got somewhere around 1k visitors each month, which is pretty awesome. But... to my surprise, the whole system is using over 14 million I/O operations.

I suspected there was something wrong with this... so i proceeded to do a small research.
By means of the application 'iotop', i managed to spot the I/O hog: apache!.

Specifically, i ran iotop with the following parameters:

```
sudo iotop -a -P
```
I ran a quick search on google, and found <a href="http://blog.vec.com/2012/05/29/io-problem-solved/">this</a> post.  (Thank you George, for sharing your solution!).

Long short story, Apache's APC plugin was using a memory mapped file, and it was writing... almost all the time.
The solution?. Edit your /etc/php.d/apc.ini file, and make sure that the mmap_file_mask parameter is se to use Shared Memory, as follows:

```
apc.mmap_file_mask=/apc.shm.XXXXXX
```
That should fix it!