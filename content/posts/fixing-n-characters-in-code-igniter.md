---
title: "Fixing ñ characters in code-igniter"
date: 2013-01-09T18:36:48+00:00
slug: "fixing-n-characters-in-code-igniter"
categories:
  - "HTML5"
---

It seems this is one of the oldest issues of PHP develoment, right?. I've developed a PHP website, based on codeigniter framework (and a mysql database), and i ran into a lot of problems with the ñ, not showing up well in google.

Here's what i've done to fix this problem:

1. Set the database collation / columns to utf8_general_ci (by means of phpmyadmin).
2. In codeigniter's 'config.php' file.

    ```
    $config['charset'] = 'UTF-8';
    ```

3. In codeigniter's 'database.php':

    ```
    $db['default']['char_set'] = 'utf8';
    $db['default']['dbcollat'] = 'utf8_general_ci';
    ```

4. In the 'general' html-rendering, before anything else gets echo'ed (beware, i'm using HTML5.. HTML4 is different):

    ```
    <meta charset="UTF-8">
    ```

5. And finally... in my .htaccess file:

    ```
    AddDefaultCharset UTF-8
    ```

I hope this helps. I've spent many hours reading... testing... and a couple days waiting for Google's update!.