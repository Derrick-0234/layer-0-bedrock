def first_bad_version(n: int, is_bad) -> int:
    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        if is_bad(m):
            r = m
        else:
            l = m + 1
    return l

if __name__ == "__main__":
    bad = 4
    def is_bad(x): return x >= bad
    assert first_bad_version(5, is_bad) == 4
    bad = 1
    assert first_bad_version(1, is_bad) == 1
    print("ok")
