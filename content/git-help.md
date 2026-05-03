---
title: "GIT Help!"
date: 2015-03-19T23:14:05+00:00
slug: "git-help"
build:
  list: never
---

### Delete local branches with no remote

```bash
git branch --merged develop | grep -Ev "(master|release|hotfix|develop)" | xargs git branch -d
```

### Selective Stash

```bash
git stash -p
```

### Rename Pushed Branch

```bash
git branch -m old_branch new_branch           # Rename branch locally
git push origin :old_branch                   # Delete the old branch
git push --set-upstream origin new_branch     # Push the new branch, set local branch to track the new remote
```

### Merge Theirs

```bash
git merge --strategy-option theirs
```

### Push a Tag

```bash
git tag -a "v1.5" -m "Adding Tag v1.5"
git push origin v1.5
```

### Delete a Tag

```bash
git tag -d [tag]
git push origin :refs/tags/[tag]
```

### Interactive Amend

```bash
git rebase -i HEAD~<N>
```

### Revert Last Commit

```bash
git reset --soft HEAD^
```

### Checkout 3 Rev Backwards

```bash
git checkout HEAD~3
```

### Merge Cherry Pick from Another Remote

```bash
git remote add some-remote https://github.com/Else/Where.git
git fetch some-remote
git cherry-pick HASH
```

### Logs between Tag + develop

```bash
git log v0.6.1..develop
```

### Move Pushed Commits to a New Branch

```bash
git branch their-branch master
git reset --hard master $SHA1_OF_C
git push --force $SHARED_REPO_REMOTE
```
