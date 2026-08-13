from .distance import Distance

class Trail:
    allowed_difficulties = {"easy", "moderate", "hard", "expert"}

    def __init__(self, id, name, distance, elevation_gain_m, difficulty):
        self.id = id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m
        self._difficulty = None
        self.set_difficulty(difficulty)

    def set_difficulty(self, diff):
        if diff not in Trail.allowed_difficulties:
            raise ValueError("Invalid difficulty")
        self._difficulty = diff

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            distance=Distance(data["distance"], data["unit"]),
            elevation_gain_m=data["elevation_gain_m"],
            difficulty=data["difficulty"]
        )

    def __eq__(self, other):
        return self.id == other.id
