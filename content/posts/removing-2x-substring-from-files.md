---
title: "Removing \"@2x\" substring from files"
date: 2013-07-03T15:17:54+00:00
slug: "removing-2x-substring-from-files"
categories:
  - "OSX"
---

If you're reading this, probably... it's because the Art Designers of your team just sent you a bunch of SD assets, with the @2x substring... and you don't wanna spend the next 30 minutes cleaning that up... right?

If that's the case, you've come to the right place. Fire Terminal, open the containing folder, and type the following:

```
find . -type f -name "*@2x*" -exec sh -c 'echo mv "$0" "${0/@2x/}"' '{}' \;

```

<strong>
Note:</strong> you might have just noticed that this will actually echo the replacement. That's for safety. Validate the output, and proceed removing the 'echo' command call.