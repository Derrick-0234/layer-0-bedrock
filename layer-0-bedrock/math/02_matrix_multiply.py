from typing import List

Matrix = List[List[float]]

def matmul(A: Matrix, B: Matrix) -> Matrix:
    if not A or not B or not A[0] or not B[0]:
        raise ValueError("Empty matrix")
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])
    if n != n2:
        raise ValueError("Shape mismatch")

    # pretranspose B for speed + clarity
    Bt = list(zip(*B))
    out: Matrix = []
    for i in range(m):
        row = []
        for j in range(p):
            s = 0.0
            for k in range(n):
                s += A[i][k] * Bt[j][k]
            row.append(s)
        out.append(row)
    return out

if __name__ == "__main__":
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    assert matmul(A,B) == [[19.0,22.0],[43.0,50.0]]
    print("ok")
