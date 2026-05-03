---
title: "OSX: Renaming Fonts (For Free!)"
date: 2012-03-29T23:22:07+00:00
slug: "osx-renaming-fonts-for-free"
categories:
  - "iOS"
  - "OSX"
---

I just got a huge problem. I'm working on an iOS app, and it turns out that we need to maintain compatibility with iOS 4. So... the problem is that we use custom fonts. A lot of them. That shouldn't be an issue. BUT... i got to notice that iOS 4 supports up to two different fonts per family.

Long short story, if you've got a font family with... 5 different fonts, iOS 4 will load just two of  them. So how do we solve it?.

Simple!. We rename some of the extra fonts. Thing is, there are lots of tools to do that. But they're paid. And... dude, it's just renaming a font!. That's where <a title="TTX" href="http://sourceforge.net/projects/fonttools/">TTX</a> comes in.

TTX is an opensource tool that basically converts a font into a readable XML. So... you just need to parse your OTF file, change the font name... and run TTX again, to pack it up into an OTF file, back again.

So far so good. But i was getting an error while trying to run TTX on OSX 10.7.3. The problem is that TTX works fine only in 32 bits mode.

So.... if you're also having problems, just run this command, and you're good to go:

```
defaults write com.apple.versioner.python Prefer-32-Bit -bool yes

```
