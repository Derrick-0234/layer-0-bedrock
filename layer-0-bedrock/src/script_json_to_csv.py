import argparse
import csv
import json
import logging
from pathlib import Path
from typing import Any

from src.json_flatten import clean_json_rows

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert JSON to CSV (clean rows).")
    p.add_argument("--input", required=True, help="Path to input JSON file (list of objects)")
    p.add_argument("--output", required=True, help="Path to output CSV file")
    p.add_argument(
        "--fields",
        default="",
        help="Comma-separated CSV columns. If empty, use sorted union of keys.",
    )
    return p.parse_args()


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def infer_fields(rows: list[dict]) -> list[str]:
    keys: set[str] = set()
    for r in rows:
        if isinstance(r, dict):
            keys.update(r.keys())
    return sorted(keys)


def run(input_path: Path, output_path: Path, fields: list[str] | None = None) -> dict:
    logger.info("start tool=json_to_csv input=%s", input_path)

    raw = load_json(input_path)
    if not isinstance(raw, list):
        raise ValueError("Input JSON must be a list of objects")

    cleaned = clean_json_rows(raw)

    if fields is None or len(fields) == 0:
        fields = infer_fields(cleaned)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(cleaned)

    dropped = max(0, len(raw) - len(cleaned))
    logger.info(
        "summary rows_in=%d rows_out=%d dropped=%d output=%s",
        len(raw),
        len(cleaned),
        dropped,
        output_path,
    )
    if dropped > 0:
        logger.warning("warnings dropped_rows=%d", dropped)

    return {"rows_in": len(raw), "rows_out": len(cleaned), "dropped": dropped, "output": str(output_path)}


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Missing input file: {input_path}")

    fields = [s.strip() for s in args.fields.split(",") if s.strip()] if args.fields else []
    run(input_path, output_path, fields)


if __name__ == "__main__":
    main()
