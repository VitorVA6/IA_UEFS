import math
import numpy as np

a = np.array([1, 1, 0])
b = np.around([0.9999, 0.888, 0.2222])
if np.array_equal(a, b):
    print('aehoooo')
else:
    print('ops')