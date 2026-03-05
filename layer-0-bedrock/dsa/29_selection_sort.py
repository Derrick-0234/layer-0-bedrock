from typing import List
def selection_sort(nums: List[int]) -> List[int]:
    a = nums[:]
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a
if __name__ == "__main__":
    assert selection_sort([3,2,1]) == [1,2,3]
    assert selection_sort([5,1,1,2,0,0]) == [0,0,1,1,2,5]
    print("ok")
