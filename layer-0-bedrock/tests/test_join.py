from src.join import left_join_by_email


def test_left_join_adds_right_fields_when_match():
    left = [{"name": "Alice", "email": "alice@example.com"}]
    right = [{"email": "alice@example.com", "plan": "pro"}]

    out, right_fields = left_join_by_email(left, right)

    assert set(right_fields) == {"plan"}
    assert out == [{"name": "Alice", "email": "alice@example.com", "plan": "pro"}]


def test_left_join_blanks_when_no_match():
    left = [{"name": "Carol", "email": "carol@example.com"}]
    right = [{"email": "alice@example.com", "plan": "pro"}]

    out, _ = left_join_by_email(left, right)

    assert out == [{"name": "Carol", "email": "carol@example.com", "plan": ""}]


def test_left_join_normalizes_email():
    left = [{"name": "Bob", "email": " BOB@Example.com "}]
    right = [{"email": "bob@example.com", "plan": "free"}]

    out, _ = left_join_by_email(left, right)

    assert out[0]["email"] == "bob@example.com"
    assert out[0]["plan"] == "free"


def test_join_matches_messy_right_email():
    # Arrange
    left = [{"name": "Alice", "email": "alice@example.com"}]
    right = [{"email": " ALICE@EXAMPLE.COM ", "plan": "pro"}]

    # Act
    out, _ = left_join_by_email(left, right)

    # Assert
    assert out[0]["plan"] == "pro"
    assert out[0]["email"] == "alice@example.com"
