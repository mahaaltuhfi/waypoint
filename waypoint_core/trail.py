from abc import ABC, abstractmethod
from waypoint_core.distance import Distance

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
            raise ValueError(f"Difficulty must be one of {allowed}")
        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @classmethod
    def from_dict(cls, data):
        dist = Distance(data["distance_value"], data.get("unit", cls.default_unit))
        return cls(
            data["id"],
            data["name"],
            dist,
            data["elevation_gain_m"],
            data["difficulty"]
        )

    @staticmethod
    def is_valid_difficulty(difficulty):
        return difficulty in {"easy", "moderate", "hard", "expert"}

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return False
        return self.trail_id == other.trail_id

    @abstractmethod
    def estimated_time_hours(self):
        pass


class DayHike(Trail):
    def estimated_time_hours(self):
        base = self.distance.magnitude / 3.0
        climb = self.elevation_gain_m / 600.0
        return base + climb


class BackpackingRoute(Trail):
    def estimated_time_hours(self):
        base = self.distance.magnitude / 2.0
        climb = self.elevation_gain_m / 400.0
        return base + climb


class TrailRun(Trail):
    def estimated_time_hours(self):
        base = self.distance.magnitude / 8.0
        climb = self.elevation_gain_m / 1000.0
        return base + climb


class GuidedDayHike(DayHike):
    def estimated_time_hours(self):
        return super().estimated_time_hours() + 1.0


class RatingMixin:
    def set_rating(self, rating):
        if rating not in {1, 2, 3, 4, 5}:
            raise ValueError("Rating must be 1–5")
        self._rating = rating

    @property
    def rating(self):
        return getattr(self, "_rating", None)


class RatedDayHike(RatingMixin, DayHike):
    pass


class FakeTrail:
    def __init__(self, trail_id):
        self.trail_id = trail_id
