from __future__ import annotations

import re
from collections import Counter
from typing import List, Tuple

_WORD_RE = re.compile(r"[A-Za-z0-9']+")

def top_words(text: str, k: int = 10) -> Tuple[int, List[Tuple[str, int]]]:
    """
    Returns:
      total_words: total token count
      top: list of (word, count) sorted by count desc then word asc
    """
    tokens = [t.lower() for t in _WORD_RE.findall(text or "")]
    total_words = len(tokens)

    counts = Counter(tokens)
    # Stable deterministic ordering: count desc, word asc
    top = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]
    return total_words, top
