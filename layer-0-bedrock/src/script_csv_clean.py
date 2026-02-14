import argparse
import csv
import logging
from pathlib import Path

from src.transform import clean_rows

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Clean a CSV of name/email rows.")
    p.add_argument("--input", default="data/input.csv", help="Input CSV path")
    p.add_argument("--output", default="data/output.csv", help="Output CSV path")
    return p.parse_args()

def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    cleaned = clean_rows(rows)

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email"])
        writer.writeheader()
        writer.writerows(cleaned)

    dropped = len(rows) - len(cleaned)
    log.info("input=%s", input_path)
    log.info("output=%s", output_path)
    log.info("rows_read=%d", len(rows))
    log.info("rows_dropped=%d", dropped)
    log.info("rows_written=%d", len(cleaned))

if __name__ == "__main__":
    main()
