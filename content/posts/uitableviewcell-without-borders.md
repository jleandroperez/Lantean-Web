---
title: "UITableViewCell without borders!"
date: 2012-04-06T14:21:40+00:00
slug: "uitableviewcell-without-borders"
categories:
  - "iOS"
---

Suppose that you have an UITableView with a borderColor. Everything is cool and easy... as long as you don't need to break the mold.

But if you ever need to add just ONE single cell without borders, you'll notice that there is no way to do it. Well, it turns out that there is. But it's not a straightforward one. You simply need to do this:

```
UIView* emptyBackView = [[UIView alloc] initWithFrame:CGRectZero];
[cell setBackgroundView:emptyBackView];

[emptyBackView release];
emptyBackView = nil;

```

Magic, ha?. If you add an empty backgroundView (with its background set to clearColor), the cell's border will be gone.

I've been using this trick since iOS 3.1.2 times... and it's still valid for iOS 5.1, so go ahead, and get rid of those borders!