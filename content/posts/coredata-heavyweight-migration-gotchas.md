---
title: "CoreData HeavyWeight Migration Issues"
date: 2014-10-25T10:45:36+00:00
slug: "coredata-heavyweight-migration-gotchas"
categories:
  - "iOS"
  - "OSX"
---

We recently hit a pretty severe bug. In one of our apps, users began experiencing token issues after an upgrade.

Bottomline?... the last upgrade had a Heavyweight migration. So far so good, but what happened?. Turns out that the <strong>URIRepresentation</strong> that can be used to map a <strong>NSManagedObjectID</strong>, is and is not reliable. Everything is okay, until you perform a heavyweight migration!.

Heavyweight migrations might swizzle your NSManagedObjectID's. Fix?, create your own <strong>primaryKeys</strong>. <strong>NSUUID</strong> helper class is the easiest way to accomplish that.

<a href="https://devforums.apple.com/message/480640#480640">Reference here!</a>
