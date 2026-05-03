---
title: "Sparkle in Sandbox Mode"
date: 2014-01-27T22:48:24+00:00
slug: "sparkle-in-sandbox-mode"
categories:
  - "OSX"
---

<p>If you're trying to distribute updates for your OSX app, outside the AppStore, still, with the AppSandbox enabled, you've come to the right place.</p>

<p>In the official Sparkle repository, you can find <a href="https://github.com/wbyoung/Sparkle">this pull request</a>. Since it hasn't been updated in a while, and the settings were fixed for OSX Lion, i've just forked the pull request, and pushed a couple fixes <a href="https://github.com/jleandroperez/Sparkle">here</a>.</p>

<p>Allright, so, how should you proceed?</p>

1. Clone the repository!
2. Open the **Build Phases** of your target and...
   1. Add **Sparkle.framework** as a dependency
   2. Link **Sparkle.framework** library
   3. Copy **Sparkle.framework** to 'Frameworks'
3. If you've done things right, your 'Build Phases' tab should look something like this:  
   > ![OSX Sparkle Sandboxed](/wp-content/uploads/2014/01/Screen-Shot-2014-01-27-at-10.31.09-PM.png)
4. Add a '**Run Script**' phase with the following snippet:

<blockquote>

<p style="padding-left: 40px;">LOCATION="${BUILT_PRODUCTS_DIR}/${FRAMEWORKS_FOLDER_PATH}"<br />IDENTITY="Developer ID Application: [INSERT YOUR IDENTITY NAME HERE]"<br />find "$LOCATION" -name '*.framework' -exec codesign --verbose --force --sign "$IDENTITY" {}/Versions/Current \;<br />codesign --verbose --force --sign "$IDENTITY" "$LOCATION/../XPCServices/com.andymatuschak.Sparkle.SandboxService.xpc"</p>

</blockquote>

<p> </p>

<p>That's it. After hitting 'Archive', your app should be able to auto-update itself.</p>

<p>References:<br />- <a href="http://stackoverflow.com/questions/20272170/os-x-app-update-issue-with-sparkle-under-mavericks-and-xcode-5/20287450#20287450">Codesign in Mavericks and Xcode 5 (Stackoverflow)</a><br />- <a href="http://support.hockeyapp.net/discussions/problems/16725-mac-app-store-code-signing-on-mavericks">Codesign in Mavericks and Xcode 5 (Hockeyapp)</a><br />- <a href="https://github.com/andymatuschak/Sparkle">Sparkle</a> (Thanks Andy, for sharing such an awesome project)</p>

<p></p>
