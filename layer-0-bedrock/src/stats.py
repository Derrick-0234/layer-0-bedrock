def summarize_scores(rows):
    """
    Input: list[dict] with a "score" field
    Output: dict with count, min, max, mean
    """
    scores = []
    for row in rows:
        raw = (row.get("score") or "").strip()
        if not raw:
            continue
        try:
            scores.append(float(raw))
        except ValueError:
            continue

    if not scores:
        return {"count": 0, "min": "", "max": "", "mean": ""}

    return {
        "count": len(scores),
        "min": min(scores),
        "max": max(scores),
        "mean": sum(scores) / len(scores),
    }
