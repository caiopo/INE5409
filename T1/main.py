from matrix import create_complete_matrix, create_tridiagonal_matrix
from lu_crout import lu_crout, residuo
from gauss_tridiagonal import gauss_tridiagonal
from gauss_seidel import gauss_seidel, converges

import numpy as np

n = 50  # Tamanho da matriz (n*n)

# ------ Questão A ------

A, b = create_complete_matrix(n)

luc_ans = lu_crout(A, b)
luc_res = residuo(A, b, luc_ans)
luc_max_res = max(abs(luc_res))
luc_num_ops = (4 * n**3 + 15 * n**2 - 7 * n - 6) // 6

print('Questão A (LU-Crout)')
print('\nA2:')
print('Primeira incógnita:', luc_ans[0])
print('Última incógnita:', luc_ans[-1])
print('Resíduo máximo:', luc_max_res)

print('\nA3:')
print('Operações em ponto flutuante:', luc_num_ops)


# ------ Questão B ------

t, r, d, b = create_tridiagonal_matrix(n)

gtrid_ans = gauss_tridiagonal(t, r, d, b)
gtrid_res = residuo(A, b, gtrid_ans)
gtrid_max_res = max(abs(gtrid_res))
gtrid_num_ops = 8 * n - 7

print('\n\n\nQuestão B (Gauss Otimizado)')

print('\nB2:')
print('Primeira incógnita:', gtrid_ans[0])
print('Última incógnita:', gtrid_ans[-1])
print('Resíduo máximo:', gtrid_max_res)

print('\nB3:')
print('Operações em ponto flutuante:', gtrid_num_ops)


# ------ Questão C ------

print('\n\n\nQuestão C (Gauss-Seidel)')

print('\nC1:')
if converges(A):
    print('O sistema possui diagonal dominante e sempre irá convergir.\n'
          'Podemos acelerar o cálculo usando um fator de sobrerrelaxação.')
else:
    print('O sistema não possui diagonal dominante e '
          'talvez não venha a convergir')

print('\nC2:')
criteria = 1e-4

print('Critério de parada utilizado: {}'.format(criteria))
print('Para encontrar o fator de relaxação que faz '
      'a função convergir mais rapidamente vamos buscar '
      'entre 0.1 e 1.9:')

factors = []

for rel in range(1, 20):
    _, c = gauss_seidel(rel / 10, criteria, n)
    print('Fator =', rel / 10, '| Iterações =', c)

    factors.append((c, rel))

min_iters, rel = min(factors)

rel /= 10

print('Podemos ver que fator de relaxação que '
      'converge mais rápido é {}, com {} iterações'.format(rel, min_iters))

print('\nC3:')
gs_ans, gs_num_iters = gauss_seidel(rel, criteria, n)

gs_res = residuo(A, b, gs_ans)
gs_max_res = max(abs(gs_res))

gs_num_ops = 346 * gs_num_iters

print('Primeira incógnita:', gs_ans[0])
print('Última incógnita:', gs_ans[-1])
print('Resíduo máximo:', gs_max_res)

print('\nC4:')
print('Número de iterações:', gs_num_iters)
print('Número de operações de ponto flutuante:', gs_num_ops)

gs_ans2, _ = gauss_seidel(rel, criteria**2, n)

max_trunc = max(abs((gs_ans - gs_ans2) / gs_ans2))

print('\nC5:')
print('Truncamento máximo:', max_trunc)


# ------ Questão D ------

print('\n\n\nQuestão D (Comparação)')

print('\nNúmero de operações em cada método:')
print('LU-Crout:', luc_num_ops)
print('Gauss Otimizado:', gtrid_num_ops)
print('Gauss-Seidel:', gs_num_ops)

if luc_num_ops <= gtrid_num_ops and luc_num_ops <= gs_num_ops:
    best_method = 'LU-Crout'

if gtrid_num_ops <= luc_num_ops and gtrid_num_ops <= gs_num_ops:
    best_method = 'Gauss Otimizado'

if gs_num_ops <= gtrid_num_ops and gs_num_ops <= luc_num_ops:
    best_method = 'Gauss-Seidel'

print('Para esse sistema, o método mais eficiente é', best_method)
