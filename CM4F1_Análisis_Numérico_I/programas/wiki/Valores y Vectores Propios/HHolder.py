import numpy as np
from numpy import linalg as LA

"""
ESTE CÓDIGO NECESITA SER ORDENADO"
"""

def multmatr(A,B):

	m = A.shape[0]
	p = B.shape[0]
	n = B.shape[1]
	C = np.array([0.0]*(m*n))
	C.shape = (m,n)

	for i in range(m):
		for j in range(n):
			s = 0.0
			for k in range(p):
				s = s + A[i][k]*B[k][j]
			C[i][j] = s
	return C
		
def HHolder(A,b):
	m = A.shape[0]
	n = A.shape[1]
	Ak = np.copy(A)
	w = np.array([0.0]*m)
	w.shape = (m,1)
	print("b1: ", b, end="\n\n")
	for j in range(n):
		print("j: ", j, end="\n\n")
		if LA.norm(A[j:m,j],np.inf) == 0:
			break
		delta = LA.norm(A[j:m,j],2)*np.sign(A[j][j])
		print("d: ", delta, end="\n\n")

		w[j:m,0] = A[j:m,j]
		w[j][0] = w[j][0] + delta
		print("W: ")
		print(w, end="\n\n")

		beta = 2.0/((LA.norm(w[j:m,0],2))**2)
		print("beta: ")
		print(beta, end="\n\n")

		A[j][j] = -delta
		print("Ajj: ")
		print(A[j][j], end="\n\n")

		for l in range(j+1,n):
			print("l: ", l, end="\n\n")
			print("wTl: ",w.T[0,j:m], end="\n\n")
			print("Al: ", A[j:m,l], end="\n\n")

			s = w.T[0,j:m].dot(A[j:m,l])
			print("sl: ", s, end="\n\n")
			print("A[j:m,l]: ", A[j:m,l], end="\n\n")
			print("w[j:m,0]*s*beta : ", w[j:m,0]*s*beta, end="\n\n")

			A[j:m,l] = A[j:m,l] - w[j:m,0]*s*beta
			print("A[j:m,l]: ",A[j:m,l], end="\n\n")

		print("A: ")
		print(A, end="\n\n")

		print("b* : ", b, end="\n\n")
		print("w: ",w.T[0,j:m], end="\n\n")
		print("b: ",b[j:m,0], end="\n\n")
		s = w.T[0,j:m].dot(b[j:m,0])
		print("s: ", s, end="\n\n")
		#print(w[j:m]*s)
		b[j:m] = b[j:m] - w[j:m]*s*beta
		print("B: ", b, end="\n\n")
		print("w: ", w, end="\n\n")

	return A, b

def sol(A,b):
	m = b.shape[0]
	n = A.shape[1]
	x = np.array([0.0]*n)
	x.shape = (n,1)
	for j in range(n-1,-1,-1):
		print("A[j,j+1:n].dot(x[j+1:n]): ", A[j,j+1:n].dot(x[j+1:n]), end="\n\n")
		print("bj: ", b[j], end="\n\n")
		print("b-ax: ", (b[j]-A[j,j+1:n].dot(x[j+1:n]))/A[j][j], end="\n\n")
		print("ajj: ",A[j][j], end="\n\n")
		a = b[j]-A[j,j+1:n].dot(x[j+1:n])
		print("a: ",a[0], end="\n\n")
		x[j] = a[0]/(A[j][j])
		print("xj: ",x[j][0], end="\n\n")
	print("x: ", x, end="\n\n")
	resid = b[n:m]*b[n:m].T
	print("residuo: ", resid, end="\n\n")
	return x, resid


if __name__ == '__main__':

	A = np.array([[1.,1.,1.],[1.,1.,2.],[3.,4.,1.],[4.,9.,16.]])
	b = np.array([2.,3.,5.,6.])
	b.shape = (4,1)
	#print((b[0:4,0]*3).shape)

	C = HHolder(A,b)
	D = sol(C[0],C[1])
	#(E,F) = sol(C,D)
	#print(E)
	#print(F)
