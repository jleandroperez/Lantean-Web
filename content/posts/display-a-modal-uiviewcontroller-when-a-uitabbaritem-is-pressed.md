---
title: "Display a modal UIViewController when a UITabBarItem is pressed"
date: 2012-05-03T17:54:13+00:00
slug: "display-a-modal-uiviewcontroller-when-a-uitabbaritem-is-pressed"
categories:
  - "iOS"
---

Suppose the following scenario. You need to display a modal UIViewController whenever the user presses a specific button in a UITabBar.

The trick is pretty simple. First, add an empty UIViewController, wich will serve as placeholder for the 'modal tab':

```
UIViewController* someViewController    = [[UIViewController alloc] init];
[someViewController setTitle:NSLocalizedString(@"Modal Tab", nil)];
[someViewController.tabBarItem setImage:[UIImage imageNamed:@"modal.png"]];

```

Then, setup the UITabBarController's delegate:

```
[_tabBarController setDelegate:self];

```

At last... you need to implement the UITabBarControllerDelegate protocol. Specifically, something that looks like this:

```
- (BOOL)tabBarController:(UITabBarController*)tabBarController shouldSelectViewController:(UIViewController*)viewController

{
    BOOL isModalTab = ([[viewController title] isEqualToString:NSLocalizedString(@"Modal Tab", nil)]);

    if(isModalTab)
    {
        UIViewController* modalViewController = [[[ModalViewController alloc] init] autorelease];
        [self presentModalViewController:modalViewController animated:YES];
    }

    return !isModalTab;
}

```

That would do the trick..!

<div></div>