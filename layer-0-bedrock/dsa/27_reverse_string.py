from typing import List
def reverse_string(s: List[str]) -> List[str]:
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1; j -= 1
    return s
if __name__ == "__main__":
    assert reverse_string(list("hello")) == list("olleh")
    assert reverse_string(list("Hannah")) == list("hannaH")
    print("ok")
