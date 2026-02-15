from __future__ import annotations

import argparse
from pathlib import Path

from src.md_report import csv_to_markdown_report

DATA_DIR = Path("data")
DEFAULT_INPUT_CSV = DATA_DIR / "folder_list.csv"
DEFAULT_OUTPUT_MD = DATA_DIR / "report.md"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a deterministic Markdown report from a CSV.")
    p.add_argument("--input", default=str(DEFAULT_INPUT_CSV), help="Input CSV path")
    p.add_argument("--output", default=str(DEFAULT_OUTPUT_MD), help="Output Markdown path")
    p.add_argument("--title", default="Folder List Report", help="Report title")
    p.add_argument("--max-rows", type=int, default=30, help="Max preview rows")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    input_csv = Path(args.input)
    output_md = Path(args.output)

    output_md.parent.mkdir(parents=True, exist_ok=True)

    md = csv_to_markdown_report(input_csv, title=args.title, max_rows=args.max_rows)
    output_md.write_text(md, encoding="utf-8")
    print(f"Done. wrote report → {output_md}")


if __name__ == "__main__":
    main()
