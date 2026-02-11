from src.log_parse import parse_log

def test_parse_log_skips_bad_lines_and_parses_good():
    text = "\n".join([
        "2026-02-10 12:34:56 INFO hello",
        "not a log line",
        "2026-02-10 12:35:00 ERROR boom",
    ])
    rows = parse_log(text)
    assert len(rows) == 2
    assert rows[0].level == "INFO"
    assert rows[0].message == "hello"
    assert rows[1].level == "ERROR"
    assert rows[1].message == "boom"
