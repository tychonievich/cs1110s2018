---
title: "Lab 10: Point of Interest"
...


# Activities

## Overview

Your code should

1.  Prompt the user to enter a latitude and longitude
2.  Read a list of locations to find the closest location to the user
3.  Open the user's web browser centered on that location

To test this, you'll need

1.  A list of locations, such as
    
    -   <http://cs1110.cs.virginia.edu/files/arbys.csv>
    -   <http://cs1110.cs.virginia.edu/files/chickfila.csv>
    -   <http://cs1110.cs.virginia.edu/files/fiveguys.csv>
    -   <http://cs1110.cs.virginia.edu/files/wendys.csv>
    
    Each file contains rows with 
    
    -   latitude
    -   longitude
    -   store-name
    -   state
    -   street
    -   city
    -   state-and-postal-code
    -   telephone number

2.  A test location or two.
    Rice hall is (38.0317274, -78.5110432);
    you can find others at [http://www.gps-coordinates.net/](http://www.gps-coordinates.net/).

## Finding a POI (Point of Interest)

You'll need to write code that, given a target latitude and longitude, loops the points of interest in the CSV file and finds the one that is closest to the target location.
To do this, you'll need to create CSV reading code (like we have done in class recently)
and also have a way of computing the distance between two GPS coordinates.
That distance math is complicated because the earth is a spheroid; the following code should work, and you are encouraged to use it as-is:

````python
import math

# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist
````

You can execute this code by calling:

````python
distance = distance_between(user_lat, user_lon, poi_lat, poi_lon)
````

Here, the `user_lat` and `user_lon` are what the user typed in
and `poi_lat` and `poi_lon` are the 0 and 1 columns from the .csv
(remember you can get these after you split the line... look at the examples from class!).

The result `distance` here is the distance in miles.

Loop through the entire file, remembering which POI gave you the shortest distance from the user's coordinates to that POI coordinates.
Save that information in some variables.


## Opening a map

Now let's put it on a map!

We can take the address (which is the combination of columns 4, 5, and 6 from the .csv)
and create a web address object (URL) that Python can use to open your computer's default browser.

````python
# You'll need this at the top of your file
import webbrowser
````

Once you have imported the `webbrowser` library, you'll need to create the proper URL for Google Maps.

Pick one of the following mapping websites:

OpenStreetMap
:   The URL should look like:

    `http://www.openstreetmap.org/search?query=` + the address

Mapquest
:   The URL should look like:

    `http://www.mapquest.com/search/results?query=` + the address

Google Maps
:   The URL should look like:

    `http://maps.google.com/maps?q=` + the address

Bing Maps
:   The URL should look like:

    `http://www.bing.com/maps?q=` + the address


The "the address" field above is created by concatenating columns 4, 5, and 6 from the .csv, replacing all spaces by plus-signs.

Once you have a URL, open it in a browser using

````python
webbrowser.open(url)
````

Give it a shot and see what POI you can find!


## Submission

**At least one partner** should submit one .py file named `poi.py` to Archimedes (the submission system):
[https://archimedes.cs.virginia.edu/cs1110/](https://archimedes.cs.virginia.edu/cs1110/).
Please put **all partners' ids** in comments at the top of the file.
