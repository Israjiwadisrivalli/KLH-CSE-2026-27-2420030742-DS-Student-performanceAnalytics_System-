
import numpy as np

A = np.array([[2, -1, -2],
              [-4, 6, 3],
              [-4, -2, 8]], dtype=float)

b = np.array([-2, 9, -5], dtype=float)

L = np.eye(3)
U = np.zeros((3, 3))

for i in range(3):
    for j in range(i, 3):
        U[i, j] = A[i, j] - sum(L[i, k]*U[k, j] for k in range(i))

    for j in range(i+1, 3):
        L[j, i] = (A[j, i] - sum(L[j, k]*U[k, i] for k in range(i))) / U[i, i]

y = np.linalg.solve(L, b)
x = np.linalg.solve(U, y)

print("Matrix A:\n", A)
print("\nLower Matrix L:\n", L)
print("\nUpper Matrix U:\n", U)
print("\nIntermediate Solution y:\n", y)
print("\nFinal Solution x:\n", x)
