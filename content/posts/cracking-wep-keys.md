---
title: "Bruteforcing WEP Keys"
date: 2012-05-26T12:35:41+00:00
slug: "cracking-wep-keys"
categories:
  - "Security"
---

<a href="/wp-content/uploads/2012/05/Screen-Shot-2012-05-26-at-12.23.36-PM.png"><img class="alignleft size-thumbnail wp-image-403" title="Screen Shot 2012-05-26 at 12.23.36 PM" alt="" src="/wp-content/uploads/2012/05/Screen-Shot-2012-05-26-at-12.23.36-PM.png" width="150" height="139" /></a>

Today... we'll take a look at WEP key-breaking. We'll use a linux live-cd distribution called <a href="http://www.backtrack-linux.org/downloads/" rel="nofollow">backtrack</a>. It's a linux distribution bundled with a load of hacking / cracking tools. It's free, and it's pretty cool.

So... first step... download and burn it!.
I'll assume you know how to boot it and launch a bash terminal. Let's begin from there.
We're gonna use two command-line tools: airodump-ng and aircrack-ng. So... let's open a terminal, and type the following commands:

```
airmon-ng start [interface]
(Your interface is probably gonna be called something like wlan0...  you can check the available interfaces with ifconfig command).
airodump-ng wlan0 --write OUTPUT-FILE

```

What's going on here?. Airmon will set your wifi card into promiscuous mode. Which means that it won't just let you see packets sent to your own mac address. Instead, you're gonna need to monitor all of the traffic in the air.

On top of that, airodump-ng will dump into a file all of the traffic recorded. Why?. In order to successfully crack a WEP key, you need to gather at least 10k 'Initialization Vectors'. We're not gonna get into details of what is that... not in this post. But the point is that.. wanna crack a WEP... need a lot of traffic.

Let's go on. Launch a second bash terminal, and type the following:

```
aircrack-ng OUTPUT-FILE-01.cap
```

This second tool is gonna ask you which network is it that you wanna crack, and it'll try to break the WEP encryption. If it's unable to do it with the current traffic log, you'll get a message saying something like 'try with 10000 IVs', or 'try with 15000'.

It's just a matter of time now...