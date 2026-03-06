from typing import List
def insertion_sort(nums: List[int]) -> List[int]:
    a = nums[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

if __name__ == "__main__":
    assert insertion_sort([3,2,1]) == [1,2,3]
    assert insertion_sort([5,1,1,2,0,0]) == [0,0,1,1,2,5]
    print("ok")
