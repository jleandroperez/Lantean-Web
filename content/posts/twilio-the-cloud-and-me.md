---
title: "Twilio, the Cloud... and Me!"
date: 2017-04-12T16:59:30+00:00
slug: "twilio-the-cloud-and-me"
categories:
  - "Offtopic"
---

<p>Today, we'll briefly detail how to setup a Twilio VoIP number in a way that it'll allow us to:</p>

<p>- Receive SMS's via Email<br>- Send SMS's via CLI<br>- Receive Voice Calls via Landline, and if nobody picks up, fallback to Softphone<br>- Make Voice Calls via Softphone</p>

<p><strong>Before we begin, you'll need to:</strong></p>

<p>1. Signup!<br>2. Register a Number!<br>3. Create a <strong>SIP Domain</strong><br>4. Add a User under the SIP Domains &gt; Credential Lists<br>5. Setup this <a href="https://support.twilio.com/hc/en-us/articles/223181788-Forwarding-SMS-messages-to-your-email-inbox">"SMS to Email" PHP script"</a>, in your favorite EC2 box</p>

<p>Once ready, let's open the Developer Center, and opening the TwiML bins. Once there, add the following TwiML's:</p>

<p><strong>Name:</strong> Incoming Voice to Softphone:</p>

```
<!--?xml version="1.0" encoding="UTF-8"?-->

USER@SIP-DOMAIN.sip.us1.twilio.com
```

<p><strong>Name:</strong> Incoming Voice to Landline:</p>

```
<!--?xml version="1.0" encoding="UTF-8"?-->

Please, hold on the line while i put you through.

YOUR-LANDLINE-NUMBER
```

<p><strong>Name:</strong> Incoming SIP to Destination:</p>

```
<!--?xml version="1.0" encoding="UTF-8"?-->

{{#e164}}{{To}}{{/e164}}
```

<p><strong>Name:</strong> Incoming SMS to Email:</p>

```
<!--?xml version="1.0" encoding="UTF-8"?-->

URL-MAPPED-TO-YOUR-SEND-MAIL-SCRIPT
```

<p>&nbsp;</p>

<p>Once ready, open <strong>Phone Numbers</strong> &gt; <strong>Manage Numbers</strong> &gt; <strong>Active Numbers</strong> and map everything as follows:</p>

<p>- <strong>A call comes in:</strong> Incoming voice to Landline TwiML<br>- <strong>A message comes in:</strong> Incoming SMS to email Script's URL</p>

<p>Finally, we need to map the <strong>"Incoming Voice to Softphone"</strong> TwiML, as follows:</p>

<p>- Open <strong>Programmable Voice</strong><br>- Open <strong>SIP Domains</strong> and click over your domain<br>- Set the "Incoming Voice to Softphone" TwiML URL in the <strong>Voice Configuration</strong> &gt; <strong>Request URL</strong> field</p>

<p>That should be it, pretty much. As per Soft Phones available for macOS, the most common one is X-Lite, which offers a free version (and it's also available for iOS).</p>

<p>Hope that helps!</p>

<p>--</p>

<p>P.s.: With the following snippet, placed in you ~/.profile, you should be also able to send SMS's via CLI:</p>

```
function sms() {
curl -X POST 'https://api.twilio.com/2010-04-01/Accounts/ACCOUNT-KEY/Messages.json' \
--data-urlencode "To=${@:1:1}" \
--data-urlencode "From=YOUR-TWILIO-PHONE" \
--data-urlencode "Body=${@:2:1}" \
-u USER-KEY:USER-SECRET
}
```