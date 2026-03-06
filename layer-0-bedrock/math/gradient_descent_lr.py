import random
from typing import List, Tuple

def make_data(n: int = 200, true_w: float = 2.5, true_b: float = -0.7, noise_std: float = 0.3, seed: int = 0) -> Tuple[List[float], List[float]]:
    rng = random.Random(seed)
    xs: List[float] = []
    ys: List[float] = []
    for _ in range(n):
        # normal-ish: sum of uniforms (CLT)
        x = sum(rng.uniform(-1.0, 1.0) for _ in range(6)) / 6.0
        noise = rng.gauss(0.0, noise_std)
        y = true_w * x + true_b + noise
        xs.append(x)
        ys.append(y)
    return xs, ys

def mse_and_grads(xs: List[float], ys: List[float], w: float, b: float) -> Tuple[float, float, float]:
    n = len(xs)
    if n == 0 or len(ys) != n:
        raise ValueError("xs and ys must be same non-zero length")

    loss = 0.0
    dw = 0.0
    db = 0.0
    for x, y in zip(xs, ys):
        yhat = w * x + b
        err = yhat - y
        loss += err * err
        dw += 2.0 * err * x
        db += 2.0 * err

    mse = loss / n
    dw /= n
    db /= n
    return mse, dw, db

def gradient_descent(xs: List[float], ys: List[float], alpha: float = 0.1, steps: int = 500) -> Tuple[float, float]:
    w, b = 0.0, 0.0
    prev = None

    for t in range(1, steps + 1):
        J, dw, db = mse_and_grads(xs, ys, w, b)
        w -= alpha * dw
        b -= alpha * db

        if t % 50 == 0:
            print(f"iter={t:>3}  loss={J:.6f}  w={w:.3f}  b={b:.3f}")

        # strict: loss should trend down (allow a little noise early, but not explode)
        if prev is not None and t % 50 == 0:
            assert J <= prev * 1.05, (prev, J)  # allow 5% wiggle
            prev = J
        elif prev is None and t % 50 == 0:
            prev = J

    return w, b

if __name__ == "__main__":
    xs, ys = make_data()
    w, b = gradient_descent(xs, ys, alpha=0.1, steps=500)

    # strict sanity: learned params should be in the ballpark
    assert abs(w - 2.5) < 0.3, w
    assert abs(b + 0.7) < 0.3, b

    print("ok")
