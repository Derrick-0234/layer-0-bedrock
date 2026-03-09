import csv
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
INPUT = BASE / "sample.csv"
CLEANED = BASE / "cleaned.csv"
REPORT = BASE / "report.md"

def clean_rows(rows):
    out = []
    for row in rows:
        name = row.get("name", "").strip()
        email = row.get("email", "").strip().lower()
        age = row.get("age", "").strip()

        if not name or not email or "@" not in email:
            continue

        out.append({
            "name": name,
            "email": email,
            "age": age,
        })
    return out

def mean(xs):
    return sum(xs) / len(xs)

def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)

def std(xs):
    return math.sqrt(variance(xs))

def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    if not rows:
        raise ValueError("No cleaned rows to write")
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "age"])
        writer.writeheader()
        writer.writerows(rows)

def write_report(path, rows_in, rows_out, ages):
    age_mean = mean(ages) if ages else 0.0
    age_std = std(ages) if ages else 0.0

    text = f"""# Cleaning Report

- rows in: {rows_in}
- rows out: {rows_out}
- dropped: {rows_in - rows_out}
- age mean: {age_mean:.2f}
- age std: {age_std:.2f}
- cleaned csv: {CLEANED.name}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    print(f"start input={INPUT}")
    rows = load_csv(INPUT)
    cleaned = clean_rows(rows)
    write_csv(CLEANED, cleaned)

    ages = [float(r["age"]) for r in cleaned if r["age"]]
    write_report(REPORT, len(rows), len(cleaned), ages)

    print(f"rows_in={len(rows)} rows_out={len(cleaned)} output={REPORT}")
    print("ok")

if __name__ == "__main__":
    main()
