from typing import List
def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    out = [0]*n
    i, j, w = 0, n-1, n-1
    while i <= j:
        a = nums[i]*nums[i]
        b = nums[j]*nums[j]
        if a > b:
            out[w] = a; i += 1
        else:
            out[w] = b; j -= 1
        w -= 1
    return out
if __name__ == "__main__":
    assert sorted_squares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sorted_squares([-7,-3,2,3,11]) == [4,9,9,49,121]
    print("ok")
