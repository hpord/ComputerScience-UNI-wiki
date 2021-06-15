import numpy as np
import os
import glob



def generate(n_matrix, base_number):

    files = glob.glob('./matrices/*.txt')
    for f in files:
        os.remove(f)

    print(f"\nmin size: {base_number}")
    print(f"max size: {base_number + n_matrix}")
    print(f"number de matrices: {n_matrix}", end="\n")

    for i in range(n_matrix):

        size_matrix = base_number + (i+1)
        array = np.random.randint(low=1, high=35, size=(size_matrix, size_matrix))
        
        array_symm = np.maximum(array, array.transpose())

        np.fill_diagonal(array_symm, 0)

        np.savetxt(f'./matrices/matrix_{size_matrix}.txt', array_symm.astype(int), delimiter=',')

if __name__ == '__main__':
    generate(n_matrix=7, base_number=2)