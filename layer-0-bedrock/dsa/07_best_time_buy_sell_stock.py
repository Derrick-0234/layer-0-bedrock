from typing import List

def max_profit(prices: List[int]) -> int:
    min_price = 10**18
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        else:
            best = max(best, p - min_price)
    return best

if __name__ == "__main__":
    assert max_profit([7,1,5,3,6,4]) == 5
    assert max_profit([7,6,4,3,1]) == 0
    print("ok")
