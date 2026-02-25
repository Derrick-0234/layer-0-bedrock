from typing import List

def majority_element(nums: List[int]) -> int:
    counts = {}
    need = len(nums) // 2
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > need:
            return x
    return nums[0]

if __name__ == "__main__":
    assert majority_element([3,2,3]) == 3
    assert majority_element([2,2,1,1,1,2,2]) == 2
    print("ok")
