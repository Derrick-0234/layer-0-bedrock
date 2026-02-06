from src.dedupe import dedupe_by_email


def test_removes_duplicates_case_and_spaces():
    rows = [
        {"name": "A", "email": " ALICE@EXAMPLE.COM ", "age": "14"},
        {"name": "A2", "email": "alice@example.com", "age": "14"},
        {"name": "B", "email": "bob@example.com", "age": "15"},
    ]
    out = dedupe_by_email(rows)
    assert [r["email"] for r in out] == ["alice@example.com", "bob@example.com"]
    assert len(out) == 2


def test_keeps_unique_rows():
    rows = [
        {"name": "A", "email": "a@example.com", "age": "1"},
        {"name": "B", "email": "b@example.com", "age": "2"},
    ]
    out = dedupe_by_email(rows)
    assert len(out) == 2


def test_drops_missing_email():
    rows = [
        {"name": "NoEmail", "email": "", "age": "1"},
        {"name": "NoneEmail", "age": "2"},
        {"name": "Good", "email": "good@example.com", "age": "3"},
    ]
    out = dedupe_by_email(rows)
    assert [r["email"] for r in out] == ["good@example.com"]
