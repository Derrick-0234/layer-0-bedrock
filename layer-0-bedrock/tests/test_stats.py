from src.stats import summarize_scores


def test_good_scores_summary():
    # Arrange
    rows = [{"score": "80"}, {"score": "90"}]

    # Act
    out = summarize_scores(rows)

    # Assert
    assert out["count"] == 2
    assert out["min"] == 80.0
    assert out["max"] == 90.0
    assert out["mean"] == 85.0


def test_ignores_blank_and_bad_scores():
    # Arrange
    rows = [{"score": ""}, {"score": "not-a-number"}, {"score": "70"}]

    # Act
    out = summarize_scores(rows)

    # Assert
    assert out["count"] == 1
    assert out["min"] == 70.0
    assert out["max"] == 70.0
    assert out["mean"] == 70.0


def test_empty_input_returns_empty_summary():
    # Arrange
    rows = []

    # Act
    out = summarize_scores(rows)

    # Assert
    assert out["count"] == 0


def test_ignores_not_a_number_and_keeps_good_score():
    # Arrange
    rows = [{"score": "not-a-number"}, {"score": "80"}]

    # Act
    out = summarize_scores(rows)

    # Assert
    assert out["count"] == 1
    assert out["min"] == 80.0
    assert out["max"] == 80.0
    assert out["mean"] == 80.0
