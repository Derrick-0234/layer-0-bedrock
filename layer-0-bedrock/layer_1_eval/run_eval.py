import argparse
import json
from pathlib import Path
from datetime import datetime, timezone


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run a tiny eval pack and write results.json (skeleton).")
    p.add_argument("--cases", required=True, help="Path to cases JSON")
    p.add_argument("--output", required=True, help="Path to results JSON")
    return p.parse_args()


def simple_model(question: str) -> str:
    # Placeholder: deterministic stub. Replace later with real assistant call.
    q = question.lower()
    if "what is rag" in q:
        return "RAG looks up company docs first, then answers."
    if "3 parts" in q:
        return "Docs, Search, Answer."
    if "failure" in q:
        return "Wrong doc and hallucination."
    return "Unknown."


def run(cases_path: Path, output_path: Path) -> dict:
    cases = json.loads(cases_path.read_text(encoding="utf-8"))

    results = []
    passed = 0

    for c in cases:
        ans = simple_model(c["question"])
        exp = c.get("expected_contains", [])
        ok = all(x.lower() in ans.lower() for x in exp)

        results.append(
            {
                "id": c["id"],
                "question": c["question"],
                "answer": ans,
                "pass": ok,
                "missing": [x for x in exp if x.lower() not in ans.lower()],
                "tags": c.get("tags", []),
            }
        )
        passed += 1 if ok else 0

    # deterministic ordering
    results = sorted(results, key=lambda r: r["id"])

    out = {
        "meta": {
            "cases": len(results),
            "passed": passed,
            "failed": len(results) - passed,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
        "results": results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def main() -> None:
    args = parse_args()
    run(Path(args.cases), Path(args.output))


if __name__ == "__main__":
    main()
