from pathlib import Path
from src.folder_list import list_files

def test_list_files_returns_relative_paths_sorted(tmp_path: Path):
    base = tmp_path / "base"
    (base / "sub").mkdir(parents=True)

    (base / "a.txt").write_text("hello", encoding="utf-8")
    (base / "sub" / "b.txt").write_text("world", encoding="utf-8")

    rows = list_files(base)
    paths = [r.path for r in rows]

    assert paths == ["a.txt", "sub/b.txt"]
    assert rows[0].size_bytes > 0
    assert rows[1].size_bytes > 0
