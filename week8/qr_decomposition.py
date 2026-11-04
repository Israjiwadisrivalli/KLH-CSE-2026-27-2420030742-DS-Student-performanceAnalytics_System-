
import numpy as np

A = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 1]], dtype=float)

b = np.array([4, 5, 6], dtype=float)

Q = np.zeros((3, 3))
R = np.zeros((3, 3))

for j in range(3):
    v = A[:, j].copy()
    for i in range(j):
        R[i, j] = np.dot(Q[:, i], A[:, j])
        v -= R[i, j] * Q[:, i]

    R[j, j] = np.linalg.norm(v)
    Q[:, j] = v / R[j, j]

x = np.linalg.solve(R, Q.T @ b)

print("Matrix A:\n", A)
print("\nOrthogonal Matrix Q:\n", Q)
print("\nUpper Triangular Matrix R:\n", R)
print("\nSolution Vector x:\n", x)
