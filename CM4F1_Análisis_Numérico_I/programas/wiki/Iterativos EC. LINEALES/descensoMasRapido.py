import numpy as np
from numpy import linalg as LA
import time

def is_pos_def(x):
    """check if a matrix is symmetric positive definite"""
    return np.all(np.linalg.eigvals(x) > 0)

def steepest_descent(A, b, x):
    """
    Solve Ax = b
    Parameter x: initial values
    """
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matrix A needs to be symmetric positive definite (SPD)')
    r = b - A @ x
    k = 0
    print("\nValues de 'x' in the iteracion...\n")
    iteration = 1
    while LA.norm(r) > 1e-10 :
        p = r
        q = A @ p
        alpha = (p @ r) / (p @ q)
        x = x + alpha * p
        r = r - alpha * q
        k =+ 1

        print(" {}: ".format(iteration), end=" ")
        print(x, end="\n")
        iteration += 1

    return x

if __name__ == '__main__':

    A = np.array([[9.0, -2.0, 0.0], [-2.0, 4.0, -1.0], [0.0, -1.0, 1.0]])
    b = np.array([5.0, 1.0, -0.833])

    initial = np.array([0.0, 0.0, 0.0])

    start1 = time.time()
    result = steepest_descent(A, b, x=initial)
    done1 = time.time()
    elapsed1 = done1 - start1


    print("\n\nResult final:  {}".format(result))
    print("Time total: {} seg".format(elapsed1), end="\n\n")