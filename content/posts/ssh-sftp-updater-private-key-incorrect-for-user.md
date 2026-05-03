---
title: "SSH SFTP Updater : \"Private key incorrect for user\""
date: 2013-03-11T00:18:33+00:00
slug: "ssh-sftp-updater-private-key-incorrect-for-user"
categories:
  - "Offtopic"
---

If you're using <a href="http://wordpress.org/extend/plugins/ssh-sftp-updater-support/">Wordpress SSH SFTP</a> Updater plugin, and you got the error "Private Key is Incorrect for use"... even when the keys are correct, check the following:

```
nano /etc/ssh/sshd_config
```

If there is a "ForceCommand internal-sftp" directive, somewhere, in sshd's config, try disabling it. That was what was causing me issues:

I had an sftp-only user, and the WP plugin doesn't support that!.</pre>