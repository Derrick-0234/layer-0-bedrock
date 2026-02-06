from src.json_flatten import clean_json_rows

def test_keeps_good_row():
    rows = [{"name": "Alice", "email": "alice@example.com", "age": 14}]
    assert clean_json_rows(rows) == [{"name": "Alice", "email": "alice@example.com", "age": 14}]

def test_trims_name_and_lowercases_email():
    rows = [{"name": " Bob ", "email": " BOB@Example.com ", "age": 15}]
    assert clean_json_rows(rows) == [{"name": "Bob", "email": "bob@example.com", "age": 15}]

def test_drops_bad_rows():
    rows = [
        {"name": "", "email": "a@b.com", "age": 1},        # bad: blank name
        {"name": "A", "email": "", "age": 1},             # bad: blank email
        {"name": "A", "email": "not-an-email", "age": 1}, # bad: no @
    ]
    assert clean_json_rows(rows) == []
