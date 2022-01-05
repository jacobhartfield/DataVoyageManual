# Usage notes for NightRoute Atlas

## Quick start
1. Create a virtual environment and install `PyYAML` if you want to load the curated YAML.
2. Run `python -m scripts.atlas_cli --data data` from the project root.
3. Tailor narrative snippets in `data/narrative_samples.txt` every time you collect a new memory.

## Development checks
- The `tests` folder can be executed with `pytest` or any test runner that can discover the sample file.
- Helpers should focus on adding context rather than massaging the data itself; the atlas is intentionally opinionated about the story flow.
