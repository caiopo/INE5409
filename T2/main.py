from math import cos, sin
from math import exp

import numpy as np

from newton_geral import residuo, solve_newton_geral
from newton_pn import pn, solve_newton_pn
# ------ Questão 1 ------
from newton_snl import newton_snl


def f1(x):
    return x * x * x - exp(x)


def f1_second_derivative(x):
    return 6 * x - exp(x)


roots1 = solve_newton_geral(f1, -10, 10)
res1 = residuo(f1, roots1)

print('Questão 1\n')

for i, (root, res) in enumerate(zip(roots1, res1)):
    print('raiz{} = {}, resíduo = {}'.format(i, root, res))

descontinuidades = solve_newton_geral(f1_second_derivative, -10, 10)

print('Os pontos de descontinuidade são:', descontinuidades)

# ------ Questão 2 ------

print('\n\n\nQuestão 2\n')
p = np.array([1, -7, 20.95, -34.75, 34.5004, -20.5012, 6.7512, -0.9504, 0, 0, 0])

roots2, multp2 = solve_newton_pn(p)

for i, (root, m) in enumerate(zip(roots2, multp2)):
    res = pn(p, root)
    print('x{} = {}, M = {}, resíduo = {}'.format(i, root, m, res))

roots_np = np.roots(p)
roots_np.sort()

print('\nRaízes encontradas pelo NumPy:')
for i, root in enumerate(roots_np):
    res = pn(p, root)
    print('x{} = {}, resíduo = {}'.format(i, root, res))

# ------ Questão 3 ------

print('\n\n\nQuestão 3\n')


def fsnl(x):
    y = np.zeros_like(x)

    y[0] = x[0] ** 3 + x[1] ** 3 - 2
    y[1] = sin(x[0]) * cos(x[1]) - 0.45

    return y


xi3 = np.array([0.5, 0.5], dtype=float)
roots3, num_iter3 = newton_snl(fsnl, xi3.copy())

print('X inicial:', xi3)
print('Raízes encontradas:', roots3)
print('Número de iterações:', num_iter3)

print('Resíduo máximo:', max(abs(fsnl(roots3))))
