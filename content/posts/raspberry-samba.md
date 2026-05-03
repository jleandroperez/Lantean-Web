---
title: "Raspberry + Samba"
date: 2017-04-17T09:00:32+00:00
slug: "raspberry-samba"
categories:
  - "Raspberry"
---

<p><strong>Installing Samba:</strong><br></p>

```
apt-get install samba samba-common-bin
```

<p>Once there, edit <strong>/etc/samba/smb.conf</strong> as follows:</p>

```
workgroup = [your_workgroup_name]

[SHARE-NAME]
comment=Samba Share
path=/PATH/TO/YOUR/SHARE
browseable=Yes
writeable=Yes
only guest=no
create mask=0777
directory mask=0777
public=no
```

<p>At last, setup the Samba password:</p>

```
smbpasswd -a YOUR_USERNAME
```