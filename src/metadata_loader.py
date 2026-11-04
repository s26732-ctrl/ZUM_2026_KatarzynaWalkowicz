
"""
Instructions for downloading and loading dataset metadata
"""

import json
import requests
from pathlib import Path


METADATA_URL = (
    "https://lilawildlife.blob.core.windows.net/lila-wildlife/"
    "biome-health-project-maasai-mara-2018/"
    "biome-health-project-maasai-mara-2018.json"
)

METADATA_FILENAME = "biome.json"


def download_metadata(metadata_dir):
    """Download metadata if it does not already exist."""

    metadata_dir = Path(metadata_dir)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    metadata_path = metadata_dir / METADATA_FILENAME

    if not metadata_path.exists():
        response = requests.get(METADATA_URL, timeout=60)
        response.raise_for_status()
        metadata_path.write_bytes(response.content)
        print("Metadata downloaded successfully")
    else:
        print("Metadata already exists")

    return metadata_path


def load_metadata(metadata_path):
    """Load metadata from a JSON file."""

    with open(metadata_path, "r", encoding="utf-8") as file:
        return json.load(file)
