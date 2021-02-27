import sympy as sp

def puntofijo(x0, g, tol):
	print('\nx_0 = ' + "%.7f"%x0)
	print('\ntol = ' + "%.9f"%tol)

	print('\ng(x) = ', end="")
	print(g, end="\n\n")

	h = ('k','x_k','g(x_k)')
	l = []
	k = 0
	g = sp.lambdify(x, g)

	while True:
		l.append((k, x0, g(x0)))
		x0 = g(x0)
		if abs(x0-g(x0)) <= tol:
			break
		k += 1

	print(h, end="\n\n")
	for row in l:
		print(row, end="\n")
	print("\n")
	return x0

if __name__ == '__main__':
	x = sp.symbols('x')
	
	#f = sp.exp(x) - 3*x**2
	
	#problema 3 - dirigida 4 - (20-2)
	#f =  x - sp.tan(x) 
	#g = sp.tan(x)  # [4.61, 7.85] -> 6.34

	#problema 4 - dirigida 4 - (20-2)
	#f = sp.exp(-1*x) - 3*sp.sin(2*x)
	#g = -1*sp.ln(3*sp.sin(2*x))

	#problema 5 - dirigida 4 - (20-2)
	#f = x * sp.exp(-1*(x**2)) - x * sp.tan(3*x)
	#g = -1*sp.ln(sp.tan(3*x)) / x

	# problema 6 - dirigida 4 - (20-2)
	#f = x**2 - 70 - sp.exp(0.5*x) * sp.cos(4*x)
	#g = sp.acos(((x**2) - 70 ) * sp.exp(-0.5*x)) / 4

	# problema 9 - dirigida 4 - (20-2)  
	#f = sp.exp(-0.25*x)*sp.sin(3*x) - 0.2
	#g = sp.asin(0.2 * sp.exp(0.25 * x)) / 3   # 0.068291 -> 3.91

	# problema 5 CALIFICADA 5 - 20-2
	# graficando la 5ta raiz positiva se encuentra en <5.5, 6> --> 5.68955546
	f = sp.tan(3*x) - x - 1
	g = sp.tan(3*x) - 1

	print('\nf(x) = ', end="")
	print(f, end="\n")



	puntofijo(x0 = 7, g = g, tol = 0.01)
