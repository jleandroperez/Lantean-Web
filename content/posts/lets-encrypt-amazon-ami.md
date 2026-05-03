---
title: "Let's Encrypt + Amazon AMI"
date: 2017-04-06T15:05:46+00:00
slug: "lets-encrypt-amazon-ami"
categories:
  - "OSX"
---

<p><strong>Download certbot</strong></p>

```
$ wget https://dl.eff.org/certbot-auto
$ chmod a+x certbot-auto
```

<p>Generate Certificates</p>

```
sudo ./certbot-auto --debug -v --server https://acme-v01.api.letsencrypt.org/directory certonly -d YOUR_WEBSITE_HERE
```

<p><strong>Auto Renew Script:</strong></p>

```
sudo crontab -e
0 1,13 * * * /home/ec2-user/certbot-auto renew
```

<p><a href="https://nouveauframework.org/blog/installing-letsencrypts-free-ssl-amazon-linux/">Source Here</a></p>
