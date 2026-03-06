import math
from typing import Callable, List, Tuple

def forward_diff(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h

def central_diff(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2.0 * h)

def run_convergence(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    hs: List[float],
) -> List[Tuple[float, float, float, float, float]]:
    """
    Returns rows: (h, forward, forward_err, central, central_err)
    """
    true = df(x0)
    out = []
    for h in hs:
        fd = forward_diff(f, x0, h)
        cd = central_diff(f, x0, h)
        out.append((h, fd, abs(fd - true), cd, abs(cd - true)))
    return out

def _print_table(title: str, rows: List[Tuple[float, float, float, float, float]]) -> None:
    print(title)
    print("h\tforward\tf_err\tcentral\tc_err")
    for h, fd, fe, cd, ce in rows:
        print(f"{h:.0e}\t{fd:.8f}\t{fe:.3e}\t{cd:.8f}\t{ce:.3e}")
    print()

if __name__ == "__main__":
    hs = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]

    # 1) f(x)=x^3, f'(x)=3x^2
    f1 = lambda x: x**3
    df1 = lambda x: 3*(x**2)
    rows1 = run_convergence(f1, df1, x0=1.7, hs=hs)
    _print_table("f(x)=x^3 at x=1.7", rows1)

    # 2) f(x)=sin(x), f'(x)=cos(x)
    f2 = math.sin
    df2 = math.cos
    rows2 = run_convergence(f2, df2, x0=1.0, hs=hs)
    _print_table("f(x)=sin(x) at x=1.0", rows2)

    # 3) f(x)=exp(x), f'(x)=exp(x)
    f3 = math.exp
    df3 = math.exp
    rows3 = run_convergence(f3, df3, x0=0.3, hs=hs)
    _print_table("f(x)=exp(x) at x=0.3", rows3)

    # strict check: central diff error should generally improve as h shrinks (until float limits)
    # We'll enforce improvement from 1e-1 -> 1e-4 for each function.
    def assert_improves(rows):
        e1 = rows[0][4]  # central_err at 1e-1
        e4 = rows[3][4]  # central_err at 1e-4
        assert e4 < e1, (e1, e4)

    assert_improves(rows1)
    assert_improves(rows2)
    assert_improves(rows3)

    print("ok")
