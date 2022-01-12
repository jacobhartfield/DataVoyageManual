# NightRoute Atlas

NightRoute Atlas is a solo experiment in building a lightweight data voyage assistant for documenting, analyzing, and iterating on nighttime observation journeys.

## Why this project
- Personal projects feel safer when they have a story, so this tool tracks the curiosity-driven exploration of quiet hours.
- The goal is to stitch together small datasets about city lights, transit availability, and narrative snippets into a coherent nightly log.

## Strategy
1. Gather city metrics, scenic points, and handy automation for generating travel-ready narratives.
2. Keep everything scriptable and easy to evolve with new data sources.
3. Treat every commit as a progress note in the diary of an amateur urban explorer.

## Next steps
- Draft the CLI scaffold for importing and tagging data points.
- Add helper modules that can generate context-aware summaries.
- Keep documenting the thought process so the project feels lived-in.

## What is already here
- A minimal atlas object that tracks a series of points and can format them into short entries.
- Sample data that represents the cities and narrative snippets gathered during a run.
- A CLI script that ties the data and atlas together, plus tests to confirm the story builder.

## Roadmap
1. Add a small scheduler that recommends evenings based on brightness and transit pace.
2. Introduce a notebook export that can be copied into a travel log.
3. Bake in some safety checks so the tool remains a silent companion rather than a mission control system.
