from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    i, j, w = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[w] = nums1[i]
            i -= 1
        else:
            nums1[w] = nums2[j]
            j -= 1
        w -= 1
    return nums1

if __name__ == "__main__":
    assert merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]
    assert merge([1], 1, [], 0) == [1]
    print("ok")
