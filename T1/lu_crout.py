import numpy as np
from operator import itemgetter


# def swap_rows(k, A, b):
#     n = len(A)

#     max_index, max_value = max(
#         enumerate(A[:, k][k:]),
#         key=lambda t: abs(t[1]),
#     )

#     # print(f'mi: {max_index}, mv: {max_value}')

#     A[[k, max_index]] = A[[max_index, k]]
#     b[[k, max_index]] = b[[max_index, k]]


def swap_rows(k, A, b):
    n = len(A)

    max_value = abs(A[k, k])
    max_index = k

    for i in range(k + 1, n):
        if abs(A[i, k]) > max_value:
            max_value = abs(A[i, k])
            max_index = i

    A[[k, max_index]] = A[[max_index, k]]
    b[[k, max_index]] = b[[max_index, k]]


def decompose(A, b):
    A = np.copy(A)

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


if __name__ == '__main__':
    A = np.array([
        [0, 1, 2],
        [2, -1, -1],
        [1, 0, 1],
    ], dtype=float)

    b = np.array([
        [1],
        [2],
        [3],
    ], dtype=float)

    A, b = decompose(A, b)

    print(A)
    print(b)
