from typing import List

def move_zeroes(nums: List[int]) -> List[int]:
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1
    while write < len(nums):
        nums[write] = 0
        write += 1
    return nums

if __name__ == "__main__":
    assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert move_zeroes([0]) == [0]
    print("ok")
