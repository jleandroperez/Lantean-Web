---
title: "Loading UIImages from files stored inside a bundle"
date: 2013-01-16T20:28:45+00:00
slug: "loading-uiimages-from-files-stored-inside-a-bundle"
categories:
  - "iOS"
---

We've learnt before <a title="Making an iOS Assets Bundle" href="/making-an-ios-assets-bundle/">how to make an iOS Assets Bundle</a>. In this mini post... we'll learn how to learn images, stored in bundles. Okay.. this one is super simple:

```
UIImage* twitterBtnImage = [UIImage imageNamed:@"SomeResources.bundle/twitter-button.png"];

```

Of course, you need to have the 'SomeResources' bundle in your project. That's it!