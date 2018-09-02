from matrix import create_complete_matrix, create_tridiagonal_matrix
from lu_crout import lu_crout, residuo
from gauss_tridiagonal import gauss_tridiagonal

import numpy as np

n = 50  # Tamanho da matriz (n*n)

# ------ Questão A ------

A, b = create_complete_matrix(n)

luc_ans = lu_crout(A, b)
luc_res = residuo(A, b, luc_ans)
luc_max_res = max(abs(luc_res))

print('Questão A:')
print('Primeira incógnita:', luc_ans[0])
print('Última incógnita:', luc_ans[-1])
print('Resíduo máximo:', luc_max_res)
print('Operações em ponto flutuante:', (4 * n**3 + 15 * n**2 - 7 * n - 6) // 6)


# ------ Questão B ------

t, r, d, b = create_tridiagonal_matrix(n)

gtrid_ans = gauss_tridiagonal(t, r, d, b)
gtrid_res = residuo(A, b, gtrid_ans)
gtrid_max_res = max(abs(gtrid_res))

print('\nQuestão B:')
print('Primeira incógnita:', gtrid_ans[0])
print('Última incógnita:', gtrid_ans[-1])
print('Resíduo máximo:', gtrid_max_res)
print('Operações em ponto flutuante:', 8 * n - 7)
