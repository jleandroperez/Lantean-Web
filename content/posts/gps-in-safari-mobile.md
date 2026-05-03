---
title: "GPS in Safari Mobile"
date: 2012-04-19T10:46:25+00:00
slug: "gps-in-safari-mobile"
categories:
  - "iOS"
---

So... what if you wanna get the GPS position, but within a WebApp's context?. There are several tools, such as PhoneGap, that encapsulate GPS access. But it turns out that there is an extremely easy way to accomplish this task.

Check out this JavaScript snippet... easy, right?

```
navigator.geolocation.getCurrentPosition(foundLocation, noLocation);

function foundLocation(position)
{
  var lat = position.coords.latitude;
  var long = position.coords.longitude;
  alert('Found location: ' + lat + ', ' + long);
}

function noLocation()
{
  alert('Could not find location');
}

```