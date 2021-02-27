# Librería numpy
import numpy as np
import sympy as sp
from  time  import *
import matplotlib.pyplot as plt

gx = []
gy = []

print('MÉTODO NEWTON-RAPHSON',end="\n\n")

print("Este método linealiza la función a cada paso utilizando su derivada, para hallar la raíz de la ecuación en las proximidades de un punto inicial.\n")

def newton_rapshon_method(x, f, fd, maxiter, tol):

	for n in range(maxiter):
		y = x 

		x = x - f(x)/df(x)
		
		gy.append(x)
		gx.append(n+1)
		print ("Para la iteración "+str(n+1)+": X = "+str("{:10.10f}".format(x))+"\tError: "+str(abs(x - y)))
		if (abs(x-y) <= tol):
			grafico(gx, gy)
			return [x, n]
	return maxiter

def grafico (x, y):
    plt.plot(gx, gy,'r')
    plt.title('Método de Newton-Raphson')
    plt.xlabel("Numéro de iteraciones")
    plt.ylabel("Valor de X")
    plt.show()

# Defina la función a usar
e = 2.7182818284


#problema 5 - dirigida 4 - (20-2)
#f = lambda x: x * e**(-1*(x**2)) - x * np.tan(3*x)
#df = lambda x: e**(-1*(x**2)) - 2*(x**2)*e**(-1*(x**2)) - np.tan(3*x) - 3*x * (float(sp.sec(3*x))**2)


# problema 8 - dirigida 4 - (20-2)
#f = lambda x: 75*(2*(e**(-0.2*x)) - e**(-0.8*x)) - 88
# Defina la derivada de la función a usar
#df = lambda x: 75*(-0.4*(e**(-0.2*x)) + 0.8*e**(-0.8*x))


# problema 9 - dirigida 4 - (20-2)  
#f = lambda x: (e**(-0.25*x))*np.sin(3*x) - 0.2
#df = lambda x: -0.25*(e**(-0.25*x))*np.sin(3*x) + 3*(e**(-0.25*x))*np.cos(3*x)

# problema 4 CALIFICA 5 - 20-1
# graficando hay una raiz entre 0.5 y 1 (no consideramos el  0)  -> 0.7968121
#f = lambda x: x - 1 + e**(-2*x)
#df = lambda x: 1 - 2*(e**(-2*x))

f = lambda x: 9*(e**(-0.7*x))*np.cos(4*x) - 3.5
df = lambda x: -9*0.7*(e**(-0.7*x))*np.cos(4*x) - 9*(e**(-0.7*x))*np.sin(4*x)*4

# Punto Xo
Xo = 0.29  # probar con 0 también
gy.append(Xo)
gx.append(0)

# Numéro de iteraciones
maxite = 50


print("Tenemos la funcion f(x)\n")

print("Iniciamos con un valor Xo = ", str(Xo),"\n")

# Poner la cota de error de la raíz
tol = 1.0e-6

[x, k] = newton_rapshon_method(Xo, f, df, maxite, tol) 

if k==maxite:
	print("El método diverge o no converge para la cota de error pedido")

else:
	print("\nLa raíz buscada es: "+str(x))

print(f"f(4.6) = {f(4.6)}")
print(f"f(5.6) = {f(5.6)}")
print(f"f(5.6)*f(4.6) = {f(5.6)*f(4.6)}")