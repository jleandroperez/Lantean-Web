---
title: "Swift: Unit Testing"
date: 2015-07-24T16:50:49+00:00
slug: "swift-unit-testing"
categories:
  - "iOS"
  - "OSX"
---

I've recently stumbled upon severe issues, while trying to write a Unit Test, in Swift, that would access Swift Code that belongs to the main app.

Contrary to what <del datetime="2015-07-24T19:47:54+00:00">almost</del> everyone mentions, you should <strong>not import</strong> the Main App's files into the Testing target.

Instead, this is what you should do:

- Enable **Defines Module** in the main target.
- Add an **import** at the top of the Unit Test, to make the main project visible.
- Make sure that the classes to be tested are set to **public**.

<a href="http://www.andrewcbancroft.com/2014/12/29/getting-started-unit-testing-swift/">Reference Here!</a>