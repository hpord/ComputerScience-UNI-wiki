import numpy as np
from numpy import linalg as LA
import time

def is_pos_def(x):
    """check if a matrix is symmetric positive definite"""
    return np.all(np.linalg.eigvals(x) > 0)
    
def conjugate_gradient(A, b):
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matrix A needs to be symmetric positive definite (SPD)')
    r = b 
    k = 0
    x = np.zeros(A.shape[-1])

    print("\nValues de 'x' in the iteracion...\n")
    iteration = 1

    while LA.norm(r) > 1e-10 :
        if k == 0:
            p = r
        else: 
            gamma = - (p @ A @ r)/(p @ A @ p)
            p = r + gamma * p
        alpha = (p @ r) / (p @ A @ p)
        x = x + alpha * p
        r = r - alpha * (A @ p)
        k =+ 1

        print(" {}: ".format(iteration), end=" ")
        print(x, end="\n")
        iteration += 1

    return x

if __name__ == '__main__':

    A = np.array([[9.0, -2.0, 0.0], [-2.0, 4.0, -1.0], [0.0, -1.0, 1.0]])
    b = np.array([5.0, 1.0, -0.833])


    start1 = time.time()
    result = conjugate_gradient(A, b)
    done1 = time.time()
    elapsed1 = done1 - start1


    print("\n\nResult final:  {}".format(result))
    print("Time total: {} seg".format(elapsed1), end="\n\n")
    