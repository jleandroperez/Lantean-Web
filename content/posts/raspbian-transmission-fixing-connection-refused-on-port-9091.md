---
title: "Raspbian + Transmission: Fixing \"Connection refused on port 9091\""
date: 2017-04-20T10:02:30+00:00
slug: "raspbian-transmission-fixing-connection-refused-on-port-9091"
categories:
  - "Raspberry"
---

I've just managed to solve a quite annoying glitch. After booting Raspbian, Transmission was immediately unable to connect to transmission-daemon on port 9091.

After much digging, i've found out that:

- Restarting the service just makes things work
- I was getting a bunch of error messages in /var/log/daemon.log (re: bind)
- Several posts in few forums suggested that the service was being initialized before the network adapter was actually ready.

Long story short:

1. Launch <strong>raspi-config</strong>
2. Select: <strong>3. Boot Options</strong>
3. Select: <strong>B2 Wait for Network at Boot</strong>

That's all you need, pretty much. Next time you boot, transmission-remote-cli will be able to connect immediately.
