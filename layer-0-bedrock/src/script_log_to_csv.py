from __future__ import annotations

import csv
import logging
from pathlib import Path

from src.log_parse import parse_log

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

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

    log.info("input=%s", INPUT_PATH)
    log.info("output=%s", OUTPUT_PATH)
    log.info("rows_written=%d", len(rows))

if __name__ == "__main__":
    main()
