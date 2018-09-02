import numpy as np


def gauss_tridiagonal(t, r, d, b):
    n = len(r)
    x = np.zeros(n)
    t = np.copy(t)
    r = np.copy(r)
    d = np.copy(d)
    b = np.copy(b)

    for i in range(1, n):
        aux = t[i] / r[i - 1]
        r[i] = r[i] - aux * d[i - 1]
        b[i] = b[i] - aux * b[i - 1]

    x[n - 1] = b[n - 1] / r[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - d[i] * x[i + 1]) / r[i]

    return x
