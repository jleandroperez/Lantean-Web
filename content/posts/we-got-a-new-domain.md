---
title: "We got a new domain!"
date: 2013-01-29T13:55:44+00:00
slug: "we-got-a-new-domain"
categories:
  - "SEO"
---

Well, as you might have noticed, we've got a brand new domain: lantean.co. This is sort of an experiment to me, to see if rankings can actually improve by leaving behind the .com.ar domain. (Since this site is written, essentially, in english, and .com.ar is geotargetted for Argentina).

<a href="/wp-content/uploads/2013/01/updating-domain-name.png"><img class="aligncenter" alt="updating-domain-name" src="/wp-content/uploads/2013/01/updating-domain-name.png" width="303" height="111" /></a>

What was done in order to attempt to prevent drops in rankings?.

1. 301 redirects from the old domain. How?. the .htaccess looks like this:
   ```
   RewriteCond %{HTTP_HOST} !^www.lantean.co$ [NC]
   RewriteRule ^(.*)$ /$1 [R=301,L]
   ```
2. I've indicated Google Webmaster Tools that the website has been moved. [Here](http://support.google.com/webmasters/bin/answer.py?hl=en&answer=83105 "Google Webmaster Tools") are the details.
3. I've crossed my fingers!

Stay tuned for updates!