import numpy as np
from operator import itemgetter


def swap_rows(k, A, b):
    n = len(A)

    max_value, max_index = max(
        (abs(A[i, k]), i)
        for i in range(k, n)
    )

    A[[k, max_index]] = A[[max_index, k]]
    b[[k, max_index]] = b[[max_index, k]]


def decompose(A, b):
    A = np.copy(A)
    b = np.copy(b)

    n = len(A)

    for k in range(0, n):

        for i in range(k, n):
            sum_ = 0

            for r in range(0, k):
                sum_ += A[i, r] * A[r, k]

            A[i, k] = A[i, k] - sum_

        swap_rows(k, A, b)

        for j in range(k + 1, n):
            sum_ = 0

            for r in range(0, k):
                sum_ += A[k, r] * A[r, j]

            A[k, j] = (A[k, j] - sum_) / A[k, k]

    return A, b


def calc_x(A, b):
    n = len(A)

    c = np.zeros(n)
    x = np.zeros(n)

    c[0] = b[0] / A[0, 0]

    for i in range(1, n):
        sum_ = sum(A[i, :i] * c[:i])
        c[i] = (b[i] - sum_) / A[i, i]

    x[n - 1] = c[n - 1]

    for i in range(n - 2, -1, -1):
        sum_ = sum(A[i, i + 1:] * x[i + 1:])
        x[i] = c[i] - sum_

    return x


def lu_crout(A, b):
    A, b = decompose(A, b)

    x = calc_x(A, b)

    return x


def residuo(A, b, x):
    return np.array([
        abs(sum(A[i] * x) - b[i])
        for i in range(len(A))
    ], dtype=float)


if __name__ == '__main__':
    A = np.array([
        [0, 1, 2],
        [2, -1, -1],
        [1, 0, 1],
    ], dtype=float)

    bs = [
        np.array([1, 2, 3], dtype=float),
        np.array([0, 1, 2], dtype=float),
        np.array([3, 5, 7], dtype=float),
        np.array([1, -1, 5], dtype=float),
    ]

    for b in bs:
        X = lu_crout(A, b)

        print(X)
