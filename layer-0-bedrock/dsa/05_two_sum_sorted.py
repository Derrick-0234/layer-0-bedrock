from typing import List, Tuple

def two_sum_sorted(nums: List[int], target: int) -> Tuple[int, int]:
    """
    nums is sorted ascending.
    Return 0-based indices (i, j) such that nums[i] + nums[j] == target.
    """
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return (i, j)
        if s < target:
            i += 1
        else:
            j -= 1
    raise ValueError("No solution")

if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_sorted([1, 2, 3, 4, 6], 6) == (1, 3)
    print("ok")
