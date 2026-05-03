---
title: "Removing local git branches that aren't in the remote repository"
date: 2015-03-12T10:48:38+00:00
slug: "removing-local-git-branches-that-arent-in-the-remote-repository"
categories:
  - "OSX"
---

New trick of the day. If you wanna cleanup your local git branches that were already merged, you could use this bash alias:

```
alias git_cleanup='git branch --merged develop | grep -Ev "(master|release|hotfix|develop)" | xargs git branch -d'
```

Props to Nick + Maxime!