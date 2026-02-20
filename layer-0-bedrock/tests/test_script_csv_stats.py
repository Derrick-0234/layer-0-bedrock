from pathlib import Path
import pytest

from src.script_csv_stats import run


def w(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def test_csv_stats_good(tmp_path: Path):
    inp = tmp_path / "in.csv"
    out = tmp_path / "out.csv"

    w(inp, "score\n1\n2\n3\n")

    r = run(inp, out)
    assert r["rows_read"] == 3
    assert r["rows_ignored"] == 0
    assert out.exists()

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "count,min,max,mean"
    assert lines[1].startswith("3,")


def test_csv_stats_messy_ignores_blank_and_nonnumeric(tmp_path: Path):
    inp = tmp_path / "in.csv"
    out = tmp_path / "out.csv"

    w(inp, "score\n1\n\nx\n2\n")

    r = run(inp, out)
    assert r["rows_read"] == 3
    assert r["rows_ignored"] == 1  # blank + nonnumeric ignored


def test_csv_stats_bad_missing_file(tmp_path: Path):
    inp = tmp_path / "missing.csv"
    out = tmp_path / "out.csv"

    with pytest.raises(FileNotFoundError):
        run(inp, out)

