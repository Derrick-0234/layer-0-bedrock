from typing import List
def bubble_sort(nums: List[int]) -> List[int]:
    a = nums[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a
if __name__ == "__main__":
    assert bubble_sort([3,2,1]) == [1,2,3]
    assert bubble_sort([5,1,1,2,0,0]) == [0,0,1,1,2,5]
    print("ok")
