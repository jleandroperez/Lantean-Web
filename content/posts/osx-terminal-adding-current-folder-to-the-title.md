---
title: "OSX Terminal: Adding current folder to the title!"
date: 2012-03-08T22:00:21+00:00
slug: "osx-terminal-adding-current-folder-to-the-title"
categories:
  - "OSX"
tags:
  - "OSX"
---

If you're just like me, and have lots of Terminal tabs open, you probably end up typing 'pwd' all the time.

Luckily, there is an easy solution:

1. Create a file named '.profile', in your user's home.
2. Type the following string in there!:
   ```
   export PROMPT_COMMAND='echo -ne "\033]0;[${PWD/$HOME/~}]\007"'
   ```

That's it!. You're gonna have, from now on, the current working directory right there in the windows tab!.

&nbsp;