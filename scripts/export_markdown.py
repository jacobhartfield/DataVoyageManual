"""Utility to snapshot atlas output into markdown."""

from pathlib import Path
from typing import Optional

from scripts.atlas_cli import build_atlas


def export_story(data: Path, destination: Path) -> None:
    atlas = build_atlas(data)
    summary = atlas.format_story()

    content = """# NightRoute Atlas Snapshot\n\nGenerated story:\n\n```
"""
    content += summary + "\n```
"
    destination.write_text(content)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Emit the atlas story as markdown.")
    parser.add_argument("--data", type=Path, default=Path("data"), help="Location of the data folder")
    parser.add_argument("--dest", type=Path, default=Path("notes/story.md"), help="Where to write the markdown")
    args = parser.parse_args()

    args.dest.parent.mkdir(parents=True, exist_ok=True)
    export_story(args.data, args.dest)
    print(f"Story stamped at {args.dest}")


if __name__ == "__main__":
    main()
