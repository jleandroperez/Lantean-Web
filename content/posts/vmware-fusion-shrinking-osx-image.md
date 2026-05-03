---
title: "VMWare Fusion: Shrinking OSX Image"
date: 2015-07-29T19:40:18+00:00
slug: "vmware-fusion-shrinking-osx-image"
categories:
  - "OSX"
---

If you're using VMWare Fusion for OSX, and you've got few images of older OSX releases, odds are you might have over-alloc'ed the disk space... you can never know how much it's really gonna be required!

Steps to fix this are:

1. Launch the OSX image that requires shrinking
2. Open **Disk Utility** App
3. Pick the Disk, click over the **Partition** tab, and reduce the partition's size, as much as possible
4. Shutdown the Virtual Machine

Once ready, you'll need to locate the VMDK file of your image: it can be found inside the <strong>Image.vmwarevm</strong> bundle.

We'll need to perform two final steps. Let's fire Terminal, and head over to this location: <code>/Applications/VMware\ Fusion.app/Contents/Library/</code>

Once there, you may run the following commands, which will defragment the image, and free the empty space:

```
./vmware-vdiskmanager -d [PATH TO VMDK]
./vmware-vdiskmanager -k [PATH TO VMDK]
```

Hope you find it useful!

<strong>Update:</strong>
Alternative method involves installing VMWare Tools in the host machine, and running the following command:
```
sudo /Library/Application\ Support/VMware\ Tools/vmware-tools-cli disk shrink /
```