import csv
from pathlib import Path

from src.join import left_join_by_email


def main():
    left_path = Path("data/join_left.csv")
    right_path = Path("data/join_right.csv")
    out_path = Path("data/join_output.csv")

    with left_path.open(newline="", encoding="utf-8") as f:
        left_rows = list(csv.DictReader(f))

    with right_path.open(newline="", encoding="utf-8") as f:
        right_rows = list(csv.DictReader(f))

    merged_rows, right_fields = left_join_by_email(left_rows, right_rows)

    # Output columns = left columns + right-only columns
    left_fields = list(left_rows[0].keys()) if left_rows else ["name", "email"]
    fieldnames = left_fields + [k for k in right_fields if k not in left_fields]

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(merged_rows)

    print("Done. Wrote", len(merged_rows), "rows to", out_path)


if __name__ == "__main__":
    main()
