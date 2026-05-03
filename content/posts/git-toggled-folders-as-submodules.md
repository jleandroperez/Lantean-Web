---
title: "Git toggled folders as submodules!?"
date: 2014-06-23T22:08:29+00:00
slug: "git-toggled-folders-as-submodules"
categories:
  - "Offtopic"
tags:
  - "git"
---

Few days ago, i had to struggle with a strange scenario in which git began tracking a folder, as if it was a submodule.

Now, what's strange with that?: <strong>i didn't set any submodules</strong>!. My .gitmodule file was empty (in fact, i didn't even have that file).

Thanks to <a href="http://stackoverflow.com/questions/4185365/no-submodule-mapping-found-in-gitmodule-for-a-path-thats-not-a-submodule">this stackflow question</a>, i ended up figuring out this solution:

```
git ls-files --stage | grep 160000
git rm --cached  [Paths retrieved from the command above]
```

Hopefully, this will help another lost soul!