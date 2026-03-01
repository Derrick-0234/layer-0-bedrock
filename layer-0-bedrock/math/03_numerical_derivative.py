from typing import Callable

def numerical_derivative(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    # central difference: (f(x+h)-f(x-h)) / (2h)
    return (f(x + h) - f(x - h)) / (2.0 * h)

if __name__ == "__main__":
    # f(x)=x^2 => f'(x)=2x
    f = lambda t: t * t
    d = numerical_derivative(f, 3.0)
    assert abs(d - 6.0) < 1e-3

    # f(x)=sin(x) => f'(x)=cos(x)
    import math
    g = math.sin
    d2 = numerical_derivative(g, 1.0)
    assert abs(d2 - math.cos(1.0)) < 1e-3

    print("ok")
