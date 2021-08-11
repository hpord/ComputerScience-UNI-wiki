import numpy as np
from numpy.linalg import matrix_power
a=np.array([[1/3,0,2/3],
            [1/2,1/2,0], 
            [1/6,1/3,1/2]])

print(matrix_power(a,4))