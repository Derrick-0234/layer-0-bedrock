from src.transform import clean_rows

def test_clean_rows_filters_bad_rows():
    rows = [{"name": "", "email": "a@b.com"}, {"name": "A", "email": ""}]
    assert clean_rows(rows) == []

def test_clean_rows_trims_and_lowercases():
    rows = [{"name": " Alice ", "email": " ALICE@Example.com "}]
    assert clean_rows(rows) == [{"name": "Alice", "email": "alice@example.com"}]

def test_clean_rows_keeps_valid():
    rows = [{"name": "Bob", "email": "bob@example.com"}]
    assert clean_rows(rows) == [{"name": "Bob", "email": "bob@example.com"}]
