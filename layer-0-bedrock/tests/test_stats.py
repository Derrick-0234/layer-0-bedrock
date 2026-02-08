from src.stats import summarize_scores


def test_good_scores_summary():
    rows = [{"score": "80"}, {"score": "90"}]
    out = summarize_scores(rows)
    assert out["count"] == 2
    assert out["min"] == 80.0
    assert out["max"] == 90.0
    assert out["mean"] == 85.0


def test_ignores_blank_and_bad_scores():
    rows = [{"score": ""}, {"score": "not-a-number"}, {"score": "70"}]
    out = summarize_scores(rows)
    assert out["count"] == 1
    assert out["min"] == 70.0


def test_empty_input_returns_empty_summary():
    out = summarize_scores([])
    assert out["count"] == 0
