---
title: "Making an iOS Assets Bundle"
date: 2013-01-16T20:16:41+00:00
slug: "making-an-ios-assets-bundle"
categories:
  - "iOS"
---

An iOS Bundle is just a folder which contains resources. Roughly speaking,  it allows you to store any resource you might need: images, nibs, or localized string files.

Why would you create an application bundle?. What's that good for?.

Suppose you have a framework of your own. And... suppose that your framework has several UIViewController which require custom images. OR, suppose that you need to load different images dynamically, within your framework's code.

You can't include those resources inside an iOS framework. So... that's where the bundles come in!.

Check out the Facebook SDK. Yup. It contains a bundle with few image resources.

<strong>[Step #1] : Adding a Bundle Target </strong>

Let's add a new target to our project, which will be the one responsible of generating the bundle.

First of all, we need to click over the project name in the navigator (1), and afterwards, over the 'add target' button at the bottom (2):

<a href="/making-an-ios-assets-bundle/updatingtarget-2/" rel="attachment wp-att-547"><img class="alignnone size-full wp-image-547" alt="UpdatingTarget" src="/wp-content/uploads/2013/01/UpdatingTarget1.png" width="895" height="440" /></a>

You can find the 'Bundle' target in the following path: 'Mac OSX &gt;&gt; Framework &amp; Library &gt;&gt; Bundle':

<a href="/making-an-ios-assets-bundle/addingbundle/" rel="attachment wp-att-537"><img class=" wp-image-537 alignnone" alt="AddingBundle" src="/wp-content/uploads/2013/01/AddingBundle.png" width="722" height="479" /></a>

Did you notice that we had to use the 'Bundle' target-template located inside MacOSX section?. Aaaand... did you notice that there is no Bundle target-template inside the iOS section?.

OSX and iOS bundles have a slightly different structure. We can use any of them both. But since we're working on iOS, let's switch to its own Bundle structure.

We need to change the 'base sdk' Build Setting for our new SomeResources target, as follows:

<a href="/making-an-ios-assets-bundle/updatingtarget/" rel="attachment wp-att-538"><img class="alignnone size-full wp-image-538" alt="UpdatingTarget" src="/wp-content/uploads/2013/01/UpdatingTarget.png" width="895" height="440" /></a>

Let's update the BaseSDK. Instead of Latest Mac OSX, please, click over that combo and select 'Latest iOS'.

Allright!. It's time to edit the Build Phases section of our Bundle. We've named our new target as 'SomeResources'. We just need to add all of our resources into the 'Copy Bundle Resources' section, as shown below:

<a href="/making-an-ios-assets-bundle/addingassets/" rel="attachment wp-att-539"><img class="alignnone size-full wp-image-539" alt="AddingAssets" src="/wp-content/uploads/2013/01/AddingAssets.png" width="896" height="442" /></a>

Note that, for this particular example, we're exporting three PNG images, a NIB file, and an InfoPlist.strings file. We'll see, later on, how to load these files.

In order to generate the bundle, we just need to select the 'SomeResources' schema:

<a href="/making-an-ios-assets-bundle/selectingschema/" rel="attachment wp-att-540"><img class="alignnone size-full wp-image-540" alt="SelectingSchema" src="/wp-content/uploads/2013/01/SelectingSchema.png" width="421" height="168" /></a>

Once we have the 'SomeResources' schema selected, we must hit "build" in order to generate the bundle file.

Your build-output folder should look as follows, assuming you're in debug mode. 'SomeResources.bundle' is ready to be distributed:

<a href="/making-an-ios-assets-bundle/builtbundle/" rel="attachment wp-att-541"><img class="alignnone size-full wp-image-541" alt="BuiltBundle" src="/wp-content/uploads/2013/01/BuiltBundle.png" width="241" height="78" /></a>

<b>
</b><strong>[Step #2] : Including SomeResources.bundle into a Sample project </strong>

How do we manage to import this new bundle into a new project?. Simply drag &amp; drop the 'SomeResources.bundle' file into your target app's Resources folder, as shown below. That's all you need to do.

<a href="/making-an-ios-assets-bundle/importingbundle-2/" rel="attachment wp-att-543"><img class="alignnone size-full wp-image-543" alt="ImportingBundle" src="/wp-content/uploads/2013/01/ImportingBundle1.png" width="578" height="338" /></a>

Up next... we'll learn how to:

- [Load NIBS from Asset Bundles.](/loading-nibs-stored-inside-a-bundle/ "Loading NIBs stored inside a bundle")
- [Load UIImages from files stored in bundles](/loading-uiimages-from-files-stored-inside-a-bundle/ "Loading UIImages from files stored inside a bundle").
- [Localize strings with dictionaries](/using-nslocalizedstring-with-a-dictionary-stored-inside-a-bundle/ "Using NSLocalizedString with a dictionary stored inside a bundle") (stored in bundles, again).

I hope you found this mini guide useful... somehow!.
Have fun!.