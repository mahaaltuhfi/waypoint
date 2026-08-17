from abc import ABC, abstractmethod
from distance import Distance


class Trail(ABC):
    default_unit = "km"

    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):
        self.trail_id = trail_id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m
        self._difficulty = None
        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        allowed = {"easy", "moderate", "hard", "expert"}
        if difficulty not in allowed:
            raise ValueError(f"difficulty must be one of {allowed}")
        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @classmethod
    def from_dict(cls, data):
        dist = Distance(data["distance_value"], data.get("unit", cls.default_unit))
        return cls(data["id"], data["name"], dist, data["elevation_gain_m"], data["difficulty"])

    @staticmethod
    def is_valid_difficulty(difficulty):
        return difficulty in {"easy", "moderate", "hard", "expert"}

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return False
        return self.trail_id == other.trail_id

    @abstractmethod
    def estimated_time(self):
        pass

    @abstractmethod
    def summary(self):
        pass


class DayHike(Trail):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, pace_kmh=4):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)
        self.pace_kmh = pace_kmh

    def estimated_time(self):
        return self.distance.magnitude / self.pace_kmh

    def summary(self):
        return f"{self.name}: day hike, {self.distance}, ~{self.estimated_time():.1f}h"


class BackpackingRoute(Trail):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, days=2):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)
        self.days = days

    def estimated_time(self):
        return self.days * 8

    def summary(self):
        return f"{self.name}: backpacking route, {self.days} days"


class TrailRun(Trail):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, pace_kmh=10):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)
        self.pace_kmh = pace_kmh

    def estimated_time(self):
        return self.distance.magnitude / self.pace_kmh

    def summary(self):
        return f"{self.name}: trail run, ~{self.estimated_time():.1f}h"


class GuidedDayHike(DayHike):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, guide_name, pace_kmh=3.5):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty, pace_kmh)
        self.guide_name = guide_name

    def summary(self):
        base = super().summary()
        return f"{base} (guided by {self.guide_name})"


class ElevationMixin:
    def grade_percent(self):
        return (self.elevation_gain_m / (self.distance.magnitude * 1000)) * 100


class RatingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ratings = []

    def add_rating(self, stars):
        self.ratings.append(stars)

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0


class RatedDayHike(ElevationMixin, RatingMixin, DayHike):
    pass


class FakeTrail:
    def __init__(self, name):
        self.name = name

    def estimated_time(self):
        return 1.0