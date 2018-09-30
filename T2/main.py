from math import exp

from newton import newton, residue


def f1(x):
    return x * x * x - exp(x)


roots1 = newton(f1, -10, 10)
res1 = residue(f1, roots1)

print('Questão 1')

for i, (root, res) in enumerate(zip(roots1, res1)):
    print('raiz{} = {}, resíduo = {}'.format(i, root, res))

