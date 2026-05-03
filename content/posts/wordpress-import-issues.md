---
title: "WordPress Import Issues"
date: 2012-03-13T00:05:26+00:00
slug: "wordpress-import-issues"
categories:
  - "HTML5"
---

I've migrated this blog to a brand new domain. Thing is... i've been having lots of glitches and bugs while trying to import the wordpress XML containing all of my posts.

How did i solve it?. Well, it's probably not the best option, in terms of security. But i had to grant 777 permissions to the folder wp-contents/upload, and the same applies to the /tmp folder.

After that, everything worked like a charm. Besides that, i had lots of issues while trying to install the plugins i'd like to use!. Yeah... permissions again. The easy and quick workaround was to simply upload everything i need, already decompressed, to the folder wp-contents/plugins.

By doing so, i managed to get the plugins to show up in the Plugins tab, in the WP site manager. And... that's it!