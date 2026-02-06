import csv
from pathlib import Path

from src.dedupe import dedupe_by_email


def main():
    input_path = Path("data/dupe_input.csv")
    output_path = Path("data/dupe_output.csv")

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    cleaned = dedupe_by_email(rows)

    # Keep the same columns as input
    fieldnames = list(rows[0].keys()) if rows else ["name", "email", "age"]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned)

    print("Done. Wrote", len(cleaned), "rows to", output_path)


if __name__ == "__main__":
    main()
