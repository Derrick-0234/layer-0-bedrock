from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counts = {}
    for x in nums1:
        counts[x] = counts.get(x, 0) + 1
    out = []
    for x in nums2:
        if counts.get(x, 0) > 0:
            out.append(x)
            counts[x] -= 1
    return out
if __name__ == "__main__":
    assert sorted(intersect([1,2,2,1],[2,2])) == [2,2]
    assert sorted(intersect([4,9,5],[9,4,9,8,4])) == [4,9]
    print("ok")
