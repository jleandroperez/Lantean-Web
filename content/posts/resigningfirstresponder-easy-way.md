---
title: "resignFirstResponder, the easy way!"
date: 2012-06-19T17:08:05+00:00
slug: "resigningfirstresponder-easy-way"
categories:
  - "iOS"
---

If you have an UIControl in edit mode... but you have no idea which one is it... and you need to resignFirstResponder, there is an easy way to do this. No, you don't need to hook to notifications. And you don't need to find the firstResponder. This can be solved with just one call.

What you need to do is...

```
[_tableView endEditing:YES]
```

Note that you could have anything else rather than a _tableView.
Easy. Right?