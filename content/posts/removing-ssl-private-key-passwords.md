---
title: "Removing SSL Private Key Passwords"
date: 2016-09-09T10:16:09+00:00
slug: "removing-ssl-private-key-passwords"
categories:
  - "Security"
---

Yes. Again! For future self reference:

```
openssl rsa -in encrypted.key -out unencrypted.key
```