import numpy as np

'''
i=1;            x(i)+x(i+1) = 1.50
i=2:n/2         x(i-1)+4x(i)+x(i+1) = 1.00
i=n/2+1:n-1     x(i-1)+5x(i)+x(i+1) = 2.00
i=n;            x(i-1)+x(i) = 3.00
'''


def func(x, i):  # ops = 146 = 1 + 69 + 75 + 1
    if i == 0:
        return 1.5 - x[i + 1]  # ops = 1 * 1

    if 1 <= i <= len(x) // 2:
        return (1 - x[i - 1] - x[i + 1]) / 4  # ops = 3 * 23

    if len(x) // 2 + 1 <= i < len(x) - 1:
        return (2 - x[i - 1] - x[i + 1]) / 5  # ops = 3 * 25

    if i == len(x) - 1:
        return 3 - x[i - 1]  # ops = 1 * 1

    raise ValueError('Invalid value for i')


def gauss_seidel(rel, crit, n):  # ops = 346 * n
    k = 0
    dif = np.inf

    x = np.zeros(n, dtype=float)
    oldx = np.zeros(n, dtype=float)

    while dif > crit:
        for i in range(n):
            x[i] = (1 - rel) * x[i] + rel * func(x, i)  # ops = 346 = 200 + 146

        dif = max(abs(x - oldx))  # ops = 50

        oldx = x.copy()

        k += 1

    return x, k


def converges(A):
    d = False

    for i in range(len(A)):

        s = sum(A[i]) - A[i][i]

        if A[i][i] < s:
            return False

        if A[i][i] > s:
            d = True

    return d
