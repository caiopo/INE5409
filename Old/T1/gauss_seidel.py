import numpy as np


# def func(x, i, rel):
#     if i == 0:  # ops = 5
#         return (1 - rel) * x[0] + rel * (1.5 - x[1])

#     if 1 <= i < len(x) // 2:  # ops = 8
#         return (1 - rel) * x[i] + rel * (1 - x[i - 1] - x[i + 1] - x[i + 25]) / 4

#     if len(x) // 2 <= i < len(x) - 1:  # ops =  8
#         return (1 - rel) * x[i] + rel * (2 - x[i - 25] - x[i - 1] - x[i + 1]) / 5

#     if i == len(x) - 1:  # ops = 5
#         return (1 - rel) * x[len(x) - 1] + rel * (3 - x[len(x) - 2])

#     raise ValueError('Invalid value for i')

def func(x, i, rel):
    if i == 0:
        return 150 - x[1]

    if i == 1:
        return (100 - x[0] - x[2]) / 9

    if i == 2:
        return (200 - x[1] - x[3]) / 9

    if i == 3:
        return 300 - x[2]


# x1 = 150 - x2
# x2 = (100 - x1 - x3) / 9
# x3 = (200 - x2 - x4) / 9
# x4 = 300 - x3


def gauss_seidel(rel, crit, x):
    k = 0
    dif = float('inf')

    n = len(x)

    oldx = np.zeros(n, dtype=float)

    while dif > crit:
        for i in range(n):
            x[i] = func(x, i, rel)

        dif = max(abs(x - oldx))  # ops = n

        oldx = x.copy()

        k += 1

    return x, k


def converges(A):
    d = False

    for i in range(len(A)):

        s = sum(A[i][:i]) + sum(A[i][i + 1:len(A)])

        if A[i][i] < s:
            return False

        if A[i][i] > s:
            d = True

    return d


if __name__ == '__main__':
    print(gauss_seidel(1, 1e-2, np.zeros(4)))
