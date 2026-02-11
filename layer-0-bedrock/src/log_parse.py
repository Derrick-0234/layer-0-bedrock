from __future__ import annotations

from dataclasses import dataclass
from typing import List
import re

LINE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.*)$")

@dataclass(frozen=True)
class LogRow:
    ts: str
    level: str
    message: str

def parse_log(text: str) -> List[LogRow]:
    rows: List[LogRow] = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        m = LINE_RE.match(line)
        if not m:
            continue
        ts, level, msg = m.group(1), m.group(2), m.group(3).strip()
        rows.append(LogRow(ts=ts, level=level, message=msg))
    return rows
