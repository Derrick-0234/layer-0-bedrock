from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class RenamePlan:
    old_rel: str
    new_rel: str

def normalize_filename(name: str) -> str:
    """
    Rule:
      - lowercase
      - spaces -> underscores
    """
    return name.strip().lower().replace(" ", "_")

def plan_renames(base_dir: Path) -> List[RenamePlan]:
    """
    Walk all files under base_dir and produce a rename plan.
    Deterministic ordering.
    """
    base_dir = Path(base_dir)
    plans: List[RenamePlan] = []

    for p in sorted(base_dir.rglob("*")):
        if not p.is_file():
            continue

        rel = p.relative_to(base_dir)
        old_name = rel.name
        new_name = normalize_filename(old_name)

        if new_name != old_name:
            new_rel = rel.with_name(new_name)
            plans.append(RenamePlan(old_rel=rel.as_posix(), new_rel=new_rel.as_posix()))

    return plans
