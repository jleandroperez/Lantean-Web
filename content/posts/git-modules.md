---
title: "GIT Modules"
date: 2013-07-17T22:49:26+00:00
slug: "git-modules"
categories:
  - "Offtopic"
---

Equivalent to SVN Externals, GIT offers a nice feature called "Modules". Long short story, you get to link an external project, inside your own project.
What do you make out of this?. Well, suppose you're using a 3rd party library. You can update everything with just a command line pull. No need to download and merge, by hand.

Sounds nice, right?. It's done this way:

```
cd MyApp
git submodule add git://github.com/some-framework/some-framework.git Frameworks/SomeFramework

```

Afterwards, we need to recursively update the submodules. Which will, in turn, clone the 'some-framework' repository:

```
git submodule update --init --recursive

```