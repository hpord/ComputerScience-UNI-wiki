import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
  """
  This is an implementation of the pseduo-code provided in the Wikipedia article.
  Inputs:
    A: nxn numpy matrix
    b: n dimensional numpy vector
    omega: relaxation factor
    initial_guess: An initial solution guess for the solver to start with
  Returns:
    phi: solution vector of dimension n
  """
  phi = initial_guess[:]
  residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
  while residual > convergence_criteria:
    for i in range(A.shape[0]):
      sigma = 0
      for j in range(A.shape[1]):
        if j != i:
          sigma += A[i][j] * phi[j]
          
      phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
    print(phi, end="\n")
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    print('Residuo: {0:10.6g}'.format(residual))
  return phi


if __name__ == '__main__':

    #An example case that mirrors the one in the Wikipedia article
    residual_convergence = 1e-8
    omega = 1.2 #Relaxation factor

    A = np.ones((3, 3))
    A[0][0] = 9
    A[0][1] = -2
    A[0][2] = 0

    A[1][0] = -2
    A[1][1] = 4
    A[1][2] = -1

    A[2][0] = 0
    A[2][1] = -1
    A[2][2] = 1


    b = np.ones(3)
    b[0] = 5.0
    b[1] = 1.0
    b[2] = -5.0/6.0

    initial_guess = np.zeros(3)

    phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
    print(phi)