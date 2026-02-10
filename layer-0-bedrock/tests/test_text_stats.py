from src.text_stats import top_words

def test_top_words_counts_and_order():
    text = "Hello hello world! world world"
    total, top = top_words(text, k=10)

    assert total == 5
    assert top[0] == ("world", 3)
    assert top[1] == ("hello", 2)
