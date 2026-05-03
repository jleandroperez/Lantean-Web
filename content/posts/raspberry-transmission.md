---
title: "Raspberry + Transmission"
date: 2017-04-14T15:49:41+00:00
slug: "raspberry-transmission"
categories:
  - "Raspberry"
---

<p>Let's begin with the basics. We'll need to upgrade the system to the latest, and update the apt-get database. Once ready, we'll proceed with the transmission's daemon + cli binaries, as follows:</p>

```
sudo
apt-get update
apt-get upgrade
apt-get install transmission-cli transmission-common transmission-daemon transmission-remote-cli
```

<p><strong>Authentication:</strong><br>By default, transmission requires you to setup username / password. Since our goal is *not* to expose Transmission to the open internet (and we'll only use it via SSH), we'll simply neutralize any kind of authentication:</p>

```
nano /etc/transmission-daemon/settings.json
```

<p>Once there, edit this snippet:</p>

```
rpc-authentication-required: false
```

<p><strong>Logging:</strong><br>We want Transmission to keep an events log. Anything that goes wrong during setup... must be persisted, otherwise, debugging it will be a nightmare.</p>

<p>The only way i've found to set this up, is by means of the Daemon Service Descriptor:</p>

```
nano /lib/systemd/system/transmission-daemon.service
```

<p>Once there, you want to add the logfile's path. Make sure that the file exists, and Transmission's user has enough permissions to edit it:</p>

```
OPTIONS="--config-dir $CONFIG_DIR --logfile /var/log/transmission.log"
```

<p><strong>Filesystem Permissions:</strong></p>

<p>Transmission's user is specified in the transmission-daemon.service descriptor (which is debian-transmission). So... you really wanna make sure whatever shared folder you end up using, belongs to Transmission's group.</p>

```
usermod -a -G debian-transmission YOUR_USER
chgrp debian-transmission /DOWNLOADS/PATH
chmod 770 /DOWNLOADS/PATH
```

<p><strong>Magnets!</strong></p>

<p>In order to begin downloading a magned, try the following:</p>

```
transmission-remote-cli
(And press 'A')
```

<p><strong>Restarting Stopped</strong></p>

<p>Last tip: If you need to restart all of your downloads at once, this command becomes quite handy:</p>

```
transmission-remote -t all -s
```