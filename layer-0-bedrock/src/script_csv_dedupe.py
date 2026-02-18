import argparse
import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Dedupe CSV rows by a key (default: email). Keep first.")
    p.add_argument("--input", required=True, help="Path to input CSV")
    p.add_argument("--output", required=True, help="Path to output CSV")
    p.add_argument("--key", default="email", help="Column name to dedupe on (default: email)")
    return p.parse_args()


def normalize_key(v: str) -> str:
    return v.strip().lower()


def run(input_path: Path, output_path: Path, key: str = "email") -> dict:
    logger.info("start tool=csv_dedupe input=%s", input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Missing input file: {input_path}")

    rows_in = 0
    rows_out = 0
    dropped = 0
    duplicates = 0
    seen: set[str] = set()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row")
        if key not in reader.fieldnames:
            raise ValueError(f"Missing key column: {key}")

        fieldnames = list(reader.fieldnames)

        with output_path.open("w", newline="", encoding="utf-8") as out_f:
            writer = csv.DictWriter(out_f, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                rows_in += 1
                raw = row.get(key, "")
                k = normalize_key(raw)

                if k == "" or "@" not in k:
                    dropped += 1
                    continue

                if k in seen:
                    duplicates += 1
                    continue

                seen.add(k)
                writer.writerow(row)
                rows_out += 1

    logger.info(
        "summary rows_in=%d rows_out=%d dropped=%d duplicates=%d output=%s",
        rows_in,
        rows_out,
        dropped,
        duplicates,
        output_path,
    )
    if dropped > 0 or duplicates > 0:
        logger.warning("warnings dropped=%d duplicates=%d", dropped, duplicates)

    return {
        "rows_in": rows_in,
        "rows_out": rows_out,
        "dropped": dropped,
        "duplicates": duplicates,
        "output": str(output_path),
    }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    run(Path(args.input), Path(args.output), key=args.key)


if __name__ == "__main__":
    main()

