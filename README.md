# Syntax Checklist

A small Python script for practicing safe handling of missing/messy data in lists and dicts — the kind of thing you constantly hit when parsing scraped or API data (e.g. OpenStreetMap/Overpass results).

## What it does

Runs through 6 tasks demonstrating:
1. List indexing
2. Dict access
3. Handling `None` values safely
4. Verifying data with boolean flags
5. Catching missing dict keys with a custom exception
6. Parsing nested dictionaries (dict inside a dict)

## Usage

```bash
uv run main.py
```
## Example output
Task1: Giza
Task3: Here are some places in Egypt:
Khan El-Khalili does not have valid coordinates.
Task5: Checking for missing keys in places:
Missing key in {'name': 'Khan El-Khalili', 'lat': 30.0444, 'type': 'market'}

## Requirements

- Python 3.14+
- uv