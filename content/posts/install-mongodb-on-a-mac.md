---
title: "Install mongoDB on a Mac!"
date: 2013-01-26T11:13:11+00:00
slug: "install-mongodb-on-a-mac"
categories:
  - "OSX"
---

<p style="text-align: center;"><a href="/wp-content/uploads/2013/01/mongo-db.png"><img class="size-full wp-image-756 aligncenter" title="mongoDB on a Mac" alt="mongoDB on a Mac" src="/wp-content/uploads/2013/01/mongo-db.png" width="221" height="103" /></a></p>

MongoDB is a NoSQL database, free of charge. The beauty of mongo relies on its schema-less design... you can add and remove fields, without doing 'alter table'.

Your information gets stored in JSON, which is  seriously interesting, specially if you work with iOS / Android Apps, and the communications layer works in json.

So.. fire up a browser, and head to <a href="http://www.mongodb.org/downloads">this urls</a>. Assuming you're running OSX (like me!), you'd need the mac binary, which is about 60 megabytes.

Preferrably, you'll need to download the 64 bits executable. The 32 bits version can address only databases up to 2 gigabytes.

Once you've got the file, simply double click on it, to get it uncompressed. Assuming that the file is in the downloads folder, let's move it to a more suitable location.

Launch terminal, and type the following:

```
sudo
cd ~/Downloads/
sudo mv mongodb /usr/local/mongodb

```

Mongo stores its databases in the <strong>"/data/db"</strong> directory, so... we'd need to create them:

```
mkdir /data
mkdir /data/db
chmod 777 /data/db

```

Now, let's add a couple symbolic links, so you can launch mongo from anywhere in the system:

```
cd /usr/local/bin
ln /usr/local/mongodb/bin/mongod

```

That's it! you've just installed mongo!. In order to launch the database, you simply need to type the 'mongodb' command.

If you wanna launch a command-line client, type 'mongo', which should connect to the server, right away.