---
title: "Calculating NSData's MD5"
date: 2013-01-16T14:26:21+00:00
slug: "calculating-nsdatas-md5"
categories:
  - "iOS"
---

Suppose that you need to calculate a NSData's MD5 signature.. for whatever reason. Say... you need to check the backend's signature.

Well... simply add a NSData extension, with the following method:

```
- (NSString*)md5
{
    unsigned char result[16];
    CC_MD5( self.bytes, self.length, result ); // This is the md5 call
    return [NSString stringWithFormat:@"%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x",
            result[0], result[1], result[2], result[3], 
            result[4], result[5], result[6], result[7],
            result[8], result[9], result[10], result[11],
            result[12], result[13], result[14], result[15]
            ];  
}

```

Again, please, don't you forget the imports!

```
#import <CommonCrypto/CommonDigest.h>

```