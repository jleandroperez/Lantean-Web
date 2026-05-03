---
title: "Installing a Webserver on AWS EC2"
date: 2013-04-01T23:31:17+00:00
slug: "webserver-on-ec2"
categories:
  - "Offtopic"
---

I've recently lantean.co to AWS EC2. Amazon offers a free EC2 instance for a year.... so i decided to give it a shot.

The main reason i had to migrate to a self managed hosting is simple. Shared Hostings don't allow you to fine tune several settings, such as the PHP Memory, and you might event not be able to login using ssh. What did i need to do?. It's simple... let's see...

<h3>&nbsp;</h3>

<h3><span style="font-size: 1.17em;">Setting up the Environment</span></h3>

1. Signup at [Amazon Web Services](http://aws.amazon.com). You'll need a credit card.
2. Create a new EC2 instance. Select 'Micro' as the type.
3. Select the Amazon AMI. (I don't trust 3rd party images!).
4. Follow the wizard, and generate the SSH private / public keys.
5. Setup the firewall, so only IP's in your C class can connect through SSH, and everyone can hit the port 80.
6. Connect to your box!
   ```
   ssh -i certificate.pem ec2-user@[elastic-ip]
   ```
7. Setup a password for your root user
   ```
   su passwd
   ```
8. Install Apache
   ```
   yum install httpd
   service httpd start
   chkconfig httpd on
   ```
9. Install PHP
   ```
   yum instlal php php-mysql
   ```
10. Install mySQL
    ```
    yum install mysql-server
    service mysqld start
    chkconfig mysqld on
    ```
11. Secure mySQL
    ```
    mysql_secure_installation
    ```
12. Install APC
    ```
    yum install php-pecl-alc
    ```

&nbsp;

<h3>Setting up Apache</h3>

Assuming we're not gonna host just a single website, but a couple of them... we're gonna need to setup Virtual Hosts. With VirtualHosts you can serve as many domains as you need, using a single apache installation. Steps!

1. Log into your instance and type... (replace domain.com with your own domain):
   ```
   su
   mkdir -p /var/www/domain.com/public_html
   mkdir /etc/httpd/conf.d/domain.com.conf
   nano /etc/httpd/conf.d/domain.com.conf/httpd.conf
   Add the following lines:
   ServerAdmin your-mail@domain.com
   DocumentRoot /var/www/domain.com/public_html
   ServerName www.domain.com
   ServerAlias *.domain.com
   ErrorLog /var/www/domain.com/error.log
   CustomLog /var/www/domain.com/requests.log combined
   ```
2. Enable htaccess in your virtual hosts:
   ```
   nano /etc/httpd/conf/httpd.conf
   AllowOverride All
   ```
3. Enable logrotate:
   ```
   nano /etc/logrotate.conf
   Add the following lines:
   /var/log/httpd/*log
   /var/www/*/*log
   {
   size 5M
   missingok
   notifempty
   sharedscripts
   delaycompress
   postrotate
   /sbin/service httpd reload > /dev/null 2>/dev/null || true
   endscript
   }
   ```

&nbsp;

<h3>Setting up mySQL</h3>

At last!. Let's see how to create a mySQL database, add a new user, and how to import your mySQL dump, using nothing but bash.

1. Create a new database and a new user
   ```
   mysql -u root -p << You will be asked for your mySQL root-password!
   create database wordpress;
   create user 'wordpress'@'localhost' identified by 'password';
   grant all privileges on wordpress.* to wordpress@localhost;
   flush privileges;
   ```
2. Import a database dump
   ```
   mysql -p -u wordpress wordpress < database_dump.sql
   ```

&nbsp;
I hope you found this short guide helpful!