import numpy as np

'''
i=1;            x(i)+x(i+1) = 1.50
i=2:n/2         x(i-1)+4x(i)+x(i+1) = 1.00
i=n/2+1:n-1     x(i-1)+5x(i)+x(i+1) = 2.00
i=n;            x(i-1)+x(i) = 3.00
'''


def create_complete_matrix(n):
    A = np.zeros((n, n))
    b = np.zeros(n)

    A[0, 0] = 1
    A[0, 1] = 1
    b[0] = 1.5

    for i in range(1, n // 2 + 1):
        A[i, i - 1] = 1
        A[i, i] = 4
        A[i, i + 1] = 1
        b[i] = 1

    for i in range(n // 2 + 1, n - 1):
        A[i, i - 1] = 1
        A[i, i] = 5
        A[i, i + 1] = 1
        b[i] = 2

    A[n - 1, n - 1] = 1
    A[n - 1, n - 2] = 1
    b[n - 1] = 3

    return A, b


def create_tridiagonal_matrix(n):
    A, b = create_complete_matrix(n)

    d = np.append(A.diagonal(offset=1), [np.nan])
    r = A.diagonal(offset=0)
    t = np.append([np.nan], A.diagonal(offset=-1))

    return t, r, d, b


if __name__ == '__main__':
    A, b = create_matrix(50)

    for line in A.tolist():
        print(line)
