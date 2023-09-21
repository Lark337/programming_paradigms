import numpy as np

n1 = np.random.randint(0, 10, 10)
n2 = np.random.randint(0, 10, 10)
r = np.corrcoef(n1, n2)[0,1]
r2 = np.corrcoef([10,20,39],[15,16,28])[0,1]
print(r)
print(r2)