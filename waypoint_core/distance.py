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
