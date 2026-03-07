import csv
import math
from collections import Counter

def mean(xs):
    return sum(xs) / len(xs)

def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)

def std(xs):
    return math.sqrt(variance(xs))

def correlation(xs, ys):
    mx = mean(xs)
    my = mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    deny = math.sqrt(sum((y - my) ** 2 for y in ys))
    if denx == 0 or deny == 0:
        raise ValueError("zero variance")
    return num / (denx * deny)

def histogram(xs, bins=5):
    lo, hi = min(xs), max(xs)
    width = (hi - lo) / bins if hi != lo else 1
    counts = Counter()
    for x in xs:
        if x == hi:
            idx = bins - 1
        else:
            idx = int((x - lo) / width)
        counts[idx] += 1
    return lo, hi, width, counts

def print_histogram(xs, bins=5):
    lo, hi, width, counts = histogram(xs, bins=bins)
    print("Histogram:")
    for i in range(bins):
        left = lo + i * width
        right = left + width
        bar = "#" * counts[i]
        print(f"[{left:.2f}, {right:.2f}) {bar}")

if __name__ == "__main__":
    xs = []
    ys = []
    with open("data/stats_small.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            xs.append(float(row["x"]))
            ys.append(float(row["y"]))

    print(f"x mean={mean(xs):.4f}")
    print(f"x std={std(xs):.4f}")
    print(f"y mean={mean(ys):.4f}")
    print(f"y std={std(ys):.4f}")
    print(f"corr(x,y)={correlation(xs, ys):.4f}")
    print_histogram(ys, bins=5)

    # sanity
    assert abs(mean(xs) - 5.5) < 1e-9
    assert correlation(xs, ys) > 0.9
    print("ok")
