---
title: "Fixing: StatusBar covering your UIViewController's view"
date: 2014-10-31T18:52:48+00:00
slug: "fixing-statusbar-covering-your-uiviewcontrollers-view"
categories:
  - "iOS"
  - "OSX"
---

Ever since iOS 7, if you're not using a UINavigationController instance, you'll need to perform a very simple step, in order to prevent iOS's StatusBar from covering your view:

1. Press Control, click over the "Top Layout Guide", and drag it upon the troublesome view.
2. You'll get a small popup. Please, click on "Vertical Spacing".
3. Edit the new constraint, and update the Constant value, as needed.

<a href="https://developer.apple.com/library/ios/qa/qa1797/_index.html">Reference here!</a>