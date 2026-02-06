import json
import csv
from pathlib import Path

from src.json_flatten import clean_json_rows


def main():
    input_path = Path("data/input.json")
    output_path = Path("data/output_json.csv")

    with input_path.open(encoding="utf-8") as f:
        rows = json.load(f)

    cleaned = clean_json_rows(rows)

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "age"])
        writer.writeheader()
        writer.writerows(cleaned)

    print("Done. Wrote", len(cleaned), "rows to", output_path)


if __name__ == "__main__":
    main()
