---
title: "Embedding NSTokenField inside NSScrollView"
date: 2020-06-16T15:59:12+00:00
slug: "embedding-nstokenfield-inside-nsscrollview"
categories:
  - "OSX"
---

<figure class="wp-block-image size-large"><img src="/wp-content/uploads/2020/06/Constraints.png" alt="" class="wp-image-2562"/></figure>

<p>In order to get <strong>NSTokenField</strong> (or <strong>NSTextField</strong>) play well with a ScrollView, you should:</p>

1. Pin the fixed edges (in my case: Top / Bottom / Left)
2. Leave alone the edges that can grow (again, in my case: Right)
3. Set a placeholder Intrinsic Size, to keep IB happy
4. Override **intrinsicContentSize**

<p><strong>Notes:</strong></p>

- Pinning the TokenField to every single edge simply causes the container view to assume the actual TokenField's size (and thus, kills the scrolling behavior).
- [Sample code available here!](https://github.com/Automattic/simplenote-macos/pull/558/files)

<p></p>
