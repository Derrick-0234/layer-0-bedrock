from pathlib import Path
import pytest

from src.script_csv_join import run


def w(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def test_csv_join_good_match_and_no_match(tmp_path: Path):
    left = tmp_path / "left.csv"
    right = tmp_path / "right.csv"
    out = tmp_path / "out.csv"

    w(left, "name,email\nA,a@a.com\nB,b@b.com\n")
    w(right, "email,city\nb@b.com,Taipei\n")

    r = run(left, right, out, left_key="email", right_key="email")
    assert r["left_rows"] == 2
    assert r["matched"] == 1

    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "name,email,city"
    assert lines[1] == "A,a@a.com,"
    assert lines[2] == "B,b@b.com,Taipei"


def test_csv_join_messy_key_normalizes(tmp_path: Path):
    left = tmp_path / "left.csv"
    right = tmp_path / "right.csv"
    out = tmp_path / "out.csv"

    w(left, "name,email\nA, B@B.COM \n")
    w(right, "email,city\nb@b.com,Taipei\n")

    r = run(left, right, out)
    assert r["matched"] == 1


def test_csv_join_bad_missing_key_column(tmp_path: Path):
    left = tmp_path / "left.csv"
    right = tmp_path / "right.csv"
    out = tmp_path / "out.csv"

    w(left, "name,mail\nA,a@a.com\n")
    w(right, "email,city\na@a.com,Taipei\n")

    with pytest.raises(ValueError):
        run(left, right, out, left_key="email", right_key="email")
