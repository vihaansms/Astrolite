from __future__ import annotations

class Distance:
    """Represents a spatial length with instant English conversions."""

    def __init__(self, meters: float):
        self._meters = float(meters)

    @classmethod
    def from_meters(cls, value: float) -> Distance:
        return cls(value)

    @classmethod
    def from_km(cls, value: float) -> Distance:
        return cls(value * 1_000.0)

    @classmethod
    def from_au(cls, value: float) -> Distance:
        return cls(value * 149_597_870_700.0)

    @classmethod
    def from_light_years(cls, value: float) -> Distance:
        return cls(value * 9.460730472e15)

    @property
    def meters(self) -> float:
        return self._meters

    @property
    def kilometers(self) -> float:
        return self._meters / 1_000.0

    @property
    def au(self) -> float:
        return self._meters / 149_597_870_700.0

    @property
    def light_years(self) -> float:
        return self._meters / 9.460730472e15

    def light_travel_time_seconds(self) -> float:
        """How long it takes light to traverse this distance."""
        return self._meters / 299_792_458.0

    def __repr__(self) -> str:
        if self._meters >= 9.46e15:
            return f"{self.light_years:.2f} ly"
        if self._meters >= 1.49e11:
            return f"{self.au:.2f} AU"
        if self._meters >= 1_000:
            return f"{self.kilometers:.2f} km"
        return f"{self._meters:.2f} m"