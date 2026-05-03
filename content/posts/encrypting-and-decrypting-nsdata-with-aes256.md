---
title: "Encrypting and Decrypting NSData with AES256"
date: 2013-01-16T14:24:09+00:00
slug: "encrypting-and-decrypting-nsdata-with-aes256"
categories:
  - "iOS"
---

Today we're gonna encrypt information, stored in a NSData object, using AES-256 algorithm. As you may already know, AES-256 is a symmetric encryption schema. Which means that you need to share, somehow, the key you're gonna use (in order to decrypt the data).

I've encapsulated a couple helper methods, as a NSData extension, for the sake of simplicity. I've based myself on <a href="http://stackoverflow.com/questions/6527761/aes-with-commoncrypto-uses-too-much-memory-objective-c" rel="nofollow">this</a>. Let's see...

```
- (NSData*)aes256EncryptWithKey:(NSString*)key
{
    // 'key' should be 32 bytes for AES256, will be null-padded otherwise
    char keyPtr[kCCKeySizeAES256 + 1];
    bzero( keyPtr, sizeof( keyPtr ) );

    // fetch key data
    [key getCString:keyPtr maxLength:sizeof( keyPtr ) encoding:NSUTF8StringEncoding];

    NSUInteger dataLength = [self length];

    // See the doc: For block ciphers, the output size will always be less than or equal to the input size plus the size of one block.
    // That's why we need to add the size of one block here
    size_t bufferSize = dataLength + kCCBlockSizeAES128;
    void *buffer = malloc( bufferSize );

    size_t numBytesEncrypted = 0;
    CCCryptorStatus cryptStatus = CCCrypt( kCCEncrypt, kCCAlgorithmAES128, kCCOptionPKCS7Padding,
                                          keyPtr, kCCKeySizeAES256,
                                          NULL /* initialization vector (optional) */,
                                          [self bytes], dataLength, /* input */
                                          buffer, bufferSize, /* output */
                                          &numBytesEncrypted );
    if( cryptStatus == kCCSuccess )
    {
        // The returned NSData takes ownership of the buffer and will free it on deallocation
        return [NSData dataWithBytesNoCopy:buffer length:numBytesEncrypted];
    }

    free( buffer );
    return nil;
}

```

And now... the decrypt routine...

```
- (NSData*)aes256DecryptWithKey:(NSString*)key
{
    // 'key' should be 32 bytes for AES256, will be null-padded otherwise
    char keyPtr[kCCKeySizeAES256+1];
    bzero( keyPtr, sizeof( keyPtr ) );

    // fetch key data
    [key getCString:keyPtr maxLength:sizeof( keyPtr ) encoding:NSUTF8StringEncoding];

    NSUInteger dataLength = [self length];

    // See the doc: For block ciphers, the output size will always be less than or equal to the input size plus the size of one block.
    // That's why we need to add the size of one block here
    size_t bufferSize = dataLength + kCCBlockSizeAES128;
    void *buffer = malloc( bufferSize );

    size_t numBytesDecrypted = 0;
    CCCryptorStatus cryptStatus = CCCrypt( kCCDecrypt, kCCAlgorithmAES128, kCCOptionPKCS7Padding,
                                          keyPtr, kCCKeySizeAES256,
                                          NULL /* initialization vector (optional) */,
                                          [self bytes], dataLength, /* input */
                                          buffer, bufferSize, /* output */
                                          &numBytesDecrypted );

    if( cryptStatus == kCCSuccess )
    {
        // The returned NSData takes ownership of the buffer and will free it on deallocation
        return [NSData dataWithBytesNoCopy:buffer length:numBytesDecrypted];
    }

    free( buffer );
    return nil;
}

```

Ahhhh... don't you forget about the imports!

```
#import <CommonCrypto/CommonDigest.h>
#import <CommonCrypto/CommonCryptor.h>

```