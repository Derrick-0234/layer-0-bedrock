import csv
from pathlib import Path

from src.stats import summarize_scores


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

    print("Done. Wrote summary to", output_path)


if __name__ == "__main__":
    main()
