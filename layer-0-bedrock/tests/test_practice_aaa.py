from src.transform import clean_rows


def test_good_row_stays():
    # Arrange
    rows = [{"name": "Alice", "email": "alice@example.com"}]

    # Act
    out = clean_rows(rows)

    # Assert
    assert out == [{"name": "Alice", "email": "alice@example.com"}]


def test_messy_row_gets_cleaned():
    # Arrange
    rows = [{"name": " Alice ", "email": " ALICE@Example.com "}]

    # Act
    out = clean_rows(rows)

    # Assert
    assert out == [{"name": "Alice", "email": "alice@example.com"}]


def test_bad_row_gets_removed():
    # Arrange
    rows = [
        {"name": "", "email": "a@b.com"},
        {"name": "A", "email": ""},
        {"name": "Good", "email": "good@example.com"},
    ]

    # Act
    out = clean_rows(rows)

    # Assert
    assert out == [{"name": "Good", "email": "good@example.com"}]


def test_drops_email_without_at_symbol():
    # Arrange
    rows = [
        {"name": "Bad", "email": "notanemail"},
        {"name": "Good", "email": "good@example.com"},
    ]

    # Act
    out = clean_rows(rows)

    # Assert
    assert out == [{"name": "Good", "email": "good@example.com"}]
