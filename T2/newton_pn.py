from math import pi

import numpy as np
from random import random

from newton_geral import frange


def pn(p, x):
    y = p[0]

    for i in p[1:]:
        y = y * x + i

    return y


def find_roots_pn(p):
    r = 1 + max(abs(p[1:])) / p[0]

    xi = []

    start = -r
    stop = r

    step = 1 / (10 * pi)

    for a in frange(start, stop, step):
        b = a + step

        fa = pn(p, a)
        fb = pn(p, b)

        if fa * fb <= 0:
            xi.append((a + b) / 2)

    for i in range(len(xi) + 1, len(p)):
        xi.append(
            (random() - 0.5) * 0.5 * r
        )

    return np.array(xi)


def briot_ruffini(n, p, x):
    b = np.zeros(n, dtype=float)

    for i in range(0, n):
        b[i] = p[i] + x * b[i - 1]

    return n - 1, b


def remainder(p, xi):
    k = 0
    n = len(p) - 1
    ndiv = len(p)
    r = np.zeros_like(p)

    r[-1] = p[0]

    while n > 0 and k < ndiv:
        b = [p[0]]

        for i in range(1, n + 1):
            b.append(p[i] + xi * b[i - 1])

        r[k] = b[n]

        p = np.array(b)
        k += 1
        n -= 1

    return r


def multiplicidade(r):
    rlim = 1e-5

    m = 1

    sum_ = abs(r[0]) + abs(r[1])

    while sum_ < rlim:
        sum_ += abs(r[m + 1])
        m += 1

    return m


def newton_pn(p, xi, tol=1e-14, use_multiplicidade=True):
    dx = 2 * tol
    k = 0
    m = 1

    while abs(dx) > tol and k < 50:
        k += 1

        r = remainder(p, xi)
        m = multiplicidade(r) if use_multiplicidade else 1

        dx = -r[m - 1] / (m * r[m])

        xi += dx

    return xi, m


def solve_newton_pn(p, use_multiplicidade=True):
    n = len(p) - 1
    x = np.zeros(n, dtype=float)
    m = np.zeros(n, dtype=int)

    for i in range(1, n):
        p[i] = p[i] / p[0]

    p[0] = 1

    xi = find_roots_pn(p)

    k = 0

    while n > 0:
        x[k], m[k] = newton_pn(p, xi[k], use_multiplicidade=use_multiplicidade)

        for j in range(m[k]):
            n, p = briot_ruffini(n, p, x[k])

        k += 1

    return x[:k], m[:k]


if __name__ == '__main__':
    def main():
        p = np.array([1, -3, 3, -1], dtype=float)

        roots, multp = solve_newton_pn(p)

        print(list(roots))
        print(multp)


    main()
