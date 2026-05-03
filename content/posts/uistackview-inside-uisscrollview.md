---
title: "UIStackView inside UISScrollView"
date: 2017-03-09T16:40:48+00:00
slug: "uistackview-inside-uisscrollview"
categories:
  - "OSX"
---

1. Disable tAMIC

```
scrollView.translatesAutoresizingMaskIntoConstraints = false
stackView.translatesAutoresizingMaskIntoConstraints = false

```

2. Pin the ScrollView

```
NSLayoutConstraint.activate([
  scrollView.leadingAnchor.constraint(equalTo: leadingAnchor),
  scrollView.trailingAnchor.constraint(equalTo: trailingAnchor),
  scrollView.topAnchor.constraint(equalTo: topAnchor),
  scrollView.bottomAnchor.constraint(equalTo: bottomAnchor)
  ])

```

3. Pin the StackView to the ScrollView corners. Include minimum width + padding:

```
let padding = CGFloat(10)
NSLayoutConstraint.activate([
  stackView.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor, constant: padding),
  stackView.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor, constant: -padding),
  stackView.topAnchor.constraint(equalTo: scrollView.topAnchor),
  stackView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor),
  stackView.heightAnchor.constraint(equalTo: scrollView.heightAnchor),
  stackView.widthAnchor.constraint(greaterThanOrEqualTo: scrollView.widthAnchor, constant: -2 * padding)
])

```