from typing import List

Matrix = List[List[float]]
Vector = List[float]

def solve_axb(A: Matrix, b: Vector) -> Vector:
    n = len(A)
    if n == 0 or any(len(row) != n for row in A) or len(b) != n:
        raise ValueError("A must be n×n and b length n")

    # make copies
    M = [row[:] for row in A]
    y = b[:]

    # forward elimination with partial pivoting
    for col in range(n):
        # pivot row
        pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot][col]) < 1e-12:
            raise ValueError("Singular matrix")
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
            y[col], y[pivot] = y[pivot], y[col]

        # eliminate below
        for r in range(col + 1, n):
            factor = M[r][col] / M[col][col]
            if factor == 0:
                continue
            for c in range(col, n):
                M[r][c] -= factor * M[col][c]
            y[r] -= factor * y[col]

    # back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, n):
            s -= M[i][j] * x[j]
        x[i] = s / M[i][i]
    return x

if __name__ == "__main__":
    A = [[2,1],[5,7]]
    b = [11,13]
    x = solve_axb(A,b)
    # expected [7.111..., -3.222...]
    assert abs(x[0] - 7.1111111111) < 1e-6
    assert abs(x[1] + 3.2222222222) < 1e-6
    print("ok")
