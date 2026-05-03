---
title: "iOS 8 Autosizing Cells"
date: 2014-12-11T09:42:44+00:00
slug: "ios-8-autosizing-cells"
categories:
  - "iOS"
---

The latest iOS release (8.0 at the time this was written!) added a new cool feature: autosizing cells. Meaning that we don't really need to implement <strong>tableView:heightForRowAtIndexPath:</strong> anymore.

How can we enable this?. Super simple, just add the following snippet:

```
self.tableView.estimatedRowHeight = SomeConstant;
self.tableView.rowHeight = UITableViewAutomaticDimension;

```

Now, here's the deal. iOS 7 still requires <strong>tableView:heightForRowAtIndexPath:</strong> to be implemented. And if you do implement it, iOS 8 will disregard the Automatic Dimension settings.

Solution?.. import <strong>objc/runtime.h</strong>, and place this hack in your UITableView's delegate:

```
- (BOOL)respondsToSelector:(SEL)aSelector {
  if (sel_isEqual(aSelector, @selector(tableView:estimatedHeightForRowAtIndexPath:)) ||
    sel_isEqual(aSelector, @selector(tableView:heightForRowAtIndexPath:))) {
      return false;
  }
  return [super respondsToSelector:aSelector];
}

```

YES. It's a hack =)