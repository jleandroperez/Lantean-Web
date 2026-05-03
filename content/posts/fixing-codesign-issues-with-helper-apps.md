---
title: "Fixing Codesign Issues with Helper Apps"
date: 2013-06-19T13:15:40+00:00
slug: "fixing-codesign-issues-with-helper-apps"
categories:
  - "OSX"
---

I've been getting "Invalid binary" errors, while trying to upload a binary to the AppStore. The solution can be found in stackoverflow, i'm just pasting it here, for future reference...

<strong>1. Re-Codesign the Helper app from terminal:</strong>
```
codesign -f -s "3rd Party mac Developer Application:" -i "com.bundle.YOUR.HELPER" --entitlements path/to/helper/entitlements YOUR-HELPER.app
```

<strong>2.   Remove provisioning profile from Helper app, adding a "Run script" into the "Build Phases":</strong>

```
rm "${BUILT_PRODUCTS_DIR}/${PRODUCT_NAME}.app/Contents/Library/LoginItems/YOUR-HELPER.app/Contents/embedded.provisionprofile"
```

After this, i managed to upload the binary!

&nbsp;