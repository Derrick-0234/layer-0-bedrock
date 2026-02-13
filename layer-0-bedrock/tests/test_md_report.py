from pathlib import Path
from src.md_report import csv_to_markdown_report

def test_csv_to_markdown_report_contains_expected_sections(tmp_path: Path):
    csv_path = tmp_path / "x.csv"
    csv_path.write_text("name,score\nalice,10\nbob,20\n", encoding="utf-8")

    md = csv_to_markdown_report(csv_path, title="Test Report", max_rows=20)

    assert "# Test Report" in md
    assert "- Rows: 2" in md
    assert "## Preview" in md
    assert "| name | score |" in md
    assert "| alice | 10 |" in md
    assert "| bob | 20 |" in md
