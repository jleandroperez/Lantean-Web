---
title: "Debugging BAD_ACCESS crashes"
date: 2012-04-15T23:26:15+00:00
slug: "debugging-bad_access-crashes"
categories:
  - "iOS"
---

Newbies can rely on ARC to handle memory management. But personally, i'd rather handling everything myself. Old school!.

Besides that, you'll probably need to support iOS 4 devices, as well. So... at least for now, Memory Management is kind of a mandatory chapter, to everyone!.

So what happens when you get a 'BAD_ACCESS' crash?. There are just so many scenarios that can trigger that crash... but the most common is simply a message sent to a dealloc'ed object.

Objective C runtime comes with a really powerful feature: Zombies!. By setting a flag, 'release' objects are, internally, replaced by a 'placeholder object'.

What's the meaning of this?. Simple!. ObjC runtime helps you determine if there is any released object that's getting sent a message. If that's the case, you'll get a message in Xcode console.

How do we enable Zombies?. Mmmmmm... in Xcode 4.3.2, you need to do this:

1. Product &gt;&gt; Manage Schemes &gt;&gt; Bottom left corner... 'Edit'
2. Select 'Run' in the left column
3. Select the 'Arguments' tab
4. Add an 'Environment Variable' called NSZombieEnabled, with 'YES' as value.

<strong>Important</strong>: Remember to remove this setting after you're done. Otherwise, 'Leaks' instrument will be... useless!

&nbsp;