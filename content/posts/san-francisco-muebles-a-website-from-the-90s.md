---
title: "San Francisco Muebles: A Website from the 90's!"
date: 2015-03-19T21:56:15+00:00
slug: "san-francisco-muebles-a-website-from-the-90s"
categories:
  - "Offtopic"
---

Several years ago (1999 to be precise!), i've started a simple website for my father's business: <a href="http://www.sfoficina.com.ar" title="San Francisco Muebles">San Francisco Muebles</a>.

This is how it used to look like (thanks god for <a href="http://web.archive.org">web.archive.org</a>!)

<a href="http://www.sfoficina.com.ar"><img src="/wp-content/uploads/2015/03/san-francisco-muebles.png" alt="san-francisco-muebles" width="1552" height="1112" class="aligncenter size-full wp-image-1830" /></a>

Back then, iframes, simple javascript, fancy flash buttons... and some plain html was, pretty much, the gold standard for a personal (OR business) website.

Over the years, my dad's website has evolved into many different incarnations: i've adopted Plain-PHP, Code Igniter, and jQuery to handle fancy transitions.

But at some point you hit a brickwall: how do i make this maintainable by anyone (not just me!) and extremely lightweight?. I do run my own Amazon Box... can i also have an extra backup layer, just in case i break my EC2 instance?

<strong>What is <a href="http://jekyllrb.com">Jekyll</a>? </strong>
It's a simple tool, written in Ruby, that allows you avoid HTML duplication: if you've got many pages that should look the same way, you simply get to write a template, and reuse it all over.

<strong>Why Jekyll?</strong>
Jekyll is the engine behind <a href="https://pages.github.com">Github Pages</a>, and it simply caught my eye.

<strong>What is so great about having a website in Plain HTML?</strong>
Simply put, the resources required to host a Plain HTML website are extremely low.

Plus, you get to use Route53 Failover Mechanism: your website is constantly monitored. If anything goes wrong, Route53 takes over, and maps your domain elsewhere. In my case, Amazon S3 will just kick in, and serve the site.

<strong>Conclusions!</strong>
Implementing Jekyll has been a fun (and quite successful) experiment. It just took under 8 hours to do the whole thing.

However, some knowledge is still required: you need to execute a script, and upload the output to the server. Which is okay, but... there are many ways in which things can go wrong.

Bottomline: there is nothing easier, and more parent-friendly, than <a href="https://pages.github.com">WordPress</a>. Which is precisely the reason why the next incarnation will be WP based!