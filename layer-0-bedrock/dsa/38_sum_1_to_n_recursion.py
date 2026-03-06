def sum_to_n(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    return n + sum_to_n(n-1)
if __name__ == "__main__":
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    print("ok")
