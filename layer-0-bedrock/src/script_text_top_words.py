from __future__ import annotations

import csv
from pathlib import Path

from src.text_stats import top_words

DATA_DIR = Path("data")
INPUT_PATH = DATA_DIR / "text_input.txt"
OUTPUT_PATH = DATA_DIR / "top_words.csv"

def main() -> None:
    text = INPUT_PATH.read_text(encoding="utf-8")
    total, top = top_words(text, k=20)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["word", "count"])
        w.writerows(top)

    print(f"Done. total_words={total}. wrote {len(top)} rows to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
