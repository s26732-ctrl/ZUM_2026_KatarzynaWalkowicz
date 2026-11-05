
"""
Download dataset images from LILA.
"""

from pathlib import Path
import requests


IMAGE_BASE_URL = (
    "https://lilawildlife.blob.core.windows.net/lila-wildlife/"
    "biome-health-project-maasai-mara-2018/"
)


def download_images(filenames, images_dir):

    images_dir = Path(images_dir)
    images_dir.mkdir(parents=True, exist_ok=True)

    downloaded = 0
    skipped = 0
    failed = []

    with requests.Session() as session:
        for filename in filenames:
            image_path = images_dir / filename

            if image_path.exists() and image_path.stat().st_size > 0:
                skipped += 1
                continue

            try:
                response = session.get(
                    IMAGE_BASE_URL + filename,
                    timeout=60
                )
                response.raise_for_status()

                image_path.write_bytes(response.content)
                downloaded += 1

            except requests.RequestException:
                failed.append(filename)

    print(f"Downloaded: {downloaded}")
    print(f"Skipped: {skipped}")
    print(f"Failed: {len(failed)}")

    return failed
