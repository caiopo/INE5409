from gauss import gauss, residuo
from gauss_seidel import gauss_seidel, converges
from matrix import create_matrix, n

import numpy as np


A, b = create_matrix()

g_res = gauss(A, b)

g_mres = max(abs(residuo(A, b, g_res)))

print('A1:')
print('Primeira:', g_res[0])
print('Última:', g_res[-1])
print('Resíduo máximo:', g_mres)

print('\nA2:')
print('Operações em ponto flutuante:', (4 * n**3 + 9 * n**2 - n - 6) // 6)


criteria = 1e-4

print('\nB1:')

if converges(A):
    print('O sistema possui diagonal dominante e sempre irá convergir. '
          'Podemos acelerar o cálculo usando um fator de sobre-relaxação.')
else:
    print('O sistema não possui diagonal dominante e '
          'talvez não venha a convergir')


print('\nB2:')
print('Para encontrar o fator de relaxação que faz '
      'a função convergir mais rapidamente vamos buscar '
      'entre 0.1 e 1.9:')

conv = []

for rel in range(1, 20):
    _, c = gauss_seidel(rel / 10, criteria, np.zeros(50, dtype=float))
    print('Fator =', rel / 10, '| Iterações =', c)

    conv.append((c, rel))

min_iters, rel = min(conv)

rel /= 10

print('Podemos ver que fator de relaxação que '
      'converge mais rápido é {}, com {} iterações'.format(rel, min_iters))


gs_res, gs_iters = gauss_seidel(rel, criteria, np.zeros(50, dtype=float))

gs_mres = max(abs(residuo(A, b, gs_res)))

print('\nB3:')
print('Primeira:', gs_res[0])
print('Última:', gs_res[-1])
print('Resíduo máximo:', gs_mres)

print('\nB4:')
print('Operações em ponto flutuante:', 10 + n + 8 * (n - 2))

gs_res2, gs_iters2 = gauss_seidel(rel, criteria**2, np.zeros(50, dtype=float))

max_trunc = max(abs((gs_res - gs_res2) / gs_res2))

print('\nB5:')
print('Truncamento máximo:', max_trunc)
