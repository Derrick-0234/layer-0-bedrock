def can_construct(ransomNote: str, magazine: str) -> bool:
    counts = {}
    for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in ransomNote:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True

if __name__ == "__main__":
    assert can_construct("a", "b") is False
    assert can_construct("aa", "ab") is False
    assert can_construct("aa", "aab") is True
    print("ok")
