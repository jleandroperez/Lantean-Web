---
title: "IPTables: Blocking your favorite Brute Force Attacker"
date: 2016-01-21T12:08:45+00:00
slug: "iptables-blocking-your-favorite-brute-force-attacker"
categories:
  - "OSX"
---

If you happen to detect a bruteforce attack on your self-hosted WP instance, this would be the IPTables syntax to block it:

<blockquote>iptables -A INPUT -s 119.81.130.34 -j DROP</blockquote>

Whenever you miss the attacker, and you're ready to unblock, you may just type:

<blockquote>iptables -D INPUT -s 119.81.130.34 -j DROP</blockquote>

Hope this helps!