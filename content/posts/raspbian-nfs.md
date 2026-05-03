---
title: "Raspbian + NFS"
date: 2017-04-20T10:07:45+00:00
slug: "raspbian-nfs"
categories:
  - "Raspberry"
---

<p><strong>Install:</strong></p>

```
apt-get install nfs-kernel-server
nano /etc/exports
```

<p>Once there, let's add:</p>

```
/mnt/flash *(rw,sync)
```

<p>Dont' forget to run <strong>exportfs</strong>!</p>

<p><strong>Add New Services:</strong></p>

<p>Here's the deal: rpcbind must run before nfs-server. But due to a bug... that's not the case. What happens if the sequence is not that?... simple! NFS is inaccessible.</p>

<p>In order to fix this, let's do the following:</p>

```
cat >/etc/systemd/system/nfs-common.service <<\EOF 
[Unit]
Description=NFS Common daemons 
Wants=remote-fs-pre.target 
DefaultDependencies=no 

[Service] 
Type=oneshot 
RemainAfterExit=yes 
ExecStart=/etc/init.d/nfs-common start 
ExecStop=/etc/init.d/nfs-common stop 

[Install] 
WantedBy=sysinit.target 
EOF
```

```
cat >/etc/systemd/system/rpcbind.service <<\EOF 
[Unit] 
Description=RPC bind portmap service 
After=systemd-tmpfiles-setup.service 
Wants=remote-fs-pre.target 
Before=remote-fs-pre.target 
DefaultDependencies=no 

[Service]
ExecStart=/sbin/rpcbind -f -w 
KillMode=process 
Restart=on-failure 

[Install]
WantedBy=sysinit.target 
Alias=portmap 
EOF
```

<p><a href="https://unix.stackexchange.com/questions/263331/debian-jessie-start-rpcbind-and-nfs-common-at-boot-with-systemd">Source Here!</a></p>

<p></p>
