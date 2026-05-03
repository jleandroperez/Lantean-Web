---
title: "Showing current folder in Terminal's Title"
date: 2013-01-16T19:55:07+00:00
slug: "showing-current-folder-in-terminals-title"
categories:
  - "OSX"
---

This is a nice trick i've learnt not long ago. Nice, and useful. If you run OSX, and you'd like Terminal to display the current folder, in its title... to looks something like this:

<p style="text-align: center;"><a href="/showing-current-folder-in-terminals-title/terminaltitle/" rel="attachment wp-att-532"><img class="size-full wp-image-532 aligncenter" alt="TerminalTitle" src="/wp-content/uploads/2013/01/TerminalTitle.jpg" width="581" height="133" /></a></p>

All you need to do is to edit the .profile in your home directory, and type the following line:

```
export PROMPT_COMMAND='echo -ne "\033]0;[${PWD/$HOME/~}]\007"'
```

Nice, right?