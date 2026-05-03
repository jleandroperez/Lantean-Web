---
title: "Switching t2.micro > t3.micro"
date: 2019-02-26T23:08:17+00:00
slug: "switching-t2-micro-t3-micro"
categories:
  - "OSX"
---

<p>Okay… incoming boring post, so that i don't go insane searching for this.</p>

<p><strong>A. Verify you've got ena support:</strong></p>

```
[ec2-user ~]$ modinfo ena
filename:       /lib/modules/4.14.33-59.37.amzn2.x86_64/kernel/drivers/amazon/net/ena/ena.ko
version:        1.5.0g
(...)
```

<p><strong>B. Install </strong><a href="https://aws.amazon.com/cli/"><strong>AWS CLI</strong></a></p>

<p><strong>C. Figure out your instance ID:</strong></p>

```
$ aws ec2 describe-instances
```

<p><strong>C. Verify the current status of EnaSupport:</strong></p>

```
$ aws ec2 describe-instances --instance-ids INSTANCE_ID --query "Reservations[].Instances[].EnaSupport"
```

<p><strong>D. At this point you should probably stop the instance!</strong></p>

<p><strong>E. Enable ENA</strong></p>

```
$ aws ec2 modify-instance-attribute --instance-id INSTANCE_ID --ena-support
```

<p><strong>F. Verify it all went well:</strong></p>

```
$ aws ec2 describe-instances --instance-ids INSTANCE_ID --query "Reservations[].Instances[].EnaSupport" [     true ]
```

<p><strong>G. Switch to t3.micro in the AWS web frontend.</strong></p>

<p><strong>H. Start the instance. The driver should be vif:</strong></p>

```
$  ethtool -i eth0
driver: vif
(...)
```

<p>Ref. <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html#test-enhanced-networking-ena">#1</a><a href="https://stackoverflow.com/questions/54259979/upgrading-from-t2-medium-to-t3-medium">#2</a></p>
