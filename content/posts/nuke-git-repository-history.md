---
title: "Nuke GIT Repository History"
date: 2014-02-13T09:16:48+00:00
slug: "nuke-git-repository-history"
categories:
  - "Offtopic"
---

Suppose you've just commited a private API key that should not be public. Or maybe you just wanna restart your repository, because you've just finished major surgery and wanna start fresh.

If you'd like to delete all GIT history, you'd need to:

1. Remove all history

```
rm -rf .git
```

2. Reconstruct the Git repo with only the current content

```
git init
git add .
git commit -m "Initial commit"
```

3. Push to GitHub.

```
git remote add origin <github-uri>
git push -u --force origin master
```

<a href="http://stackoverflow.com/questions/9683279/how-do-i-remove-all-version-history-for-a-git-github-repository">Source here</a>.