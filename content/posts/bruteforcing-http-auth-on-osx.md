---
title: "Bruteforcing Http Auth on OSX"
date: 2013-01-22T23:46:02+00:00
slug: "bruteforcing-http-auth-on-osx"
categories:
  - "Security"
---

<a href="/wp-content/uploads/2013/01/password-cracking.jpg"><img class="alignleft size-thumbnail wp-image-690" style="margin: 10px;" title="Bruteforcing" alt="password-cracking" src="/wp-content/uploads/2013/01/password-cracking.jpg" width="150" height="150" /></a>

Suppose you forgot the password of your router. What can you do?.... should you just reset the device?.
Nahhhh.... that's boring. That's why we're gonna try to bruteforce http basic authentication.

We're assuming that you run some incarnation of OSX, and you have <a title="Mac Ports" href="http://www.macports.org/" rel="nofollow">Mac Ports</a> installed. Right?.
We'll need to download hydra... a bruteforce tool... so... fire up a terminal, and type the following:

```
sudo port install hydra
```

So far so good. Now, we're gonna need to create our own password list. In order to do so, we'll rely on crunch. It's a nice shell tool, that builds on OSX as well. Download it <a title="Crunch" href="http://sourceforge.net/projects/crunch-wordlist/files/" rel="nofollow">here</a> first. If you get any troubles building it, try typing:

```
gcc crunch.c -o crunch
```

For some reason, the makefile isn't working... so i just built it right away with gcc.

Allright! we've got all what we need. Now, let's suppose we wanna generate passwords with 5 characters length, including lowercase, uppercase and numbers. So... we should fire up our terminal, and type this:

`./crunch 5 5 -f charset.lst mixalpha-numeric -o wordlist.txt`

Beware. That will take about 5 GB of space of your storage. Okay, okay. We're almost there. Now, it's time to try hydra. Try the following syntax:

```
hydra -l admin -P wordlist.txt -vV -s 80 HOSTNAME http-get /
```

Of course. We need the username, in this example we assume it's 'admin'. And we also assume that we're hitting port 80.
Good luck!