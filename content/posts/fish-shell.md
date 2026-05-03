---
title: "Fish Shell"
date: 2015-01-02T11:01:29+00:00
slug: "fish-shell"
categories:
  - "OSX"
---

Installing Fish: 

```
brew install fish

```

Displaying the branch name in the prompt:

Place the following script here: <strong>~/.config/fish/config.fish</strong>

```
set fish_git_dirty_color red
set fish_git_not_dirty_color green

function parse_git_branch
  set -l branch (git branch 2> /dev/null | grep -e '\* ' | sed 's/^..\(.*\)/\1/')
  set -l git_diff (git diff)

  if test -n "$git_diff"
    echo (set_color $fish_git_dirty_color)$branch(set_color normal)
  else
    echo (set_color $fish_git_not_dirty_color)$branch(set_color normal)
  end
end

function fish_prompt
  if test -d .git
    printf '%s@%s %s%s%s:%s> ' (whoami) (hostname|cut -d . -f 1) (set_color $fish_color_cwd) (prompt_pwd) (set_color normal) (parse_git_branch)
  else
    printf '%s@%s %s%s%s> ' (whoami) (hostname|cut -d . -f 1) (set_color $fish_color_cwd) (prompt_pwd) (set_color normal)
  end
end

```

<a href="http://zogovic.com/post/37906589287/showing-git-branch-in-fish-shell-prompt" rel="nofollow">Reference here</a> (Thanks for sharing the snippet!)