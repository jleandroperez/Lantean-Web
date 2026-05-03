---
title: "UITableView: Make room for a new cell, and insert it!"
date: 2012-03-16T22:06:35+00:00
slug: "uitableview-make-room-for-a-new-cell-and-insert-it"
categories:
  - "iOS"
---

Suppose you wanna insert a new row at the bottom of a table. The first thing you need to do is to calculate the content offset. Suppose you already know the height of the new cell, and it's stored into the variable 'newCellsHeight'. Then...

```
CGPoint contentOffset = CGPointZero;

contentOffset.y = _tableView.contentSize.height
                  + newCellsHeight
                  - _tableView.frame.size.height
                  + _tableView.contentInset.bottom;</pre>
Once you've calculated the contentOffset (considering the current contentInsets)... you should make sure it's a non-negative value, to prevent quirks:

// Do we need to scroll down?
if(contentOffset.y &gt; 0.0f)
{
    [_tableView setContentOffset:contentOffset animated:YES];
}

```

The last step would be to actually insert the rows. Please, consider that a delay should be applied, so the insert rows animations won't break the scroll animation!