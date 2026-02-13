from __future__ import annotations

from pathlib import Path

from src.md_report import csv_to_markdown_report

DATA_DIR = Path("data")
INPUT_CSV = DATA_DIR / "folder_list.csv"
OUTPUT_MD = DATA_DIR / "report.md"

def main() -> None:
    md = csv_to_markdown_report(INPUT_CSV, title="Folder List Report", max_rows=30)
    OUTPUT_MD.write_text(md, encoding="utf-8")
    print(f"Done. wrote report → {OUTPUT_MD}")

if __name__ == "__main__":
    main()
