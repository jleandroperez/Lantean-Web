---
title: "TextKit + iOS Clipping Bug"
date: 2014-08-15T01:06:15+00:00
slug: "textkit-ios-clipping-bug"
categories:
  - "iOS"
---

I've just spent several hours hunting an iOS 8 specific bug. After inserting several new lines into a UITextView (with custom TextKit stack), the newly-added text would not appear.

This is the way our NSTextContainer instance was being initialized

```
@implementation MyTextView
- (instancetype)init {
    SPInteractiveTextStorage *textStorage = [[MyInteractiveTextStorage alloc] init];
    NSLayoutManager *layoutManager = [[NSLayoutManager alloc] init];

    NSTextContainer *container = [[NSTextContainer alloc] initWithSize:CGSizeMake(0, CGFLOAT_MAX)];
    container.widthTracksTextView = YES;
    container.heightTracksTextView = YES;

    [layoutManager addTextContainer:container];
    [textStorage addLayoutManager:layoutManager];

    self = [super initWithFrame:CGRectZero textContainer:container];
// ...

```

Now, the interesting part is, specifically, <strong>heightTracksTextView = YES</strong>.

After several debugging hours, i figured out that iOS 7 was setting, by default heightTracksTextView to NO, after setting the UITextView's scrollEnabled property.

Guess what? that's different in iOS 8. Calling setScrollEnabled is not backfiring anymore. For some reason, if you just disable heightTracksTextView, and initialize your UITextView instance with that custom NSTextContainer, any call to the <strong>caretRectForPosition</strong> method will fail.

By that, i mean, <strong>caretRectForPosition</strong> will return an invalid position. Workaround? manually disabling heightTracksTextView, right after calling the super initialized.

By the way, for future reference, <a href="http://inessential.com/2014/01/07/uitextview_scroll-to-typing_bug">this post</a> and <a href="http://inessential.com/2014/01/07/uitextview_the_solution">this one</a> helped me understand i wasn't alone in Mordor.