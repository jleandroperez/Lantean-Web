---
title: "Loading SecCertificateRef from PEM String"
date: 2014-07-07T17:05:49+00:00
slug: "loading-seccertificateref-from-pem-string"
categories:
  - "iOS"
  - "OSX"
  - "Security"
---

In order to load a PEM certificate, you'd probably wanna grab the PEM itself from your backend, right?.

You can do so, by means of this command:

```
openssl s_client -showcerts -host host.com -port 443
```

Once you've got the certificate, you should <strong>get rid of the Begin/End Certificate substrings</strong>.

Cocoa Snippet itself is quite easy:

```
NSData *rawCertificate = [[NSData alloc] initWithBase64Encoding:PlaintextCertificateString];
SecCertificateRef parsedCertificate = SecCertificateCreateWithData(NULL, (__bridge CFDataRef)rawCertificate);

```

That's it. Don't forget about checking expiration dates. Unfortunately, Apple's API to do so is private, and i personally refuse to build OpenSSL into my app, just to check that.