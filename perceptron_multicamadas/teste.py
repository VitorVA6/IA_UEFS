import math
import numpy as np

a = np.array([[0, 1, 2], [2, 2, 2]])
b = np.array([2,2,2])
np.insert(b, 0, -1)
print(b)