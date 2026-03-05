from typing import List
def bs(nums: List[int], target: int) -> int:
    def go(l: int, r: int) -> int:
        if l > r: return -1
        m = (l+r)//2
        if nums[m] == target: return m
        if nums[m] < target: return go(m+1, r)
        return go(l, m-1)
    return go(0, len(nums)-1)
if __name__ == "__main__":
    assert bs([-1,0,3,5,9,12], 9) == 4
    assert bs([-1,0,3,5,9,12], 2) == -1
    print("ok")
