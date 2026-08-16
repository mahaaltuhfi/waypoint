class Distance:
    def __init__(self, magnitude, unit):
        if magnitude < 0:
            raise ValueError("Distance cannot be negative")
        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'")
        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self):
        if self._unit == "km":
            return Distance(self._magnitude * 0.621371, "mi")
        else:
            return Distance(self._magnitude / 0.621371, "km")

    # --- Week 8 operator overloading ---
    def __add__(self, other):
        if self.unit != other.unit:
            raise ValueError("Units must match")
        return Distance(self.magnitude + other.magnitude, self.unit)

    def __eq__(self, other):
        return self.unit == other.unit and self.magnitude == other.magnitude

    def __lt__(self, other):
        if self.unit != other.unit:
            raise ValueError("Units must match")
        return self.magnitude < other.magnitude

    def __repr__(self):
        return f"{self.magnitude:.2f} {self.unit}"