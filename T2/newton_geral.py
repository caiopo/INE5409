from math import pi, tan

import numpy as np


def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step


# Find unoptimized roots in interval [start, end]
def find_roots(f, start, end):
    step = 0.001
    limit = 0.5

    roots = []

    for a in frange(start, end, step):
        b = a + step

        fa = f(a)
        fb = f(b)

        if (fa * fb < 0 and
                fa < limit and
                fb < limit):
            roots.append((a + b) / 2)

    return np.array(roots)


# Optimize root using Newton's Method
def optimize_root(f, xi, tol=1e-15):
    dx = 2 * tol
    k = 0

    while abs(dx) > tol and k < 50:
        k += 1
        fxi = f(xi)
        dx = -fxi * dx / (f(xi + dx) - fxi)
        xi += dx

    return xi


def newton_geral(f, start, end):
    roots = find_roots(f, start, end)

    return np.array([
        optimize_root(f, x) for x in roots
    ])


def residuo(f, roots):
    return np.array([abs(f(r)) for r in roots])


if __name__ == '__main__':
    def main():
        def f(x):
            return x * tan(x) - 1

        roots = newton_geral(f, 0, 3 * pi)

        print(roots)
        print(residuo(f, roots))


    main()
