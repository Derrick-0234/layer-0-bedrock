def valid_palindrome(s: str) -> bool:
    def is_pal(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1; j -= 1
        return True
    i, j = 0, len(s)-1
    while i < j:
        if s[i] == s[j]:
            i += 1; j -= 1
        else:
            return is_pal(i+1, j) or is_pal(i, j-1)
    return True
if __name__ == "__main__":
    assert valid_palindrome("aba") is True
    assert valid_palindrome("abca") is True
    assert valid_palindrome("abc") is False
    print("ok")
