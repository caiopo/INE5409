import numpy as np

x = np.arange(100).reshape((10, 10))

print(x)

i = 5

s = sum(x[i][:i]) + sum(x[i][i + 1:len(x)])

print(x[i])
print(x[i][:i])
print(x[i][i + 1:len(x)])
print()
print(sum(x[i]) - x[i][i])
print(s)
