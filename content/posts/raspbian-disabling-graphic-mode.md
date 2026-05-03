---
title: "Raspbian: Disabling Graphic Mode"
date: 2017-04-14T15:25:55+00:00
slug: "raspbian-disabling-graphic-mode"
categories:
  - "Raspberry"
---

<p><strong>Why:</strong> because i'm setting up my Raspberry as a private server, and i really don't need the XWindow overhead!</p>

<p><strong>How:</strong> As follows!</p>

```
systemctl get-default
```

<p>Verify that the output is: <strong>graphical.target</strong>.<br>Now... type the following!</p>

```
sudo systemctl set-default multi-user.target
```

<p><a href="https://raspberrypi.stackexchange.com/questions/31439/trying-to-turn-off-x11-in-jessie">Ref. Here</a></p>

<p>--</p>

<p><strong>Update:</strong></p>

<p>Simpler way? just run <strong>raspi-config</strong> and change the setting right there!</p>
