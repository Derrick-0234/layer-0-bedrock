from typing import List
def missing_number(nums: List[int]) -> int:
    n = len(nums)
    expect = n * (n + 1) // 2
    return expect - sum(nums)
if __name__ == "__main__":
    assert missing_number([3,0,1]) == 2
    assert missing_number([0,1]) == 2
    assert missing_number([9,6,4,2,3,5,7,0,1]) == 8
    print("ok")
