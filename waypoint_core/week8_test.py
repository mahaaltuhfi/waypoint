from distance import Distance
from trail import DayHike, BackpackingRoute, TrailRun, GuidedDayHike, RatedDayHike, FakeTrail, Trail

d1 = Distance(3, "km")
d2 = Distance(2, "km")
print(d1 + d2)
print(Distance(3, "km") == Distance(3, "km"))
print(sorted([Distance(5, "km"), Distance(1, "km"), Distance(3, "km")], key=lambda d: d.magnitude))

mixed = [
    DayHike(1, "Ridge Walk", Distance(8, "km"), 200, "moderate"),
    BackpackingRoute(2, "Coastal Trek", Distance(40, "km"), 900, "hard", days=3),
    TrailRun(3, "Sprint Loop", Distance(5, "km"), 50, "easy"),
    GuidedDayHike(4, "Alpine Intro", Distance(6, "km"), 400, "moderate", guide_name="Sam"),
    FakeTrail("Not a real Trail subclass"),
]
for item in mixed:
    print(item.estimated_time())

print(mixed[3].summary())

try:
    Trail(1, "x", Distance(1, "km"), 1, "easy")
except TypeError as e:
    print("Correctly blocked:", e)

rated = RatedDayHike(5, "Lookout Loop", Distance(4, "km"), 100, "easy")
rated.add_rating(5)
rated.add_rating(3)
print(rated.average_rating())
print(rated.grade_percent())
print(RatedDayHike.__mro__)