import csv
import logging
from pathlib import Path

from src.stats import summarize_scores

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)


def main():
    input_path = Path("data/stats_input.csv")
    output_path = Path("data/stats_output.csv")

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    summary = summarize_scores(rows)

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["count", "min", "max", "mean"])
        writer.writeheader()
        writer.writerow(summary)

    # counts (best-effort)
    rows_read = len(rows)
    try:
        valid_count = int(summary.get("count", 0) or 0)
    except (ValueError, TypeError):
        valid_count = 0
    rows_ignored = max(rows_read - valid_count, 0)
    rows_written = 1  # one summary row

    log.info("input=%s", input_path)
    log.info("output=%s", output_path)
    log.info("rows_read=%d", rows_read)
    log.info("rows_ignored=%d", rows_ignored)
    log.info("rows_written=%d", rows_written)


if __name__ == "__main__":
    main()
