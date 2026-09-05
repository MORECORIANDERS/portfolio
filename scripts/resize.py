"""
Resize photos to max 1600px (long edge), preserve EXIF, and generate photo-meta.json.

Usage:
    python scripts/resize.py
"""

import json
import math
import os
from fractions import Fraction
from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS

PHOTO_DIR = Path(__file__).resolve().parent.parent / "src" / "assets" / "photography"
META_OUT = Path(__file__).resolve().parent.parent / "src" / "data" / "photo-meta.json"
MAX_SIZE = 1600
QUALITY = 82
EXTENSIONS = {".jpg", ".jpeg", ".JPG", ".JPEG"}


def aperture_from_value(val: float) -> str:
    """Convert ApertureValue (APEX) to F-number string."""
    f_number = 2 ** (val / 2)
    # Snap to common F-stop values
    stops = [1.0, 1.4, 2.0, 2.8, 4.0, 5.6, 8.0, 11, 16, 22, 32]
    closest = min(stops, key=lambda x: abs(x - f_number))
    return f"f/{closest}"


def shutter_from_value(val: float) -> str:
    """Convert ExposureTime (seconds) to readable string like '1/200s'."""
    if val >= 1:
        return f"{val:.0f}s"
    denom = round(1 / val)
    return f"1/{denom}s"


def extract_exif(img: Image.Image, filename: str) -> dict:
    """Extract useful EXIF fields from an image."""
    exif_raw = img._getexif()
    if not exif_raw:
        return {}

    tags = {}
    for tag_id, value in exif_raw.items():
        tag_name = TAGS.get(tag_id, tag_id)
        if isinstance(tag_name, str):
            tags[tag_name] = value

    meta = {}

    # Date
    dt = tags.get("DateTimeOriginal", "")
    if dt:
        # "2025:08:05 18:43:27" -> "2025.08"
        parts = dt.split(" ")[0].split(":")
        if len(parts) >= 2:
            meta["date"] = f"{parts[0]}.{parts[1]}"

    # Camera
    make = tags.get("Make", "")
    model = tags.get("Model", "")
    if model:
        # Avoid duplicating make if model already contains it
        if make and make.lower() not in model.lower():
            meta["camera"] = f"{make} {model}"
        else:
            meta["camera"] = model

    # Lens - use LensModel, fallback to simplified info
    lens = tags.get("LensModel", "")
    if lens:
        meta["lens"] = str(lens)

    # Focal length - prefer 35mm equivalent
    focal_35 = tags.get("FocalLengthIn35mmFilm")
    focal = tags.get("FocalLength")
    if focal_35 and focal_35 != 0:
        meta["focal"] = f"{int(focal_35)}mm"
    elif focal:
        focal_val = _ratio_to_float(focal)
        if focal_val:
            meta["focal"] = f"{int(focal_val)}mm"

    # Aperture - from ApertureValue (APEX) or MaxApertureValue
    aperture_val = tags.get("ApertureValue") or tags.get("MaxApertureValue")
    if aperture_val is not None:
        meta["aperture"] = aperture_from_value(float(aperture_val))

    # Shutter speed
    exposure = tags.get("ExposureTime")
    if exposure is not None:
        meta["shutter"] = shutter_from_value(float(exposure))

    # ISO
    iso = tags.get("ISOSpeedRatings") or tags.get("RecommendedExposureIndex")
    if iso is not None:
        meta["iso"] = f"ISO {int(iso)}"

    return meta


def _ratio_to_float(val) -> float | None:
    """Convert EXIF rational/tuple to float."""
    if isinstance(val, tuple) and len(val) == 2:
        return val[0] / val[1] if val[1] else None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def main():
    PHOTO_DIR.mkdir(parents=True, exist_ok=True)
    META_OUT.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(
        f for f in PHOTO_DIR.iterdir()
        if f.suffix in EXTENSIONS
    )

    if not files:
        print("No images found in", PHOTO_DIR)
        return

    meta = {}

    for fpath in files:
        stem = fpath.stem  # e.g. "BS0A9306"
        print(f"Processing {fpath.name}...", end=" ")

        img = Image.open(fpath)
        w, h = img.size

        # Extract EXIF before resizing
        photo_meta = extract_exif(img, fpath.name)
        photo_meta["width"] = w
        photo_meta["height"] = h

        # Resize
        if max(w, h) > MAX_SIZE:
            ratio = MAX_SIZE / max(w, h)
            new_w = int(w * ratio)
            new_h = int(h * ratio)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            print(f"{w}x{h} -> {new_w}x{new_h}", end=" ")

        # Save with EXIF preserved
        exif_data = img.info.get("exif")
        save_kwargs = {"quality": QUALITY, "optimize": True}
        if exif_data:
            save_kwargs["exif"] = exif_data
        img.save(fpath, "JPEG", **save_kwargs)

        new_size = fpath.stat().st_size / 1024
        print(f"({new_size:.0f}KB)")

        meta[stem] = photo_meta

    # Write JSON
    META_OUT.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nDone! {len(files)} images processed.")
    print(f"Metadata written to {META_OUT}")


if __name__ == "__main__":
    main()
