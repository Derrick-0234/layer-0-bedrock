from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Dict, Optional

def _escape_md(text: str) -> str:
    # Keep it simple: escape pipes so tables don't break
    return (text or "").replace("|", "\\|")

def csv_to_markdown_report(
    csv_path: Path,
    title: str = "CSV Report",
    max_rows: int = 20,
) -> str:
    """
    Deterministic Markdown report from a CSV file:
      - title
      - row count
      - columns list
      - preview table (first max_rows rows)
    """
    csv_path = Path(csv_path)
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows: List[Dict[str, str]] = list(reader)

    lines: List[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"- Source: {csv_path.as_posix()}")
    lines.append(f"- Rows: {len(rows)}")
    lines.append(f"- Columns: {', '.join(fieldnames) if fieldnames else '(none)'}")
    lines.append("")
    lines.append("## Preview")
    lines.append("")

    if not fieldnames:
        lines.append("_No columns found._")
        lines.append("")
        return "\n".join(lines)

    preview = rows[:max_rows]

    # Header row
    lines.append("| " + " | ".join(_escape_md(c) for c in fieldnames) + " |")
    lines.append("| " + " | ".join(["---"] * len(fieldnames)) + " |")

    # Data rows
    for r in preview:
        lines.append("| " + " | ".join(_escape_md(r.get(c, "")) for c in fieldnames) + " |")

    lines.append("")
    if len(rows) > max_rows:
        lines.append(f"_Showing first {max_rows} of {len(rows)} rows._")
        lines.append("")

    return "\n".join(lines)
