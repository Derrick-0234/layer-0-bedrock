import csv
from pathlib import Path

from src.transform import clean_rows


def main():
    input_path = Path("data/input.csv")
    output_path = Path("data/output.csv")

    # Make sure the output folder exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Read input CSV into a list of dicts
    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Clean rows
    cleaned = clean_rows(rows)

    # Write output CSV
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email"])
        writer.writeheader()
        writer.writerows(cleaned)

    print("Done. Wrote", len(cleaned), "rows to", output_path)


if __name__ == "__main__":
    main()
