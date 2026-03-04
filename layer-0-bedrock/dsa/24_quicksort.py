from typing import List
def quicksort(nums: List[int]) -> List[int]:
    if len(nums) <= 1: return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quicksort(left) + mid + quicksort(right)
if __name__ == "__main__":
    assert quicksort([3,2,1]) == [1,2,3]
    assert quicksort([5,1,1,2,0,0]) == [0,0,1,1,2,5]
    print("ok")
