import numpy
from scipy import linalg
from sympy import *

def dominante(y):
    columns=(y.shape)[0]
    c=y[0]
    for i in range(0,columns-1):
        if abs(y[i+1])>abs(c):
            c=y[i+1]
    return c

def Pivot_mat(A, c_index):
    dim = A.shape[0]
    P = numpy.eye(dim)

    index = c_index
    for i in range(c_index + 1, dim):
        if abs(A[i,c_index]) > abs(A[index,c_index]):
            index = i

    if index != c_index:
        P[[index, c_index]] = P[[c_index, index]]

    return P

def Gauss(A, b, verbose=False, pivot="none"):
    A_save = A
    A_b = numpy.matrix(numpy.c_[A, b]) # Augmented matrix
    n_row, n_col = A_b.shape[0], A_b.shape[1]
    process_string = "A_b"

    P = numpy.eye(n_row)
    L = numpy.eye(n_row)

    # ========================================
    if verbose:
        print("Matriz aumentada al inicio:")
        print(A_b)
        print("========================")
    # ========================================


    for i in range(0, n_row-1): # Main loop
        # Gauss matrices preparation
        P_i = numpy.eye(n_row)
        L_i = numpy.eye(n_row)

        if (A_b[i,i] == 0 and pivot == "partial") or pivot=="total":
            P_i = Pivot_mat(A_b, i)

        # ========================================
        if verbose:
            print("P_{}".format(i+1))
            print(P_i)
            print("========================")
        # ========================================

        # Apply permutation
        A_b = numpy.matmul(P_i,A_b)
        P = numpy.matmul(P_i, P)
        L = numpy.matmul(P_i, L)

        # ========================================
        if verbose:
            process_string = "P_{}.".format(i+1) + process_string
            print(process_string)
            print(A_b)
            print("========================")
        # ========================================

        # Preparing alpha_i
        alpha_i = numpy.zeros(n_row)
        alpha_i[i+1:] = numpy.transpose(A_b[i+1:n_row,i])/A_b[i,i]

        # ========================================
        if verbose:
            print("alpha_{}".format(i+1))
            print(alpha_i)
            print("========================")
        # ========================================

        # Preparing e_i
        e_i = numpy.zeros(n_row)
        e_i[i] = 1

        # Calc. L_i
        L_i = numpy.eye(n_row) - numpy.outer(alpha_i, e_i)
        L = numpy.matmul(L_i, L)

        # ========================================
        if verbose:
            print("L_{}".format(i+1))
            print(L_i)
            print("========================")
        # ========================================

        # Transform system
        A_b = numpy.matmul(L_i,A_b)
        # ========================================
        if verbose:
            process_string = "L_{}.".format(i+1) + process_string
            print(process_string)
            print(A_b)
            print("========================")
        # ========================================

    # Final calculus of LU matrices
    U = A_b[:,:n_col-1]
    L = numpy.linalg.inv(numpy.matmul(L, numpy.linalg.inv(P)))

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
def back_solve_triangular(A, b, verbose=False):
    x = numpy.empty(A.shape[1])
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
    x = numpy.zeros(A.shape[1])
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
	z = for_solve_triangular(L, numpy.matmul(P, b), verbose)
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

# HouseHolder
#	A: Matrix to wich Householder factorization is applied
#	return: Q, R Matrices so A = Q.R, Q:Orthogonal
def Householder(A, verbose=False):
	n_row, n_col = A.shape[0], A.shape[1]
	A_k = numpy.copy(A)
	n_row_k, n_col_k = A_k.shape[0], A_k.shape[1]
	R = numpy.zeros((n_row, n_col))
	Q = numpy.eye(n_row)

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
		current_col = numpy.asmatrix(A_k[:, 0]).T

		e_k = numpy.asmatrix(numpy.repeat(0, A_k.shape[0])).T
		e_k[0,0] = 1

		w = numpy.sign(current_col[0,0])*numpy.linalg.norm(current_col, 2)*e_k + current_col
		if numpy.linalg.norm(w, 2) != 0:
			w = w/numpy.linalg.norm(w, 2)
		# ========================================
		if verbose:
			print("w_{}\n{}".format(k, w))
		# ========================================
		H_k = numpy.eye(A_k.shape[0]) - 2*numpy.matmul(w, w.T)
		# ========================================
		if verbose:
			print("H_{}\n{}".format(k, expandedMat(H_k, k)))
		# ========================================
		Q = numpy.matmul(expandedMat(H_k, k), Q)

		HxA = numpy.matmul(H_k, A_k)
		R[k:n_row,k:n_col] = numpy.copy(HxA)
		# ========================================
		if verbose:
			print("R_{}\n{}".format(k, R))
		# ========================================
		A_k = numpy.empty((n_row_k-1, n_col_k-1))
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
	A_exp = numpy.copy(A)
	upper_expand = numpy.zeros((n,A.shape[1]))
	left_expand = numpy.vstack((numpy.eye(n), numpy.zeros((A.shape[0],n))))
	A_exp = numpy.r_[upper_expand, A_exp]
	A_exp = numpy.c_[left_expand, A_exp]
	return numpy.asmatrix(A_exp)

#---VALORES Y VECTORES PROPIOS
#--- METODO DE Krylov

def EIG_Krylov(A, y, verbose=False):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE KRYLOV")
		print("Resolviendo a partir de un vector inicial:", y)
		print("Para la matriz:\n", A)
		print("=========================================")
	#=========================================

	vec_list = []
	vec_list.append(y)

	n_iter = A.shape[0]
	for i in range(0, n_iter):
		#=========================================
		if verbose:
			print("=========================================")
			print("v_{} = A.v_{}: \n".format(i, i-1), numpy.matmul(A, vec_list[i]))
		#=========================================
		vec_list.append(numpy.matmul(A, vec_list[i]))

	coef_mat = numpy.copy(vec_list[0])

	for i in range(1, len(vec_list) - 1):
		coef_mat = numpy.c_[vec_list[i], coef_mat]
	b = -1.*vec_list[len(vec_list) - 1]

	#=========================================
	if verbose:
		print("Matriz de coef:\n", coef_mat)
		print("Vector de resolucion:\n", b)
		print("Resolviendo ...")
	#=========================================

	equation_coefs = solve_Gauss(coef_mat, b, verbose)

	#=========================================
	if verbose:
		eq_string = "lambda^" + str(n_iter)
		for i in range(0, n_iter):
			eq_string += "+(" + str(equation_coefs[i]) + ")lambda^" + str(n_iter-i-1) + " "
		eq_string += "= 0"
		print("=========================================")
		print("Ecuacion final:", eq_string)
		print("=========================================")
	#=========================================
	return equation_coefs

#---METODO DE LERERNIER-FADDEER
def EIG_Leverrier(A, verbose=False):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO DE LEVERRIER FADEEV")
		print("=========================================")
	#=========================================
	n = A.shape[0]
	B0 = numpy.copy(A)
	b_0 = -numpy.trace(B0)

	b_values = numpy.empty(n)
	b_values[0] = b_0

	B_old = B0
	#=========================================
	if verbose:
		print("---------------------------------------")
		print("B_{}:\n{}".format(1, B_old))
		print("b_{}:{}".format(1, b_values[0]))
		print("---------------------------------------")
	#=========================================
	for i in range(1, n):
		Bk = numpy.matmul(A, B_old + b_values[i-1]*numpy.eye(n))
		b_values[i] = -numpy.trace(Bk)/(i+1)
		B_old = numpy.copy(Bk)
		#=========================================
		if verbose:
			print("---------------------------------------")
			print("B_{}:\n{}".format(i+1, B_old))
			print("b_{}:{}".format(i+1, b_values[i]))
			print("---------------------------------------")
		#=========================================

	#=========================================
	if verbose:
		eq_string = "lambda^" + str(n)
		for i in range(0, n):
			eq_string += "+(" + str(b_values[i]) + ")lambda^" + str(n-i-1) + " "
		eq_string += "= 0"
		print("=========================================")
		print("Ecuacion final:", eq_string)
		print("=========================================")
	#=========================================
	return b_values
def autovect_Potencia(A, w = None, E = 1E-5, v = False):
    """Calcula el autovalor dominante de una matriz cuadrada A usando el
    método de potencia.

    Reciba matriz cuadrada A, w vector arbitrario multiplicable con A.
    Retorna autovalor dominante.

    Para una solución detallada, pasar v = True como parámetro.
    """
    fil, col = A.shape
    assert fil == col, "Matriz no cuadrada."

    if w is None :

        if v :
            print("Vector arbitrario no escogido.")
            print("Se usará w = [1 1 ...1]")

        w = numpy.ones(fil)
    else:
        dim_w, = w.shape # Solo tomamos el primer término del 'shape'
        assert dim_w == fil, "Dimensión del vector w no compatible con A."

    maxIter = 100
    y_i = A.dot(w)
    lambda_i = dominante(y_i)
    w_new = (1 / lambda_i) * y_i
    Error = abs(dominante(w_new-w))
    w = w_new
    if v :
            print("y_1: {}.".format(y_i))
            print("lambda_1: {}.".format(lambda_i))
            print("x_1: {}".format( w))
            print("Error:{}".format(Error))
    for i in range(2, maxIter + 1):
        y_i = A @ w
        lambda_o = lambda_i
        lambda_i = dominante(y_i)
        w_new = (1 / lambda_i) * y_i
        Error = abs(dominante(w_new-w))
        w = w_new
        if v :
            print("y_{}: {}.".format(i, y_i))
            print("lambda_{}: {}.".format(i, lambda_i))
            print("x_{}: {}".format(i, w))
            print("Error:{}".format(Error))

        if abs(lambda_i - lambda_o) < E :
            break

    return lambda_i
#---POTENCIA inversa
def autovect_PotenciaInver(A, w = None, E = 1E-5, v = False):
    """Calcula el autovalor dominante de una matriz cuadrada A usando el
    método de potencia inversa.

    Reciba matriz cuadrada A, w vector arbitrario multiplicable con A.
    Retorna autovalor dominante.

    Para una solución detallada, pasar v = True como parámetro.
    """
    fil, col = A.shape
    assert fil == col, "Matriz no cuadrada."

    if w is None :

        if v :
            print("Vector arbitrario no escogido.")
            print("Se usará w = [1 1 ...1]")

        w = numpy.ones(fil)
    else:
        dim_w, = w.shape # Solo tomamos el primer término del 'shape'
        assert dim_w == fil, "Dimensión del vector w no compatible con A."

    maxIter = 100
    B=numpy.linalg.inv(A)
    y_i = B.dot(w)
    lambda_i = dominante(y_i)
    w_new = (1 / lambda_i) * y_i
    Error = abs(dominante(w_new-w))
    w = w_new
    if v :
            print("y_1: {}.".format(y_i))
            print("lambda_1: {}.".format(lambda_i))
            print("x_1: {}".format( w))
            print("Error:{}".format(Error))

    for i in range(2, maxIter + 1):
        y_i = B @ w
        lambda_o = lambda_i
        lambda_i = dominante(y_i)
        w_new = (1 / lambda_i) * y_i
        Error = abs(dominante(w_new-w))
        w=w_new
        if v :
            print("y_{}: {}.".format(i, y_i))
            print("lambda_{}: {}.".format(i, lambda_i))
            print("x_{}: {}".format(i, w))
            print("Error:{}".format(Error))
        if abs(lambda_i - lambda_o) < E :
            break
    return (1/lambda_i)

#---POTENCIA INVERSA DESPLAZADA
def autovect_PotenciaInver_desplazada(A,q,w = None , E = 1E-5, v = False):
    """Calcula el autovalor dominante de una matriz cuadrada A usando el
    método de potencia inversa desplazada

    Reciba matriz cuadrada A, w vector arbitrario multiplicable con A y q es desplazamiento
    Retorna autovalor dominante.

    Para una solución detallada, pasar v = True como parámetro.
    """
    fil, col = A.shape
    assert fil == col, "Matriz no cuadrada."

    if w is None :

        if v :
            print("Vector arbitrario no escogido.")
            print("Se usará w = [1 1 ...1]")

        w = numpy.ones(fil)
    else:
        dim_w, = w.shape # Solo tomamos el primer término del 'shape'
        assert dim_w == fil, "Dimensión del vector w no compatible con A."

    maxIter = 100
    I=numpy.identity(fil)
    B=numpy.linalg.inv((A - (q*I)))
    y_i = B.dot(w)
    lambda_i = dominante(y_i)
    w_new = (1 / lambda_i) * y_i
    Error = abs(dominante(w_new-w))
    w = w_new
    if v :
            print("y_1: {}.".format(y_i))
            print("lambda_1: {}.".format(lambda_i))
            print("x_1: {}".format( w))
            print("Error:{}".format(Error))
    for i in range(2, maxIter + 1):
        y_i = B @ w
        lambda_o = lambda_i
        lambda_i = dominante(y_i)
        w_new = (1 / lambda_i) * y_i
        Error = abs(dominante(w_new-w))
        w = w_new
        if v :
            print("y_{}: {}.".format(i, y_i))
            print("lambda_{}: {}.".format(i, lambda_i))
            print("x_{}: {}".format(i, w))
            print("Error:{}".format(Error))
        if abs(lambda_i - lambda_o) < E :
            break
    return (1/lambda_i+ q)
#---BISECCION O GIVENS
    # A: Tridiagonal matrix
	# k: lambda polynomial index
    # return: lambda polynomial for bisection eigenvalues finding method
def Bisec_Pk(A, k):
	a = numpy.diag(A)
	b = numpy.diag(A, k=-1)

	if k == 0:
		def P0(lamb):
			return 1
		return P0
	elif k == 1:
		def P1(lamb):
			return (a[0] - lamb)
		return P1
	else:
		f_k1 = Bisec_Pk(A, k-1)
		f_k2 = Bisec_Pk(A, k-2)

		def Pk(lamb):
			return ((a[k-1] - lamb)*f_k1(lamb) - (b[k-2]**2)*f_k2(lamb))
		return Pk

# Bisec_change_counter
	# v: array/vector of numeric values

    # return: number of times that the elements of v changed sign
def Bisec_change_counter(v):
	cont = 0;
	for i in range(1, len(v)):
		sign_vi = 0 if (v[i] < 0) else 1
		sign_vi_1 = 0 if (v[i-1] < 0) else 1
		if sign_vi != sign_vi_1:
			cont += 1
	return cont


# Bisec_find_interval
	# A: Tridiagonal matrix
	# alpha_left: initial left point of search of interval
	# alpha_right: initial right point of search of interval

	# return: new interval [alpha_left, alpha_right] that satisfies condition
def Bisec_find_interval(A, alpha_left, alpha_right):
	n = A.shape[0]
	# Creating {P0, P1, ..., Pn} redy to evaluate in a alpha
	p = []
	for i in range(0, n+1):
		p.append(Bisec_Pk(A, i))

	# Initial value of {P0(alpha_left), P1(alpha_left), ...}
	for_alpha_left = []
	for i in range(0, len(p)): for_alpha_left.append(p[i](alpha_left))

	# Initial value of {P0(alpha_right), P1(alpha_right), ...}
	for_alpha_right = []
	for i in range(0, len(p)): for_alpha_right.append(p[i](alpha_right))

	while (Bisec_change_counter(for_alpha_left) != 0) or (Bisec_change_counter(for_alpha_right) != n):
		# Extend the interval
		alpha_left -= 1
		alpha_right += 1

		for_alpha_left = []
		for i in range(0, len(p)): for_alpha_left.append(p[i](alpha_left))
		for_alpha_right = []
		for i in range(0, len(p)): for_alpha_right.append(p[i](alpha_right))


	print(alpha_left, alpha_right, '\n', for_alpha_left, for_alpha_right)
	return alpha_left, alpha_right

def Bisec_p_vector(A, alpha):
	n = A.shape[0]
	# Creating {P0, P1, ..., Pn} redy to evaluate in a alpha
	p = []
	for i in range(0, n+1):
		p.append(Bisec_Pk(A, i))

	for_alpha = []
	for i in range(0, len(p)): for_alpha.append(p[i](alpha))

	return numpy.array(for_alpha)

eigenvalues_container = [] # Global array for the recursion in Bisec_find_eigens

def Bisec_find_eigens(A, alpha_left, alpha_right, eps, num_eig):
	global eigenvalues_container
	print("[{};{}]".format(alpha_left, alpha_right))
	alpha_mid = (alpha_left + alpha_right)/2.0
	print("m=", alpha_mid)
	if numpy.abs(alpha_left - alpha_right) <= eps:
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!", alpha_mid)
		eigenvalues_container.append(alpha_mid)
	else:
		#print("for left:", Bisec_p_vector(A, alpha_mid))
		num_eig_left = Bisec_change_counter(Bisec_p_vector(A, alpha_mid))
		num_eig_right = num_eig - num_eig_left

		print("(#",num_eig_left, ";#",num_eig_right, ")")

		if num_eig_left > 0:
			Bisec_find_eigens(A, alpha_left, alpha_mid, eps, num_eig_left)
		if num_eig_right > 0:
			Bisec_find_eigens(A, alpha_mid, alpha_right, eps, num_eig_right)

def EIG_Biseccion(A, alpha_left_0, alpha_right_0, eps, verbose=False):
	global eigenvalues_container
	eigenvalues_container = []
	n = A.shape[0]
	alpha_left, alpha_right = Bisec_find_interval(A, alpha_left_0, alpha_right_0)
	Bisec_find_eigens(A, alpha_left, alpha_right, eps, n)
	return eigenvalues_container

#--- jacobi
def EIG_Jacobi(matrix, E, verbose=False, pre_check=True):
	if pre_check:
		# checking for squareness
		if matrix.shape[0] != matrix.shape[1]:
			raise (ValueError('Error: Matriz no es cuadrada'))

		# checking for symmetry
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if matrix[i][j] != matrix[j][i]:
					raise (ValueError('Error: Matriz no es simetrica'))

	counter = 0

	while 1:
		maximum, h, f = 0, 0, 0

		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if i != j and maximum < abs(matrix[i][j]):
					maximum = abs(matrix[i][j])
					h, f = i, j

		m = (matrix[f][f] - matrix[h][h]) / 2 * matrix[h][f]
		t = numpy.sign(m) / (abs(m) + numpy.sqrt(m * m + 1))
		c = 1 / numpy.sqrt(t * t + 1)
		s = t * c

		mul_matrix = numpy.eye(len(matrix))
		mul_matrix[h][h], mul_matrix[f][f] = c, c
		mul_matrix[h][f], mul_matrix[f][h] = s, -s
		matrix = numpy.dot(numpy.dot(mul_matrix.transpose(), matrix), mul_matrix)

		counter += 1

		if verbose:
			s_d = sum(matrix[i][i] * matrix[i][i] for i in range(len(matrix)))
			s_nd = sum(matrix[i][j] * matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i != j)

			print('iter#', counter,  '\n\nMatriz T:\n', mul_matrix, '\n\nMatriz T\':\n', mul_matrix.transpose(), '\n\n',
				  'S_d: ', s_d, '\n', 'S_nd: ', s_nd, '\n', 'S: ', s_d + s_nd, '\n---------------------------------')

		if sum(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i != j) < E:
			break

	return matrix.diagonal()[::-1]

#--- hOUSEhOLDER QR
def EIG_QR(A, max_iter, epsilon, verbose=False):
	#=========================================
	if verbose:
		print("=========================================")
		print("METODO QR")
		print("=========================================")
	#=========================================
	cont = 1
	A_k = numpy.copy(A)
	v_old = numpy.diag(A_k)
	#=========================================
	if verbose:
		print("A_0:\n{}".format(A_k))
	#=========================================
	for k in range(1, max_iter):
		cont += 1
		Q_k, R_k = Householder(A_k, verbose)
		A_k = numpy.matmul(R_k, Q_k)
		#=========================================
		if verbose:
			print("A_{}:\n{}".format(k, A_k))
		#=========================================
		if 	numpy.linalg.norm(A_k - numpy.diag(numpy.diag(A_k))) < epsilon:
			print("Valores hallados con presicion eps:{}".format(epsilon))
			break
		v_old = numpy.copy(numpy.diag(A_k))

	#=========================================
	if verbose:
		print("A_k final (iteracion {}):\n{}".format(cont, A_k))
		print("Valores propios:\n{}".format(numpy.diag(A_k)))
	#=========================================

	return numpy.diag(A_k)


if __name__ == '__main__':

	B=numpy.array([[ 0.6 , 0.1 , 0.1],
						[0.1, 0.8, 0.2],
						[0.3 , 0.1 , 0.7]])
	x_0=numpy.array([30., 20., 50.])
	tol = 0.00001
	#polinomio
	#x=EIG_Krylov(A,True)
	#y=EIG_QR(B,100,tol,True)
	print("\nMETODO DE POTENCIA\n")
	x = autovect_Potencia(B, x_0, tol, True)
	print(x, end="\n\n")

	print("\nMETODO DE POTENCIA INVERSA\n")
	y = autovect_PotenciaInver(B, x_0, tol, True)
	print(y, end="\n\n")

	print("\nMETODO DE POTENCIA INVERSA DESPLAZADA\n")
	q = 0.6
	z  =autovect_PotenciaInver_desplazada(B, q, x_0, tol, True)
	print(z, end="\n\n")
