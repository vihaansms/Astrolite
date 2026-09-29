import math
from typing import Tuple

class SkyTarget:
    """Represents an object on the celestial sphere in plain degrees."""

    def __init__(self, name: str, right_ascension: float, declination: float):
        self.name = name
        self.right_ascension = float(right_ascension)
        self.declination = float(declination)

    @property
    def hours_minutes_seconds(self) -> Tuple[int, int, float]:
        """Convert right ascension degrees to standard 24h astronomical clock."""
        total_hours = (self.right_ascension / 360.0) * 24.0
        hours = int(total_hours)
        minutes_total = (total_hours - hours) * 60.0
        minutes = int(minutes_total)
        seconds = (minutes_total - minutes) * 60.0
        return hours, minutes, round(seconds, 2)

    def angular_distance_to(self, other: 'SkyTarget') -> float:
        """Calculates angular separation across the sky in degrees."""
        ra1, dec1 = math.radians(self.right_ascension), math.radians(self.declination)
        ra2, dec2 = math.radians(other.right_ascension), math.radians(other.declination)

        cos_distance = (
            math.sin(dec1) * math.sin(dec2) +
            math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2)
        )
        cos_distance = max(-1.0, min(1.0, cos_distance))
        return math.degrees(math.acos(cos_distance))

    def __repr__(self) -> str:
        h, m, s = self.hours_minutes_seconds
        return f"SkyTarget('{self.name}', RA: {h}h {m}m {s}s, Dec: {self.declination}°)"