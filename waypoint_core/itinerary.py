class Itinerary:
    def __init__(self):
        self.trails = []   # HAS-A: an itinerary is composed of trails, not a type of trail

    def add_trail(self, trail):
        self.trails.append(trail)

    def total_distance(self):
        # sum up all trail distances — assumes they're all in the same unit for simplicity
        total = 0
        for trail in self.trails:
            total += trail.distance.magnitude
        return total


# --- quick test ---
from .trail import Trail
from .distance import Distance


t1 = Trail(1, "Bruce Trail", Distance(12, "km"), 300, "hard")
t2 = Trail(2, "Coastal Loop", Distance(8, "km"), 150, "moderate")
t3 = Trail(3, "Ridge Walk", Distance(5, "km"), 400, "hard")

trip = Itinerary()
trip.add_trail(t1)
trip.add_trail(t2)
trip.add_trail(t3)
print(trip.total_distance())   # should be 25

trip2 = Itinerary()
trip2.add_trail(t1)
print(trip2.total_distance())  # should be 12, proving trip and trip2 are independent