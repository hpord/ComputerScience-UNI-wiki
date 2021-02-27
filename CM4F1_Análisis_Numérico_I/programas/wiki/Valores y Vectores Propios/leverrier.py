import numpy as np

def leverrier(A):
	n = A.shape[0]
	b = 1.
	l = [b]
	B = np.zeros_like(A)
	for i in range(n):
		B = A@(B+b*np.identity(n))
		b = -np.trace(B)/(i+1)
		l+=[b]

		print('B_%i :'%(i+1))
		print(B, end="\n\n")

		print('b_%i = %.7f'%(i+1, b), end="\n\n")
		

	return l

if __name__=='__main__':
	# ejercicio 7, dirigida 7, 20-2  
	A = np.array([[3.0, -1.0, 0.0],
			  [-1.0, 2.0, -1.0],
			  [0.0, -1.0, 3.0]])

	print("\nMatriz 'A':\n", A, end="\n\n")
	print("==========================")
	print('Numpy:\n', np.poly(A), end="\n\n")
	print("==========================")
	print('LeVerrier:\n', leverrier(A), end="\n\n")
