import sympy as sp
def newton_raphson(F,x0,tol):
	var = list(F.free_symbols)
	n = len(var)

	JF = F.jacobian(var)
	print('JF(x): ')
	print(JF, end="\n\n")

	JFi = sp.simplify(JF.inv())
	print('[JF(x)]^{-1}: ')
	print(JFi, end="\n\n")

	h = ('k',) + tuple('x_%i^{(k)}'%(i+1) for i in range(n))
	
	print('x^{(0)}: ') 
	print(x0, end="\n\n")
	
	print('tol='+"%.7f"%tol, end="\n\n")
	l = []
	l.append((0,)+tuple('%.7f'%x0[i] for i in range(n)))
	k = 1
	while True:
		Fx = F.evalf(subs=dict(zip(var,x0)))
		JFix = JFi.evalf(subs=dict(zip(var,x0)))
		x0 -= JFix * Fx
		l.append((k,)+tuple('%.7f'%x0[i] for i in range(n)))
		if Fx.norm() < tol:
			break
		k += 1
	
	print(h, end="\n\n")
	for row in l:
		print(row, end="\n")
	print("\n")
	return x0

if __name__ == '__main__':
	

	x1, x2, x3 = sp.symbols('x1 x2 x3')

	'''
	F = sp.Matrix([x1*x2-72,
				   x1*x2-3*x1+2*x2-78])
	'''

	'''
	# ejercicio 1, DIRIGIDA 6- 20_2
	F = sp.Matrix([-20*x1 + x2*x2 + 19,
				   x1*x1 - 20*x2 + 19])	
	'''

	# pc6 - 20.2
	#F = sp.Matrix([2*x1 + x2*x2 + (x2*x2*x1*x1)- 9,

	#			   x1*x1*x1 - x2*x2 + (x2*x1) - 5])	
	F = sp.Matrix([x1*x1 - x1 + x2*x2 + x3*x3 - 5,
				   x1*x1 + x2*x2 - x2 + x3*x3 - 4,
				   x1*x1 + x2*x2 + x3*x3 + x3 - 6])	
	print('F(x): ')
	print(F, end="\n\n")

	x0 = sp.Matrix([1.0, 0, 0])

	x = newton_raphson(F, x0, 1e-10)
	print("Matriz 'x': ")
	print(sp.Matrix(x))
