import random
from typing import List

def simulate_coin_flips(n: int, p_heads: float = 0.5, seed: int = 0) -> List[int]:
    rng = random.Random(seed)
    return [1 if rng.random() < p_heads else 0 for _ in range(n)]

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def variance(xs: List[float]) -> float:
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)

if __name__ == "__main__":
    for n in [10, 100, 1000, 10000]:
        flips = simulate_coin_flips(n, p_heads=0.5, seed=42)
        m = mean(flips)
        v = variance(flips)
        print(f"n={n:<5} mean={m:.4f} variance={v:.4f}")

    # sanity: for a fair coin, mean -> 0.5 and variance -> 0.25 as n grows
    flips = simulate_coin_flips(10000, p_heads=0.5, seed=42)
    m = mean(flips)
    v = variance(flips)
    assert abs(m - 0.5) < 0.03
    assert abs(v - 0.25) < 0.03
    print("ok")
