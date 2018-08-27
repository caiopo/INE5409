import numpy as np

n = 50  # Tamanho da matrix (n*n)


def create_matrix():
    A = np.zeros((n, n))
    b = np.zeros(n)

    A[0, 0] = 1
    A[0, 1] = 1
    b[0] = 1.5

    for i in range(1, n // 2):
        A[i, i] = 4
        A[i, i + 25] = 1
        A[i, i + 1] = 1
        A[i, i - 1] = 1
        b[i] = 1

    for i in range(n // 2, n - 1):
        A[i, i] = 5
        A[i, i - 25] = 1
        A[i, i + 1] = 1
        A[i, i - 1] = 1
        b[i] = 2

    A[n - 1, n - 1] = 1
    A[n - 1, n - 2] = 1
    b[n - 1] = 3

    return A, b
