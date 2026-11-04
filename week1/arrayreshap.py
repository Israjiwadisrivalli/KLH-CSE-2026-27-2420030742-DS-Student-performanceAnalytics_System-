import numpy as np
n=np.array([1,2,3,4,5,6])
print(n.shape)
print(n.reshape(2,3))
print(n.reshape(3,2))
n.reshape(-1)