from typing import List
def remove_element(nums: List[int], val: int) -> int:
    w = 0
    for x in nums:
        if x != val:
            nums[w] = x
            w += 1
    return w
if __name__ == "__main__":
    a = [3,2,2,3]
    k = remove_element(a, 3)
    assert k == 2 and sorted(a[:k]) == [2,2]
    b = [0,1,2,2,3,0,4,2]
    k2 = remove_element(b, 2)
    assert k2 == 5 and sorted(b[:k2]) == [0,0,1,3,4]
    print("ok")
