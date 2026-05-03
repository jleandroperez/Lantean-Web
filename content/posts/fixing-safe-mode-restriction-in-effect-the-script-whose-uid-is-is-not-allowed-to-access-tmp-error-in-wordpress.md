---
title: "Fixing 'SAFE MODE Restriction in effect. The script whose uid is  is not allowed to access /tmp' error in WordPress"
date: 2013-01-09T15:14:37+00:00
slug: "fixing-safe-mode-restriction-in-effect-the-script-whose-uid-is-is-not-allowed-to-access-tmp-error-in-wordpress"
categories:
  - "HTML5"
---

Long short story. If you wanna update, say, a plugin, or a theme.. using wordpress, and you get the following error:
```
SAFE MODE Restriction in effect. The script whose uid is  is not allowed to access /tmp
```
I've got news for you!. It's caused by the php_safe_mode flag. If you're on a shared hosting, and you cannot change that flag (or maybe you just don't want to)... here's what you need to do:

1. Create a temporary folder, somewhere in your hosting, and set the permissions to 777.
2. Open your wp-config.php file.
3. Add this line: define('WP_TEMP_DIR','/absolute/path/to-a-tmp-folder/');

That should do the trick.