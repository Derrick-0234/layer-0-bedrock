from __future__ import annotations

import csv
from pathlib import Path

from src.log_parse import parse_log

DATA_DIR = Path("data")
INPUT_PATH = DATA_DIR / "app.log"
OUTPUT_PATH = DATA_DIR / "log_output.csv"

def main() -> None:
    text = INPUT_PATH.read_text(encoding="utf-8")
    rows = parse_log(text)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ts", "level", "message"])
        for r in rows:
            w.writerow([r.ts, r.level, r.message])

    print(f"Done. parsed {len(rows)} rows → {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
