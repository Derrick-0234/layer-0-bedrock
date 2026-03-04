from typing import List
def remove_duplicates(nums: List[int]) -> int:
    if not nums: return 0
    w = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[w] = nums[i]
            w += 1
    return w
if __name__ == "__main__":
    a = [1,1,2]; k = remove_duplicates(a); assert k == 2 and a[:k] == [1,2]
    b = [0,0,1,1,1,2,2,3,3,4]; k2 = remove_duplicates(b); assert k2 == 5 and b[:k2] == [0,1,2,3,4]
    print("ok")
