import argparse
import logging
from pathlib import Path

from src.io_utils import read_csv_dicts, write_csv_dicts
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

    rows = read_csv_dicts(input_path)
    cleaned = clean_rows(rows)

    write_csv_dicts(output_path, cleaned, fieldnames=["name", "email"])

    dropped = len(rows) - len(cleaned)
    log.info("input=%s", input_path)
    log.info("output=%s", output_path)
    log.info("rows_read=%d", len(rows))
    log.info("rows_dropped=%d", dropped)
    log.info("rows_written=%d", len(cleaned))


if __name__ == "__main__":
    main()
