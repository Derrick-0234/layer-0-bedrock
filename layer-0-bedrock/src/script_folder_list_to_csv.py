from __future__ import annotations

import csv
from pathlib import Path

from src.folder_list import list_files

DATA_DIR = Path("data")
INPUT_DIR = DATA_DIR / "sample_folder"
OUTPUT_PATH = DATA_DIR / "folder_list.csv"

def main() -> None:
    rows = list_files(INPUT_DIR)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["path", "size_bytes"])
        for r in rows:
            w.writerow([r.path, r.size_bytes])

    print(f"Done. listed {len(rows)} files → {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
