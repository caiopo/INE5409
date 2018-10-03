import numpy as np


def newton_snl(f, xi):
    tol = 1e-14

    n = len(xi)
    dx = np.full_like(xi, 2 * tol)

    a = np.ndarray(shape=(n, n), dtype=xi.dtype)

    k = 0

    while max(abs(dx)) > tol and k < 50:
        k += 1

        for j in range(n):
            xdx = xi.copy()
            xdx[j] = xi[j] + dx[j]

            a[:, j] = (f(xdx) - f(xi)) / dx[j]

        b = -f(xi)

        dx = np.linalg.solve(a, b)

        xi += dx

    return xi, k
