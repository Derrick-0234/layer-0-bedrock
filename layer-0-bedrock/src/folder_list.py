from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class FileRow:
    path: str          # relative path from base_dir
    size_bytes: int

def list_files(base_dir: Path) -> List[FileRow]:
    """
    List all files under base_dir (recursive), deterministic ordering.
    """
    base_dir = Path(base_dir)
    rows: List[FileRow] = []

    for p in sorted(base_dir.rglob("*")):
        if p.is_file():
            rel = p.relative_to(base_dir).as_posix()
            rows.append(FileRow(path=rel, size_bytes=p.stat().st_size))

    return rows
