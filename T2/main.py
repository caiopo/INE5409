from math import exp

from newton_geral import newton_geral, residuo


# ------ Questão 1 ------

def f1(x):
    return x * x * x - exp(x)


def f1_second_derivative(x):
    return 6 * x - exp(x)


roots1 = newton_geral(f1, -10, 10)
res1 = residuo(f1, roots1)

print('Questão 1')

for i, (root, res) in enumerate(zip(roots1, res1)):
    print('raiz{} = {}, resíduo = {}'.format(i, root, res))

descontinuidades = newton_geral(f1_second_derivative, -10, 10)

print('Os pontos de descontinuidade são:', descontinuidades)


# ------ Questão 2 ------

print('\n\nQuestão 2')
