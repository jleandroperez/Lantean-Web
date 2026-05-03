---
title: "Fixing \"application is damaged, can’t be used to install macOS\" Error"
date: 2020-03-13T15:08:02+00:00
slug: "fixing-application-is-damaged-cant-be-used-to-install-macos-error"
categories:
  - "OSX"
---

<figure class="wp-block-image size-large"><img src="/wp-content/uploads/2020/03/Screen-Shot-2020-03-13-at-3.02.48-PM.png" alt="" class="wp-image-2537"/></figure>

<p>This error, thrown while trying to install an old macOS version (probably in a VM!) is caused by an expired certificate.</p>

<p>Good news is: this can be fixed, by deleting a file within the installer itself:</p>

1. Right click on the **Installer XXX.dmg**
2. Click over **Show Package Contents**
3. Open **Contents > Shared Support**
4. Nuke **InstallInfo.plist**

<p>🔥</p>
