from __future__ import annotations

import csv
from pathlib import Path

from src.rename_rules import plan_renames

DATA_DIR = Path("data")
INPUT_DIR = DATA_DIR / "rename_folder"
OUTPUT_PATH = DATA_DIR / "rename_plan.csv"

def main() -> None:
    plans = plan_renames(INPUT_DIR)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["old_rel", "new_rel"])
        for p in plans:
            w.writerow([p.old_rel, p.new_rel])

    print("DRY RUN (no files renamed). Plan:")
    for p in plans:
        print(f"- {p.old_rel} -> {p.new_rel}")
    print(f"Done. planned {len(plans)} renames → {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
