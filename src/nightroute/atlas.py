"""Core logic for shaping a personal night voyage atlas."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ObservationPoint:
    """A memory of a brief stop during a quiet observation run."""

    name: str
    city: str
    notes: Optional[str] = None
    brightness: Optional[int] = None


@dataclass
class NightRouteAtlas:
    """Stateful helper that stitches together observation notes."""

    points: List[ObservationPoint] = field(default_factory=list)

    def add_point(self, point: ObservationPoint) -> None:
        """Add another point to the atlas."""
        self.points.append(point)

    def latest_point(self) -> Optional[ObservationPoint]:
        """Return the most recent observation if there is one."""
        if not self.points:
            return None
        return self.points[-1]

    def format_story(self) -> str:
        """Render a short itinerary summary."""
        if not self.points:
            return "No points logged yet."
        pieces = []
        for idx, point in enumerate(self.points, start=1):
            brightness = f" (brightness {point.brightness})" if point.brightness is not None else ""
            pieces.append(f"{idx}. {point.name} in {point.city}{brightness}")
        return "\n".join(pieces)
