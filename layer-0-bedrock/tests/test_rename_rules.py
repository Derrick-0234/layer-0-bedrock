from pathlib import Path
from src.rename_rules import plan_renames

def test_plan_renames_lowercases_and_underscores(tmp_path: Path):
    base = tmp_path / "base"
    (base / "sub").mkdir(parents=True)

    (base / "My File.txt").write_text("hi", encoding="utf-8")
    (base / "sub" / "Another File.TXT").write_text("ok", encoding="utf-8")
    (base / "clean.txt").write_text("stay", encoding="utf-8")  # should not be in plan

    plans = plan_renames(base)
    got = [(p.old_rel, p.new_rel) for p in plans]

    assert got == [
        ("My File.txt", "my_file.txt"),
        ("sub/Another File.TXT", "sub/another_file.txt"),
    ]
