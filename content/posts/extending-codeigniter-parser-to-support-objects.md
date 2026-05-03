---
title: "Extending CodeIgniter Parser to support Objects"
date: 2013-02-01T19:46:30+00:00
slug: "extending-codeigniter-parser-to-support-objects"
categories:
  - "OSX"
---

<a href="/wp-content/uploads/2013/02/code-igniter.png"><img class="alignleft size-thumbnail wp-image-799" style="margin-left: 10px; margin-right: 10px;" title="CodeIgniter" alt="CodeIgniter" src="/wp-content/uploads/2013/02/code-igniter.png" width="150" height="150" /></a>I really like codeIgniter, since it's super lightweight, and its learning curve is super small. You can get to build a whole website within just a couple days, even with database support.

I've written myself a e-commerce website in just two weeks, without having previous knowledge on the technology. Now, let's get to business.

What happens when you're writing a view (php based), and you need to display a variable?. Well, you've got, essentially, two options. To begin with, you can simply invoke the php 'echo' routine, by doing something like this:

```
<?php echo $variable; >
```

<strong></strong>Now, if you wanna keep your code really clean, you can rely on <a href="http://ellislab.com/codeigniter/user-guide/libraries/parser.html">CodeIgniter built in parser</a>. How do you implement it?... super simple...:

<h5><strong>

1. Initialize the Parser Library:</strong></h5>
```
$this->load->library('parser');
```

<h5><strong>2. Replace the '&lt;?php echo $blog_title; ?&gt;' routines with the following syntax:</strong></h5>

```
{blog_title}
```

So far so good. Now... here's something interesting. What happens if you wanna print an object's property? or an object's method?. Well, CodeIgniter doesn't support that scenario. It will only work with strings, and with arrays (of strings). So... i've extended a bit the library, in order to support 'printing object's properties'.

You can <a href="/wp-downloads/sf_parser.php.zip">download right here</a> my extended version of the parser. We won't be analyzing the code i've written. It's not complex, and you're invited to run a diff between the original, and my patch.

Now... how do we use it?. Simple...

<h5><strong>1. Install the sf_parser library</strong></h5>

You should copy the 'sf_parser.php' file to '/application/libraries/sf_parser.php'. That's it. No more no less. Simplicity is one of the things i love the most about CI framework.

<h5><strong>2. Initialize the sf_parser library</strong></h5>

Instead of initializing the CI's default parser, we're gonna need to load our custom library. We can achieve that by doing the following:

```
$this->load->library('sf_parser');
```

<h5><strong>3. Use the new syntax!</strong></h5>

The goal of this library is to enable you (the user!) to print any object's properties, or getter's results. Which means that... instead of using the following syntax, in your view.php file:

```
<?php echo $blog->get_title();>
```

You can now do something far more elegant... which looks something like this:

```
{blog:get_title}
```

If you found it useful... if you found a bug... or if you've extended it further, i'd love to hear from you!