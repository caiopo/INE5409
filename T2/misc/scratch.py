import numpy as np

x = np.arange(1, 10, dtype=float)

x[4], x[8] = (1.4, 1.8)

print(x)
