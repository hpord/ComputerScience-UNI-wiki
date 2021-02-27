import numpy as np

# Epsilon_Mach
#   return: Machine epsilon
def Epsilon_Mach():
	eps = 1.0
	while eps + 1.0 > 1.0:
		epsilon = eps
		eps = 0.5*eps
	return epsilon

# Pivot_mat
    # A: Matrix for pivoting
    # c_index: column index (generally) where we apply de pivoting

    # return: permutation matrix 'P'
def Pivot_mat(A, c_index):
    dim = A.shape[0]
    P = np.eye(dim)

    index = c_index
    for i in range(c_index + 1, dim):
        if abs(A[i,c_index]) > abs(A[index,c_index]):
            index = i

    if index != c_index:
        P[[index, c_index]] = P[[c_index, index]]

    return P

# back_solve_triangular
    # A: Coef. matrix
    # b: solutions vector

    # return: solutions vector x from backward evaluations
def back_solve_triangular(A, b, verbose=False):
    x = np.empty(A.shape[1])
    rows = A.shape[0]
    for i in range(rows-1, -1, -1):
        pre_sum = A[i, i+1:].dot(x[i+1:])
        x[i] = (b[i] - pre_sum)/A[i,i]
        # ========================================
        if verbose:
            print("x_{}".format(i+1))
            print(x[i])
            print("========================")
        # ========================================
    # ========================================
    if verbose:
        print("x")
        print(x)
        print("========================")
    # ========================================
    return x

# for_solve_triangular
    # A: Coef. matrix
    # b: solutions vector

    # return: solutions vector x from forward evaluations
def for_solve_triangular(A,b, verbose=False):
    x = np.zeros(A.shape[1])
    rows = A.shape[0]
    for i in range(0, rows):
        if i == 0:
            x[0] = b[0]/A[0,0]
        else:
            pre_sum = A[i,0:i].dot(x[0:i])
            x[i] = (b[i] - pre_sum)/A[i,i]
        # ========================================
        if verbose:
            print("x_{}".format(i+1))
            print(x[i])
            print("========================")
        # ========================================
    # ========================================
    if verbose:
        print("x")
        print(x)
        print("========================")
    # ========================================
    return x

def solve_tridiagonal(A, b_0, verbose=False):
	a = np.copy(np.diag(A, k=-1))
	b = np.copy(np.diag(A))
	c = np.copy(np.diag(A, k=1))
	d = np.copy(b_0)

	n = len(d) # n is the numbers of rows, a and c has length n-1
	for i in range(n-1):
		d[i+1] -= 1. * d[i] * a[i] / b[i]
		b[i+1] -= 1. * c[i] * a[i] / b[i]
	for i in reversed(range(n-1)):
		d[i] -= d[i+1] * c[i] / b[i+1]
	return [d[i] / b[i] for i in range(n)]


# decompose
    # A: Matrix

    # return: 	D = Diagonal matrix from A,
	#			E: negative of l.tri. matrix from A (no diag),
	#			F: negative of u.tri. matrix from A (no diag)
def decompose(A, verbose=False):
	E = -np.tril(A, -1)
	F = -np.triu(A, 1)
	D = np.diag(A.diagonal())
	if verbose:
		print("D: \n", D)
		print("E: \n", E)
		print("F: \n", F)

	return D,E,F

# Gauss
    # A: Coef. matrix
    # b: Results matrix
    # verbose: printing flag
    # pivot: Pivoting criteria
    # lu: Asks if return L and U matrices from decomposition

    # return: X vector of solutions
def Gauss(A, b, verbose=False, pivot="none"):
    A_save = A
    A_b = np.matrix(np.c_[A, b]) # Augmented matrix
    n_row, n_col = A_b.shape[0], A_b.shape[1]
    process_string = "A_b"

    P = np.eye(n_row)
    L = np.eye(n_row)

    # ========================================
    if verbose:
        print("Matriz aumentada al inicio:")
        print(A_b)
        print("========================")
    # ========================================


    for i in range(0, n_row-1): # Main loop
        # Gauss matrices preparation
        P_i = np.eye(n_row)
        L_i = np.eye(n_row)

        if (A_b[i,i] == 0 and pivot == "partial") or pivot=="total":
            P_i = Pivot_mat(A_b, i)

        # ========================================
        if verbose:
            print("P_{}".format(i+1))
            print(P_i)
            print("========================")
        # ========================================

        # Apply permutation
        A_b = np.matmul(P_i,A_b)
        P = np.matmul(P_i, P)
        L = np.matmul(P_i, L)

        # ========================================
        if verbose:
            process_string = "P_{}.".format(i+1) + process_string
            print(process_string)
            print(A_b)
            print("========================")
        # ========================================

        # Preparing alpha_i
        alpha_i = np.zeros(n_row)
        alpha_i[i+1:] = np.transpose(A_b[i+1:n_row,i])/A_b[i,i]

        # ========================================
        if verbose:
            print("alpha_{}".format(i+1))
            print(alpha_i)
            print("========================")
        # ========================================

        # Preparing e_i
        e_i = np.zeros(n_row)
        e_i[i] = 1

        # Calc. L_i
        L_i = np.eye(n_row) - np.outer(alpha_i, e_i)
        L = np.matmul(L_i, L)

        # ========================================
        if verbose:
            print("L_{}".format(i+1))
            print(L_i)
            print("========================")
        # ========================================

        # Transform system
        A_b = np.matmul(L_i,A_b)
        # ========================================
        if verbose:
            process_string = "L_{}.".format(i+1) + process_string
            print(process_string)
            print(A_b)
            print("========================")
        # ========================================

    # Final calculus of LU matrices
    U = A_b[:,:n_col-1]
    L = np.linalg.inv(np.matmul(L, np.linalg.inv(P)))

    # ========================================
    if verbose:
        print("Ab final (Gauss)")
        print(A_b)
        print("========================")
        print("L final (Gauss)")
        print(L)
        print("========================")
        print("U final (Gauss)")
        print(U)
        print("========================")
    # ========================================

    return P, L, U

# Gauss-Jordan
    # A: Coef. matrix
    # b: Results matrix
    # verbose: printing flag
    # pivot: Pivoting criteria

    # return: X vector of solutions
def Gauss_Jordan(A, b, verbose=False, pivot="none"):
    A_b = np.matrix(np.c_[A, b]) # Augmented matrix
    n_row, n_col = A_b.shape[0], A_b.shape[1]
    process_string = "A_b"

    # ========================================
    if verbose:
        print("Matriz aumentada al inicio:")
        print(A_b)
        print("========================")
    # ========================================


    for i in range(0, n_row): # Main loop
        # Gauss matrices preparation
        P_i = np.eye(n_row)
        T_i = np.eye(n_row)

        if (A_b[i,i] == 0 and pivot == "partial") or pivot=="total":
            P_i = Pivot_mat(A_b, i)

        # ========================================
        if verbose:
            print("P_{}".format(i+1))
            print(P_i)
            print("========================")
        # ========================================

        # Apply permutation
        A_b = np.matmul(P_i,A_b)

        # ========================================
        if verbose:
            process_string = "P_{}.".format(i+1) + process_string
            print(process_string)
            print(A_b)
            print("========================")
        # ========================================

        # Preparing alpha_i
        alpha_i = np.empty(n_row)
        alpha_i[:] = (A_b[:,i].T/A_b[i,i])
        alpha_i[i] = 1/A_b[i,i]

        # ========================================
        if verbose:
            print("alpha_{}".format(i+1))
            print(alpha_i)
            print("========================")
        # ========================================

        # Preparing e_i
        e_i = np.zeros(n_row)
        e_i[i] = 1

        # Calc. L_i
        T_i = np.eye(n_row) - np.outer(alpha_i, e_i)

        # ========================================
        if verbose:
            print("T_{}".format(i+1))
            print(T_i)
            print("========================")
        # ========================================

        # Transform system
        A_b = np.matmul(T_i,A_b)
        # ========================================
        if verbose:
            process_string = "T_{}.".format(i+1) + process_string
            print(process_string)
            print(A_b)
            print("========================")
        # ========================================

    # ========================================
    if verbose:
        print("Ab final (Gauss-Jordan)")
        print(A_b)
        print("========================")
    # ========================================
    return back_solve_triangular(A_b[:,:n_col-1],A_b[:,n_col-1], verbose)

# Inverse
    # A: Matrix
    # verbose: printing flag

    # return: Matrix A^-1 inverse of A
def Inverse(A, verbose=False):
    n_row, n_col = A.shape[0], A.shape[1]
    if n_row != n_col or np.linalg.det(A) == 0:
        print("Singular matrix or dimensions error")
        return
    process_string = "A"
    cp = A
    A_inv = np.eye(n_row)

    # ========================================
    if verbose:
        print("Matriz al inicio:")
        print(A)
        print("========================")
    # ========================================


    for i in range(0, n_row): # Main loop
        # Gauss matrices preparation
        T_i = np.eye(n_row)

        # Preparing alpha_i
        alpha_i = np.empty(n_row)
        alpha_i[:] = (A[:,i].T/A[i,i])
        alpha_i[i] = 1/A[i,i]

        # Preparing e_i
        e_i = np.zeros(n_row)
        e_i[i] = 1

        # Calc. L_i
        T_i = np.eye(n_row) - np.outer(alpha_i, e_i)
        # Gauss-Jordan variation to calculate inverse, forcing T-tilde[i,i] = 1/A[i,i]
        T_i[i,i] = 1/A[i,i]

        # ========================================
        if verbose:
            print("T-tilde_{}".format(i+1))
            print(T_i)
            print("========================")
        # ========================================

        # Transform system
        A = np.matmul(T_i, A)
        A_inv = np.matmul(T_i, A_inv)
        # ========================================
        if verbose:
            process_string = "T-tilde_{}.".format(i+1) + process_string
            print(process_string)
            print(A)
            print("========================")
        # ========================================

    # ========================================
    if verbose:
        print("Resultado de la inversión:")
        print(A_inv)
        print("========================")
    # ========================================
    return A_inv

# LU Decomposition: Direct crout method 1
#   A: Matrix in which we apply LU_1 decomp.
#   return: P, L, U matrices
def LU_1(A, verbose=False, pivot="none"):
    dim = A.shape[0]

    if(dim != A.shape[0]):
        print("Error. 'A' matriz no cuadrada")
        return

    process_string = "A"

    # ========================================
    if verbose:
        print("Matriz A al principio")
        print(A)
        print("========================")
    # ========================================

    P = np.eye(dim)
    L = np.zeros((dim, dim))
    U = np.eye(dim)

    for k in range(0, dim):
        P_k = np.eye(dim)

        if (A[k,k] == 0 and pivot == "partial") or pivot=="total":
            P_k = Pivot_mat(A, k)

        # ========================================
        if verbose:
            print("P_{}".format(k+1))
            print(P_k)
            print("========================")
        # ========================================

        A = np.matmul(P_k, A)
        P = np.matmul(P_k, P)
        # ========================================
        if verbose:
            process_string = "P_{}.".format(k+1) + process_string
            print(process_string)
            print(A)
            print("========================")
        # ========================================

    for k in range(0, dim):
        # l_ik
        for i in range(k, dim): # rows iteration
            pre_sum = L[i,0:k].dot(U[0:k,k])
            L[i,k] = A[i,k] - pre_sum

        # ========================================
        if verbose:
            print("L_{}".format(k+1))
            print(L)
            print("========================")
        # ========================================

        # u_kj
        for j in range(k+1, dim): # cols iteration
            pre_sum = L[k,0:k].dot(U[0:k, j])
            U[k,j] = (A[k,j] - pre_sum)/L[k,k]

        # ========================================
        if verbose:
            print("U_{}".format(k+1))
            print(U)
            print("========================")
        # ========================================

    # ========================================
    if verbose:
        print("P final:")
        print(P)
        print("========================")
        print("L final:")
        print(L)
        print("========================")
        print("U final:")
        print(U)
        print("========================")
    # ========================================
    return P,L,U

# LU Decomposition: Direct crout method 2
#   A: Matrix in which we apply L_1U decomp.
#   return: P, L, U matrices
def L_1U(A, verbose=False, pivot="none"):
    dim = A.shape[0]

    if(dim != A.shape[0]):
        print("Error. 'A' matriz no cuadrada")
        return

    process_string = "A"

    # ========================================
    if verbose:
        print("Matriz A al principio")
        print(A)
        print("========================")
    # ========================================

    P = np.eye(dim)
    L = np.eye(dim)
    U = np.zeros((dim, dim))

    for k in range(0, dim):
        P_k = np.eye(dim)

        if (A[k,k] == 0 and pivot == "partial") or pivot=="total":
            P_k = Pivot_mat(A, k)

        # ========================================
        if verbose:
            print("P_{}".format(k+1))
            print(P_k)
            print("========================")
        # ========================================

        A = np.matmul(P_k, A)
        P = np.matmul(P_k, P)
        # ========================================
        if verbose:
            process_string = "P_{}.".format(k+1) + process_string
            print(process_string)
            print(A)
            print("========================")
        # ========================================

    for k in range(0, dim):
        # l_ik
        for j in range(k, dim): # rows iteration
            pre_sum = L[k,0:k].dot(U[0:k,j])
            U[k,j] = A[k,j] - pre_sum

        # ========================================
        if verbose:
            print("U_{}".format(k+1))
            print(U)
            print("========================")
        # ========================================

        # u_kj
        for i in range(k+1, dim): # cols iteration
            pre_sum = L[i,0:k].dot(U[0:k, k])
            L[i,k] = (A[i,k] - pre_sum)/U[k,k]

        # ========================================
        if verbose:
            print("L_{}".format(k+1))
            print(L)
            print("========================")
        # ========================================

    # ========================================
    if verbose:
        print("P final:")
        print(P)
        print("========================")
        print("L final:")
        print(L)
        print("========================")
        print("U final:")
        print(U)
        print("========================")
    # ========================================
    return P,L,U

# LDLt
#   A: Simetric matrix in which we apply LDLt decomp
#   verbose: printing flag
#   pivot: Pivoting criteria
#
#   return: P, L, D matrices such that PAPt = LDLt

def LDLt(A, verbose=False, pivot="none"):
	n = A.shape[0]
	P = np.eye(n)
	L = np.eye(n)
	D = np.zeros(n)
	process_string = "A"

	eig_values = np.linalg.eig(A)[0]
	for i in eig_values:
	    if i < 0:
	        print("(LDLt) Error: matriz no definida positiva")
	        return

	for k in range(0, n):
	    P_k = np.eye(n)

	    if (A[k,k] == 0 and pivot == "partial") or pivot=="total":
	        P_k = Pivot_mat(A, k)

	    # ========================================
	    if verbose:
	        print("P_{}".format(k+1))
	        print(P_k)
	        print("========================")
	    # ========================================

	    A = np.matmul(P_k, A)
	    A = np.matmul(A, P_k.T)
	    P = np.matmul(P_k, P)

	    # ========================================
	    if verbose:
	        process_string = "P_{}.".format(k+1) + process_string + ".P^T_{}".format(k+1)
	        print(process_string)
	        print(A)
	        print("========================")
	    # ========================================

	    pre_sum = 0
	    for v in range(0, k):
	        pre_sum += D[v]*(L[k, v])**2
	    D[k] = A[k,k] - pre_sum

	    for i in range(k+1, n):
	        pre_sum_2 = 0
	        for v in range(0, k):
	            pre_sum_2 += L[i, v]*D[v]*L[k, v]

	        L[i,k] = (A[i,k] - pre_sum_2)/D[k]

	    # ========================================
	    if verbose:
	        print("D_{}.".format(k+1))
	        print(D)
	        print("========================")
	    # ========================================

	    # ========================================
	    if verbose:
	        print("L_{}.".format(k+1))
	        print(L)
	        print("========================")
	    # ========================================

	# ========================================
	if verbose:
		print("P")
		print(P)
		print("========================")
		print("L")
		print(L)
		print("========================")
		print("D")
		print(np.diag(D))
		print("========================")
    # ========================================
	return P, L, np.diag(D)

# Cholesky
#   A: Simetric matrix in which we apply Cholesky decomp
#   verbose: printing flag
#   pivot: Pivoting criteria
#
#   return: G lower triangular matrix
def Cholesky(A, verbose=False, pivot="none"):
	eig_values = np.linalg.eig(A)[0]
	n = A.shape[0]
	G = np.zeros((n,n))
	P = np.eye(n)
	process_string = "A"

	for i in eig_values:
	    if i < 0:
	        print("(Cholesky) Error: matriz no definida positiva")
	        return

	for k in range(0, n):
		P_k = np.eye(n)

		if (A[k,k] == 0 and pivot == "partial") or pivot=="total":
			P_k = Pivot_mat(A, k)

		# ========================================
		if verbose:
		    print("P_{}".format(k+1))
		    print(P_k)
		    print("========================")
		# ========================================

		A = np.matmul(P_k, A)
		A = np.matmul(A, P_k.T)
		P = np.matmul(P_k, P)

		# ========================================
		if verbose:
			process_string = "P_{}.".format(k+1) + process_string + ".P^T_{}".format(k+1)
			print(process_string)
			print(A)
			print("========================")
	    # ========================================


		pre_sum = G[k, 0:k].dot(G[k, 0:k])
		G[k,k] = np.sqrt(A[k,k] - pre_sum)

		for i in range(k+1, n):
		    pre_sum_2 = G[i, 0:k].dot(G[k,0:k])
		    G[i,k] = (A[i,k] - pre_sum_2)/G[k,k]

		# ========================================
		if verbose:
		    print("G_{}.".format(k+1))
		    print(G)
		    print("========================")
# ========================================

	return P, G

# Pivot_mat_pr
    # A: Matrix for pivoting with Parlett-Reid criteria
    # c_index: column index (generally) where we apply de pivoting

    # return: permutation matrix 'P'
def Pivot_mat_pr(A, c_index):
    dim = A.shape[0]
    P = np.eye(dim)

    index = c_index + 1
    for i in range(c_index + 2, dim):
        if abs(A[i,c_index]) > abs(A[index,c_index]):
            index = i

    if index != c_index + 1:
        P[[index, c_index + 1]] = P[[c_index + 1, index]]

    return P

# Cholesky
#   A: Simetric matrix in which we apply Parlett & Reid decomp
#   verbose: printing flag
#   pivot: Pivoting criteria
#
#   return: P: permutation matrix, L: Lower triangular matrix, T: tridiagoinal matrix as PAP^t = LTL^t
def Parlett_Reid(A, verbose=False, pivot="none"):
    n_row, n_col = A.shape[0], A.shape[1]

    P = np.eye(n_row)
    L = np.eye(n_row)
    T = np.eye(n_row)

    process_string = "A"

    for k in range(0, n_row-2):
        P_k = np.eye(n_row)

        if (A[k,k] == 0 and pivot == "partial") or pivot=="total":
            P_k = Pivot_mat_pr(A, k)
        # ========================================
        if verbose:
            print("P_{}".format(k+1))
            print(P_k)
            print("========================")
        # ========================================
        A = np.matmul(P_k, A)
        A = np.matmul(A, P_k.T)

        P = np.matmul(P_k, P)
        L = np.matmul(P_k, L)

        # ========================================
        if verbose:
            process_string = "P_{}.".format(k+1) + process_string + ".P_{}^T".format(k+1)
            print(process_string)
            print(A)
            print("========================")
        # ========================================

        # Preparing alpha_i
        alpha_k = np.zeros(n_row)
        alpha_k[k+2:] = (A[k + 2:n_row,k].T/A[k + 1,k])

        # ========================================
        if verbose:
            print("alpha_{}".format(k+1))
            print(alpha_k)
            print("========================")
        # ========================================

        # Preparing e_i
        e_k = np.zeros(n_row)
        e_k[k+1] = 1

        # Calc. L_i
        M_k = np.eye(n_row) - np.outer(alpha_k, e_k)

        # ========================================
        if verbose:
            print("M_{}".format(k+1))
            print(M_k)
            print("========================")
        # ========================================

        # Transform system
        A = np.matmul(M_k, A)
        A = np.matmul(A, M_k.T)
        L = np.matmul(M_k, L)

        # ========================================
        if verbose:
            process_string = "M_{}.".format(k+1) + process_string +".M_^T{}".format(k+1)
            print(process_string)
            print(A)
            print("========================")
        # ========================================

    T = A
    L = np.linalg.inv(np.matmul(L, P.T))
    # ========================================
    if verbose:
        print("A final")
        print(A)
        print("========================")
    # ========================================
    return P, L, T

def Cond_number(A, norm, verbose=False):
	A_inv = Inverse(A, verbose)
	# ========================================
	if verbose:
	    print("A_^-1")
	    print(A_inv)
	    print("========================")
	# ========================================
	cond_number = np.linalg.norm(A, norm)*np.linalg.norm(A, norm)
	# ========================================
	if verbose:
	    print("Numero de condicion:")
	    print(cond_number)
	    print("========================")
	# ========================================
	return cond_number

def Cond_interval(A, x_tilde, b, norm, verbose=False):
    R = np.matmul(A, x_tilde) - b
    R_norm = np.linalg.norm(R, norm)
    # ========================================
    if verbose:
        print("R")
        print(R)
        print("========================")
        print("||R||")
        print(R_norm)
        print("========================")
    # ========================================
    b_norm = np.linalg.norm(b, norm)
    # ========================================
    if verbose:
        print("b")
        print(b)
        print("========================")
        print("||b||")
        print(b_norm)
        print("========================")
    # ========================================
    cond_A = Cond_number(A, norm, verbose)
    # ========================================
    if verbose:
        print("b")
        print(b)
        print("========================")
        print("||b||")
        print(b_norm)
        print("========================")
    # ========================================
    inf = R_norm/(b_norm*cond_A)
    sup = cond_A*R_norm/b_norm
    # ========================================
    if verbose:
        print("Cota de error")
        print("[{};{}]".format(inf, sup))
        print("========================")
    # ========================================
    return inf, sup

# Gram_Schmidt
#   A: Matrix in which we apply Gram Schmidt decomp
#   verbose: printing flag
#   pivot: Pivoting criteria
#
#   return: E, U such like A = EU
def Gram_Schmidt(A, verbose=False):
	n_row, n_col = A.shape[0], A.shape[1]
	E = np.zeros((n_row, n_col))
	U = np.zeros((n_col, n_col))

	n_row, n_col = A.shape[0], A.shape[1]

	for j in range(0,n_col):
		E[:, j] = A[:, j]

		if j > 1:
			for i in range(0, j-1):
				U[i,j] = E[:, i].dot(A[:, j])
				E[:, j] = E[:, j] -  U[i,j]*E[:, i]
		U[j,j] = np.sqrt(E[:, j].dot(E[:, j]))
		E[:, j] = E[:, j]/U[j,j]

		# ========================================
		if verbose:
			print("E en iter {}:".format(j))
			print(E)
			print("========================")
			print("U en iter {}:".format(j))
			print(U)
			print("========================")
	    # ========================================

	# ========================================
	if verbose:
		print("E final:")
		print(E)
		print("========================")
		print("U final:")
		print(U)
		print("========================")
	# ========================================
	return E, U


# HouseHolder
#	A: Matrix to wich Householder factorization is applied
#	return: Q, R Matrices so A = Q.R, Q:Orthogonal
def Householder(A, verbose=False):
	n_row, n_col = A.shape[0], A.shape[1]
	A_k = np.copy(A)
	n_row_k, n_col_k = A_k.shape[0], A_k.shape[1]
	R = np.zeros((n_row, n_col))
	Q = np.eye(n_row)

	# ========================================
	if verbose:
		print("=========================================")
		print("DESCOMPOSICION QR - HOUSEHOLDER")
		print("=========================================")
	# =========================================

	for k in range(0, n_col):
		# ========================================
		if verbose:
			print("-----------A_{}:-----------\n{}".format(k, A_k))
		# ========================================
		current_col = np.asmatrix(A_k[:, 0]).T

		e_k = np.asmatrix(np.repeat(0, A_k.shape[0])).T
		e_k[0,0] = 1

		w = np.sign(current_col[0,0])*np.linalg.norm(current_col, 2)*e_k + current_col
		if np.linalg.norm(w, 2) != 0:
			w = w/np.linalg.norm(w, 2)
		# ========================================
		if verbose:
			print("w_{}\n{}".format(k, w))
		# ========================================
		H_k = np.eye(A_k.shape[0]) - 2*np.matmul(w, w.T)
		# ========================================
		if verbose:
			print("H_{}\n{}".format(k, expandedMat(H_k, k)))
		# ========================================
		Q = np.matmul(expandedMat(H_k, k), Q)

		HxA = np.matmul(H_k, A_k)
		R[k:n_row,k:n_col] = np.copy(HxA)
		# ========================================
		if verbose:
			print("R_{}\n{}".format(k, R))
		# ========================================
		A_k = np.empty((n_row_k-1, n_col_k-1))
		A_k[:,:] = R[k+1:,k+1:]
		n_row_k -= 1
		n_col_k -= 1

	# ========================================
	if verbose:
		print("Q final:\n{}".format(Q.T))
		print("R final:\n{}".format(R))
	# ========================================
	return Q.T, R

def expandedMat(A, n):
	A_exp = np.copy(A)
	upper_expand = np.zeros((n,A.shape[1]))
	left_expand = np.vstack((np.eye(n), np.zeros((A.shape[0],n))))
	A_exp = np.r_[upper_expand, A_exp]
	A_exp = np.c_[left_expand, A_exp]
	return np.asmatrix(A_exp)


# Factorizacion A = QR mediante Matrices de rotacion de Givens
def Givens(A, verbose=False):
	# ========================================
	if verbose:
		print("=========================================")
		print("DESCOMPOSICION QR - GIVENS")
		print("=========================================")
	# =========================================

	new_A = np.copy(A)
	n = A.shape[0]
	Q = np.eye(n)

	for col in range(A.shape[1]):
		for row in range(A.shape[0] - 1, -1, -1):
			if row > col:
				# ====================================
				if verbose:
					print("=======================")
					print("({}, {})".format(row, col))
					print("=======================")
				# ====================================

				G_matrix = np.eye(n)
				a = new_A[row-1,col]
				b = new_A[row,col]

				cos = a/(np.sqrt( a**2 + b**2 ))
				sen = b/(np.sqrt( a**2 + b**2 ))

				# ====================================
				if verbose:
					print("(cos, sen) = ({};{})".format(cos, sen))
				# ====================================

				G_matrix[row, row] = cos
				G_matrix[row, row-1] = sen
				G_matrix[row-1, row-1] = cos
				G_matrix[row-1, row] = -sen

				# ====================================
				if verbose:
					print("Matriz de Givens para (i,j)=({},{}):\n".format(row, col), G_matrix)
				# ====================================

				Q = np.matmul(G_matrix.T,Q)

				# ====================================
				if verbose:
					print("Matriz ingresada luego de la rotacion:\n",new_A)
				# ====================================

				new_A = np.matmul(G_matrix.T, new_A)
	R = np.copy(new_A)
	print("Matriz final: \n", R)
	print("Matriz Q (Producto de Matrices de Givens): \n", Q)
	return Q.T, R


# ===================================================
# Equation solving methods
# ===================================================

def solve_Gauss(A, b, verbose=False, pivot="none"):
	# ========================================
	if verbose:
		print("=========================================")
		print("METODO DE GAUSS")
		print("=========================================")
	#=========================================
	P, L, U = Gauss(A, b, verbose, pivot)
	# ========================================
	if verbose:
		print("De LUx = Pb, evaluamos Lz = Pb y Ux = z")
		print("1. Resolviendo Lz = Pb")
	# ========================================
	z = for_solve_triangular(L, np.matmul(P, b), verbose)
	# ========================================
	if verbose:
		print("z")
		print(z)
		print("2. Resolviendo Ux = z")
	# ========================================
	x = back_solve_triangular(U, z, verbose)
	# ========================================
	if verbose:
		print("x")
		print(x)
	# ========================================
	return x

def solve_Gauss_Jordan(A, b, verbose=False, pivot="none"):
	#=========================================
	if verbose:
		print("METODO DE GAUSS JORDAN")
	#=========================================
	return Gauss_Jordan(A, b, verbose, pivot)

def solve_LU_1(A, b, verbose=False, pivot="none"):
	#=========================================
	if verbose:
		print("METODO DE DESCOMPOSICION LU_1")
	#=========================================
	P, L, U = LU_1(A, verbose, pivot)
	# ========================================
	if verbose:
		print("De LUx = Pb, evaluamos Lz = Pb y Ux = z")
		print("1. Resolviendo Lz = Pb")
	# ========================================
	z = for_solve_triangular(L, np.matmul(P, b), verbose)
	# ========================================
	if verbose:
		print("z")
		print(z)
		print("2. Resolviendo Ux = z")
	# ========================================
	x = back_solve_triangular(U, z, verbose)
	# ========================================
	if verbose:
		print("x")
		print(x)
	# ========================================
	return x

def solve_L_1U(A, b, verbose=False, pivot="none"):
		#=========================================
		if verbose:
			print("=========================================")
			print("METODO DE DESCOMPOSICION L_1U")
			print("=========================================")
		#=========================================
		P, L, U = L_1U(A, verbose, pivot)
		# ========================================
		if verbose:
			print("De LUx = Pb, evaluamos Lz = Pb y Ux = z")
			print("1. Resolviendo Lz = Pb")
		# ========================================
		z = for_solve_triangular(L, np.matmul(P, b), verbose)
		# ========================================
		if verbose:
			print("z")
			print(z)
			print("2. Resolviendo Ux = z")
		# ========================================
		x = back_solve_triangular(U, z, verbose)
		# ========================================
		if verbose:
			print("x")
			print(x)
		# ========================================
		return x

def solve_LDLt(A, b, verbose=False, pivot="none"):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE DESCOMPOSICION LDL^t")
		print("=========================================")
		print("Partiendo de Ax = b se descompone:")
		print("* PA(P^t.P)x = Pb")
		print("'--> LDL^t.Px = Pb")
		print("Luego, la resolucion será: Lz = Pb -> Dv = z -> L^t.k = v -> Px = k")
	#=========================================
	P, L, D = LDLt(A, verbose, pivot)
	# ========================================
	if verbose:
		print("1. Resolviendo Lz = Pb")
	# ========================================
	z = for_solve_triangular(L, np.matmul(P, b), verbose)
	# ========================================
	if verbose:
		print("z")
		print(z)
		print("2. Resolviendo Dv = z")
	# ========================================
	v = for_solve_triangular(D, z, verbose)
	# ========================================
	if verbose:
		print("v")
		print(v)
		print("3. Resolviendo L^tk = v")
	# ========================================
	k = back_solve_triangular(L.T, v, verbose)
	# ========================================
	if verbose:
		print("k")
		print(k)
		print("4. Resolviendo Px = k (Ix = P^t.k)")
	# ========================================
	x = for_solve_triangular(np.eye(P.shape[0]), np.matmul(P.T, k), verbose)
	# ========================================
	if verbose:
		print("x")
		print(x)
	# ========================================
	return x

def solve_Cholesky(A, b, verbose=False, pivot="none"):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE DESCOMPOSICION DE CHOLESKY")
		print("=========================================")
		print("Partiendo de Ax = b se descompone:")
		print("* PA(P^t.P)x = Pb")
		print("'--> G.G^t.Px = Pb")
		print("Luego, la resolucion será: Gz = Pb -> G^t.v = z -> Px = v")
	#=========================================
	P, G = Cholesky(A, verbose, pivot)
	# ========================================
	if verbose:
		print("1. Resolviendo Gz = Pb")
	# ========================================
	z = for_solve_triangular(G, np.matmul(P, b), verbose)
	# ========================================
	if verbose:
		print("z")
		print(z)
		print("2. Resolviendo G^t.v = z")
	# ========================================
	v = back_solve_triangular(G.T, z, verbose)
	# ========================================
	if verbose:
		print("v")
		print(v)
		print("3. Resolviendo Px = v")
	# ========================================
	x = back_solve_triangular(np.eye(P.shape[0]), np.matmul(P.T, v), verbose)
	# ========================================
	if verbose:
		print("x")
		print(x)
	# ========================================
	return x

def solve_Parlett_Reid(A, b, verbose=False, pivot="none"):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE RESOLUCION DE PARLET & REID")
		print("=========================================")
		print("Partiendo de Ax = b se descompone:")
		print("* PA(P^t.P)x = Pb")
		print("'--> L.T.L^t.Px = Pb")
		print("Luego, la resolucion será: Lz = Pb -> T.v = z -> L^t.k = v -> Px = k")
	#=========================================
	P, L, T = Parlett_Reid(A, verbose, pivot)
	# ========================================
	if verbose:
		print("1. Resolviendo Lz = Pb")
	# ========================================
	z = for_solve_triangular(L, np.matmul(P, b), verbose)
	# ========================================
	if verbose:
		print("z")
		print(z)
		print("2. Resolviendo Tv = z")
	# ========================================
	print(T)
	v = solve_Gauss(T, z)
	#v  = solve_tridiagonal(T, z)
	#print("???????????????????????", v)
	# ========================================
	if verbose:
		print("v")
		print(v)
		print("3. Resolviendo L^t.k = v")
	# ========================================
	k = back_solve_triangular(L.T, v, verbose)
	# ========================================
	if verbose:
		print("k")
		print(k)
		print("4. Resolviendo Px = k (Ix = P^t.k)")
	# ========================================
	x = for_solve_triangular(np.eye(P.shape[0]), np.matmul(P.T, k), verbose)
	# ========================================
	if verbose:
		print("x")
		print(x)
	# ========================================
	return x

def solve_Gram_Schmidt(A, b, verbose=False, pivot="none"):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE RESOLUCION DE GRAM SCHMIDT")
		print("=========================================")
		print("Partiendo de Ax = b se descompone:")
		print("* A.x = b")
		print("'--> Ux = E^t.b")
	#=========================================
	E, U = Gram_Schmidt(A, verbose)
	x = back_solve_triangular(U, np.matmul(np.linalg.inv(E), b), verbose)
	# ========================================
	if verbose:
		print("x")
		print(x)
	# ========================================
	return x

def solve_Householder(A, b, verbose=False):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE RESOLUCION DE HOUSEHOLDER")
		print("=========================================")
	#=========================================

	if A.shape[1] <= A.shape[0]:
		#=========================================
		if verbose:
			print("Caso m(fila)>n(columnas):")
			print("Aplicado a A = Q.R")
			print("Entonces se partira de A.x = b")
			print("'---> Q.R.x = b")
			print("'---> 1) R.x = Q^t.b = b_hat")
			print("Usando solo la parte no nula de la matriz de R = [r  0]^T")
			print("'---> 2) r.x = mini_b_hat")
		#=========================================

		Q,R = Householder(A, verbose)

		b_hat = np.matmul(Q.T, b)
		mini_b_hat = b_hat[:, :R.shape[1]]

		# solucionando dimension de mini_b_hat
		temp = []
		for i in range(mini_b_hat.shape[1]):
			temp.append(mini_b_hat[0,i])
		mini_b_hat = np.array(temp)

		r = np.copy(R[:R.shape[1],:])

		#=========================================
		if verbose:
			print("r:\n", r)
			print("mini_b_hat (b_hat util para matriz r):\n", mini_b_hat)
		#=========================================
		x = back_solve_triangular(r, mini_b_hat)
		#=========================================
		if verbose:
			print("finalmente x:\n{}".format(x))
		#=========================================
		return x

	else:
		#=========================================
		if verbose:
			print("Caso n(columnas)>m(filas):")
			print("Aplicado a A^T = Q.R => A = [R^T  0^T].Q^T")
			print("Entonces se partira de A.x = b")
			print("'---> [R^T  0^T].Q^Tx = b")
			print("'---> (Q^T)x = z & [R^T  0^T]z = b")
			print("'---> R^T . z_R = b_R & x = Q([z_R  0]^T)")
		#=========================================

		A_t = A.T
		Q,R = Householder(A_t, verbose)
		print("=========================================")

		R_t_0 = R.T
		#=========================================
		if verbose:
			print("[R^T 0^T]:\n{}".format(R_t_0))
		#=========================================
		R_t = R_t_0[:,:R_t_0.shape[0]]
		#=========================================
		if verbose:
			print("R^T:\n{}".format(np.round(R_t)))
		#=========================================
		b_R = b[:R_t.shape[0]]
		#=========================================
		if verbose:
			print("b_R:\n{}".format(b_R))
			print("=========================================")
			print("> Resolviendo R^T z_R = b_R")
			print("=========================================")
		#=========================================
		z_R = for_solve_triangular(R_t,b_R, verbose)
		#=========================================
		if verbose:
			print("z_R:\n{}".format(z_R))
		#=========================================
		#=========================================
		if verbose:
			print("b_R:\n{}".format(b_R))
			print("=========================================")
			print("> Resolviendo x = Q ([z_R  0]^T)")
			print("=========================================")
		#=========================================
		z_R_0 = np.append(z_R, np.zeros(Q.shape[0] - z_R.size))
		#=========================================
		if verbose:
			print("z_R:\n{}".format(z_R_0))
		#=========================================
		x = np.matmul(Q, z_R_0)
		#=========================================
		if verbose:
			print("finalmente x:\n{}".format(x))
		#=========================================
		return x

if __name__=="__main__":
	A = np.array([[10, 8, 9],
				[5, 10, 4],
				[2, 4, 8]])
	A=A.T.dot(A)
	b = np.array([170, 117, 98])
	b=A.T.dot(b)
	#solve_LU_1(A, b,True,"none")
	#solve_L_1U(A, b, True,"none")
	solve_LDLt(A, b, True, "none")
	solve_Cholesky(A, b, True, "none")
	#solve_Parlett_Reid(A, b, True, "none")
	#solve_Gram_Schmidt(A, b, True, "none")
	#solve_Householder(A, b, True)
