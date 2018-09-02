from matrix import create_matrix
from lu_crout import lu_crout, residuo

import numpy as np

n = 50  # Tamanho da matriz (n*n)

A, b = create_matrix(n)

luc_ans = lu_crout(A, b)
luc_res = residuo(A, b, luc_ans)
luc_max_res = max(abs(luc_res))

print('Questão A:')
print('Primeira incógnita:', luc_ans[0])
print('Última incógnita:', luc_ans[-1])
print('Resíduo máximo:', luc_max_res)
print('Operações em ponto flutuante:', (4 * n**3 + 15 * n**2 - 7 * n - 6) // 6)
