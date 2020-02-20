# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    variable = "lat", "lon"
    def function(self):


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint:  
      
    attr1 = "name"
    attr2 = "lat"
    attr3 = "lon"
    

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache: 
    attr1 = "name"
    attr2 = "difficulty"
    attr3 = "size"
    attr4 = "lat"
    attr5 = "lon"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = ["Catacombs", 41.70505, -121.51521]

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = "Newberry Views", 1.5, 2, 44.052137, -121.41556

# Print it--also make this print more nicely
print(geocache)
