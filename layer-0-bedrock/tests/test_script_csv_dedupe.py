from pathlib import Path
import pytest

from src.script_csv_dedupe import run


def write_text(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def test_csv_dedupe_good(tmp_path: Path):
    inp = tmp_path / "in.csv"
    out = tmp_path / "out.csv"

    write_text(
        inp,
        "name,email\n"
        "A,a@a.com\n"
        "B,b@b.com\n"
        "A2,a@a.com\n",
    )

    r = run(inp, out, key="email")

    assert r["rows_in"] == 3
    assert r["rows_out"] == 2
    assert r["duplicates"] == 1

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "name,email"
    assert lines[1] == "A,a@a.com"
    assert lines[2] == "B,b@b.com"


def test_csv_dedupe_messy_normalizes_email(tmp_path: Path):
    inp = tmp_path / "in.csv"
    out = tmp_path / "out.csv"

    write_text(
        inp,
        "name,email\n"
        "A, A@A.COM \n"
        "B,a@a.com\n",
    )

    r = run(inp, out, key="email")

    assert r["rows_out"] == 1
    assert r["duplicates"] == 1


def test_csv_dedupe_bad_missing_key_column(tmp_path: Path):
    inp = tmp_path / "in.csv"
    out = tmp_path / "out.csv"

    write_text(inp, "name,mail\nA,a@a.com\n")

    with pytest.raises(ValueError):
        run(inp, out, key="email")
