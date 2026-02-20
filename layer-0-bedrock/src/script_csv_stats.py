import argparse
import logging
from pathlib import Path

from src.io_utils import read_csv_dicts, write_csv_dicts
from src.stats import summarize_scores

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compute stats summary from a CSV.")
    p.add_argument("--input", required=True, help="Path to input CSV")
    p.add_argument("--output", required=True, help="Path to output CSV (one summary row)")
    return p.parse_args()


def run(input_path: Path, output_path: Path) -> dict:
    logger.info("start tool=csv_stats input=%s", input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Missing input file: {input_path}")

    rows = read_csv_dicts(input_path)
    summary = summarize_scores(rows)

    # Deterministic columns/order
    fieldnames = ["count", "min", "max", "mean"]
    write_csv_dicts(output_path, [summary], fieldnames=fieldnames)

    rows_read = len(rows)
    try:
        valid_count = int(summary.get("count", 0) or 0)
    except (ValueError, TypeError):
        valid_count = 0

    rows_ignored = max(rows_read - valid_count, 0)
    rows_written = 1  # summary row

    logger.info(
        "summary rows_read=%d rows_ignored=%d rows_written=%d output=%s",
        rows_read,
        rows_ignored,
        rows_written,
        output_path,
    )
    if rows_ignored > 0:
        logger.warning("warnings rows_ignored=%d", rows_ignored)

    return {
        "rows_read": rows_read,
        "rows_ignored": rows_ignored,
        "rows_written": rows_written,
        "output": str(output_path),
    }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    run(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
