import json
from pathlib import Path

import pytest

from src.script_json_to_csv import run


def test_json_to_csv_good(tmp_path: Path):
    inp = tmp_path / "in.json"
    out = tmp_path / "out.csv"
    inp.write_text(json.dumps([{"name": "A", "email": "a@a.com", "age": 10}]), encoding="utf-8")

    result = run(inp, out)

    assert result["rows_in"] == 1
    assert result["rows_out"] == 1
    assert out.exists()

    header = out.read_text(encoding="utf-8").splitlines()[0]
    assert "name" in header and "email" in header


def test_json_to_csv_messy_extra_keys(tmp_path: Path):
    inp = tmp_path / "in.json"
    out = tmp_path / "out.csv"
    inp.write_text(json.dumps([{"name": "A", "email": "a@a.com", "extra": "x"}]), encoding="utf-8")

    run(inp, out)

    header = out.read_text(encoding="utf-8").splitlines()[0]
    assert header == "age,email,name"
    assert "extra" not in header


def test_json_to_csv_bad_not_list(tmp_path: Path):
    inp = tmp_path / "in.json"
    out = tmp_path / "out.csv"
    inp.write_text(json.dumps({"name": "A"}), encoding="utf-8")

    with pytest.raises(ValueError):
        run(inp, out)
