"""Tiny CLI that ties the atlas and raw data into a narrative."""

import argparse
import json
import random
from pathlib import Path
from typing import List

from nightroute import NightRouteAtlas, ObservationPoint


def _read_sample_texts(path: Path) -> List[str]:
    try:
        return [line.strip() for line in path.read_text().splitlines() if line.strip()]
    except FileNotFoundError:
        return []


def _read_cities(path: Path) -> List[dict]:
    try:
        import yaml
    except ImportError:
        raise RuntimeError("PyYAML is required to read city records")

    textual = yaml.safe_load(path.read_text())
    if not isinstance(textual, list):
        return []
    return [entry for entry in textual if isinstance(entry, dict)]


def build_atlas(data_root: Path) -> NightRouteAtlas:
    atlas = NightRouteAtlas()
    cities = _read_cities(data_root / "cities.yaml")
    samples = _read_sample_texts(data_root / "narrative_samples.txt")

    for city in cities:
        point = ObservationPoint(
            name=city.get("notable_spots", ["untitled hush"])[0],
            city=city.get("name", "Unknown"),
            notes=random.choice(samples) if samples else None,
            brightness=random.randint(1, 10) if cities else None,
        )
        atlas.add_point(point)
    return atlas


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a short NightRoute Atlas summary.")
    parser.add_argument("--data", type=Path, default=Path("data"), help="Where to read the city files")
    parser.add_argument("--json", action="store_true", help="Write output as JSON")
    args = parser.parse_args()

    atlas = build_atlas(args.data)
    story = atlas.format_story()

    if args.json:
        payload = {
            "atlas": story,
            "length": len(atlas.points),
            "latest": atlas.latest_point().city if atlas.latest_point() else None,
        }
        print(json.dumps(payload, indent=2))
    else:
        print(story)


if __name__ == "__main__":
    main()
