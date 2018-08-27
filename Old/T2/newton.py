import numpy as np


def multiplicidade(R, lim):
    m = 1

    sum_ = abs(R[0]) + abs(R[1])

    while sum_ < lim:
        sum_ += abs(R[m])

    return m


def briot_ruffini(n, p, x):
    ni = n

    r = np.zeros_like(p)

    for k in range(n):
        b = np.zeros_like(p)

        b[0] = p[0]

        for i in range(1, n + 1):
            b[i] = p[i] + x * b[i - 1]

        r[k] = b[n]

        p = b[:]

        n -= 1

    r[ni] = 1

    return r


def newton(n, p, x):
    dif = 1
    k = 0

    while dif > 1e-12 and k < 120:
        k += 1

        r = briot_ruffini(n, p, x)

        m = multiplicidade(r, 0.1)

        delta = -r[m] / (m * r[m + 1])

        dif = abs(delta)

        x += delta

    return x, r


if __name__ == '__main__':
    p = np.array([2, 3, 0, -4])

    print(briot_ruffini(3, p.copy(), 5))
