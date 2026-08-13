from waypoint_core.distance import Distance
from waypoint_core.trail import Trail
from waypoint_core.itinerary import Itinerary

# Create distances
d1 = Distance(5, "km")
d2 = Distance(7, "km")

# Create trails
t1 = Trail(1, "Forest Trail", d1, 200, "easy")
t2 = Trail(2, "River Trail", d2, 300, "moderate")

# Create itinerary and add trails
trip = Itinerary()
trip.add_trail(t1)
trip.add_trail(t2)

# Should print 12
print("Trip total distance:", trip.total_distance())

# Second itinerary to prove independence
trip2 = Itinerary()
trip2.add_trail(t1)

# Should print 5
print("Trip2 total distance:", trip2.total_distance())
