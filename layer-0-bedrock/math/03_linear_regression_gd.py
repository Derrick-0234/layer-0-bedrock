from typing import List, Tuple

def predict(x: float, w: float, b: float) -> float:
    return w * x + b

def mse_and_grads(xs: List[float], ys: List[float], w: float, b: float) -> Tuple[float, float, float]:
    """
    Returns (mse, dw, db) for linear regression yhat = w*x + b
    mse = mean((yhat - y)^2)
    """
    n = len(xs)
    if n == 0 or len(ys) != n:
        raise ValueError("xs and ys must be same non-zero length")

    loss = 0.0
    dw = 0.0
    db = 0.0
    for x, y in zip(xs, ys):
        yhat = predict(x, w, b)
        err = yhat - y
        loss += err * err
        dw += 2.0 * err * x
        db += 2.0 * err
    mse = loss / n
    dw /= n
    db /= n
    return mse, dw, db

def gradient_descent(xs: List[float], ys: List[float], lr: float = 0.05, steps: int = 2000) -> Tuple[float, float]:
    w, b = 0.0, 0.0
    for _ in range(steps):
        mse, dw, db = mse_and_grads(xs, ys, w, b)
        w -= lr * dw
        b -= lr * db
    return w, b

if __name__ == "__main__":
    # synthetic line: y = 2x + 1
    xs = [0, 1, 2, 3, 4, 5]
    ys = [1, 3, 5, 7, 9, 11]

    w, b = gradient_descent(xs, ys, lr=0.05, steps=3000)

    # should be close to 2 and 1
    assert abs(w - 2.0) < 1e-2
    assert abs(b - 1.0) < 1e-2

    print("ok")
