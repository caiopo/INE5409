import numpy as np


def gauss(A, b):
    n = len(A)

    A = np.concatenate((A, b.reshape(-1, 1)), axis=1).astype(float)

    for k in range(n):
        for i in range(k + 1, n):
            aux = A[i, k] / A[k, k]

            for j in range(k + 1, n + 1):
                A[i, j] -= aux * A[k, j]

            A[i, k] = 0

    x = np.zeros(n)

    x[n - 1] = A[n - 1, n] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        sum_ = 0

        for j in range(i + 1, n):
            sum_ += A[i, j] * x[j]

        x[i] = (A[i, n] - sum_) / A[i, i]

    return x


def residuo(A, b, x):
    return np.array([
        abs(sum(A[i] * x) - b[i])
        for i in range(len(A))
    ], dtype=float)


if __name__ == '__main__':
    A = np.array([
        [1, 1, 1],
        [2, -2, 3],
        [3, 1, -1],
    ])

    b = np.array(
        [-1, 2, 3]
    )

    x = gauss(A.copy(), b.copy())

    print('A:', A)
    print('b:', b)
    print('x:', x)

    print(residuo(A, b, x))

    print(A[2])
    print(b[2])
