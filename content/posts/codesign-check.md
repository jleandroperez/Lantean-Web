---
title: "Codesign Check"
date: 2014-06-26T10:38:28+00:00
slug: "codesign-check"
categories:
  - "iOS"
  - "OSX"
---

Keychain access for iOS apps is tied up to the provisioning profile you use to sign the binary. So, what happens if you release a new build, signed using a different provisioning profile?.

Yes! your guess is accurate!. You loose access to anything you've stored in the keychain, resulting in (probably) deauthentication.

There is a command that allows you to verify the "Keychain Access Group" for a given executable. By means of this, you'll be able to verify if your new release will have the same access than your previous build (assuming you also have that binary!).

Take notes...

```
codesign -d --entitlements - /path/AppName.OSX.1.0.2.xcarchive/Products/Applications/AppName.app/
```