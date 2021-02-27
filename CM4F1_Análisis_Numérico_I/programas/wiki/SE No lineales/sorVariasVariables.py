import sympy as sp

def gaussseidel(F,x0,w,tol):
	var = list(F.free_symbols)
	n = len(var)
	JF = F.jacobian(var)
	print('JF(x): ')
	print(JF, end="\n\n")

	L = JF[:,:]
	for i in range(n):
		for j in range(n):
			if i<j:
				L[i:j] = 0
	D = sp.diag(JF)
	G = (1-w)/w*D+L

	Gi = G.inv()
	print('[JF(x)]^{-1}: ')
	print(Gi, end="\n\n")

	h = ('k',) + tuple('x_%i^{(k)}'%(i+1) for i in range(n))
	
	print('x^{(0)}: ') 
	print(x0, end="\n\n")

	print('tol='+"%.7f"%tol, end="\n\n")
	l = []
	l.append((0,)+tuple('%.7f'%x0[i] for i in range(n)))
	k = 1
	while True:
		Fx = F.evalf(subs=dict(zip(var,x0)))
		Gix = Gi.evalf(subs=dict(zip(var,x0)))
		x0 -= Gix * Fx
		l.append((k,)+tuple('%.7f'%x0[i] for i in range(n)))
		if Fx.norm() < tol:
			break
		k += 1
	
	print(h, end="\n\n")
	for row in l:
		print(row, end="\n")
	print("\n")
	return x0

if __name__=='__main__':
	x1,x2 = sp.symbols('x_1 x_2')
	F = sp.Matrix([x1+x2-7,x1*x2-10])
	print('F(x): ')
	print(F, end="\n\n")

	x0 = sp.Matrix([1.5,2.5])
	x = gaussseidel(F,x0,.14,0.01)
	print("Matriz 'x': ")
	print(sp.Matrix(x))
