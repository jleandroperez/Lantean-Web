---
title: "Detaching subdirectory into it's own GIT repository"
date: 2018-05-18T09:50:36+00:00
slug: "detaching-subdirectory-into-its-own-git-repository"
categories:
  - "OSX"
---

1. Move folder to it's own branch

<blockquote>git subtree split -P name-of-folder -b name-of-new-branch</blockquote>

2. Initialize the new Repository

<blockquote>git checkout new-repository-url

git pull path-to-big-repository name-of-new-branch</blockquote>

And that's it, pretty much!
