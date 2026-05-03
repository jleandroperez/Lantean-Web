---
title: "GIT over Socks5: Or how to get around Paris's Mall SSL filters"
date: 2017-01-11T14:22:15+00:00
slug: "git-over-socks5-or-how-to-get-around-pariss-mall-ssl-filters"
categories:
  - "Security"
---

```

git config --global --get socks.proxy
git config --global --unset socks.proxy
git config --global socks.proxy socks5://127.0.0.1:9050
```