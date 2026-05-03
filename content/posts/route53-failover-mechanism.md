---
title: "Route53 Failover Mechanism!"
date: 2013-05-27T20:49:18+00:00
slug: "route53-failover-mechanism"
categories:
  - "SEO"
---

Situation: you run your own website on an Amazon EC2 instance. Something happens: maybe the box runs out of resources (ddos, high traffic, you pick one!).
All of the sudden, your website is offline. Downtime means that Google will push it down in the ranking. So what do we do?.

Well, AWS Route53 has a new, and super cool mechanism, that allows you to set Health Checks. If the website doesn't pass it, the DNS record will switch to a failover entry.

How can we achieve this?. Amazon itself posted a detailed guide <a title="AWS Route53 Failover" href="http://aws.typepad.com/aws/2013/02/create-a-backup-website-using-route-53-dns-failover-and-s3-website-hosting.html">here</a>. Just for the record, <a title="Route53 HealthCheck" href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html">here</a> you will find details about when a website is considered healthy.

A couple details:

1. I've used [SiteSucker](http://sitesucker.us/ "SiteSucker"), a free OSX tool, that allows you to create a simple HTML backup. Running a static S3 backup is way cheaper than running two instances!.
2. If your apache logfile grows **a lot** due to the HealthCheck hits, you can disable the logs, if the user agent is "Route 53". Simply put the following in your .htaccess:
     
   ```
   SetEnvIfNoCase User-Agent .*Route 53.* dontlog
   ```
   Don't forget about tweaking your website.com.conf apache file, to look like this:
   ```
   CustomLog logs/access_log common env=!dontlog
   ```

This is just... sooooo cool!