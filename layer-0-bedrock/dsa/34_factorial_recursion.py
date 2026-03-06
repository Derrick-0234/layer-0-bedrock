def fact(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return 1
    return n * fact(n-1)

if __name__ == "__main__":
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 120
    print("ok")
