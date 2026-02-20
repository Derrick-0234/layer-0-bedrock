import json
from pathlib import Path

from layer_1_eval.run_eval import run


def test_eval_runner_deterministic(tmp_path: Path):
    cases = tmp_path / "cases.json"
    out1 = tmp_path / "out1.json"
    out2 = tmp_path / "out2.json"

    cases.write_text(
        json.dumps(
            [
                {"id": "b", "question": "What is RAG?", "expected_contains": ["looks up"]},
                {"id": "a", "question": "List the 3 parts of RAG.", "expected_contains": ["Docs"]},
            ]
        ),
        encoding="utf-8",
    )

    r1 = run(cases, out1)
    r2 = run(cases, out2)

    assert r1["results"][0]["id"] == "a"  # sorted by id
    assert json.loads(out1.read_text(encoding="utf-8"))["results"] == json.loads(out2.read_text(encoding="utf-8"))["results"]
