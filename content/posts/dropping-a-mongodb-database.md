---
title: "Dropping a MongoDB Database"
date: 2013-03-05T23:35:27+00:00
slug: "dropping-a-mongodb-database"
categories:
  - "Offtopic"
---

I'm writing this down, riiight here, because i just got bored of searching this in google everytime i need to run an experiment.
If you need to drop a mongo database, just fire the mongo shell and type:

```
use mydb;
db.dropDatabase();

```

That's it!