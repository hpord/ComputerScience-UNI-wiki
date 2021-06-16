# Librería numpy
import numpy as np
from  time  import *
import matplotlib.pyplot as plt

gx=[]
gy=[]

print('MÉTODO DE LA SECANTE',end="\n\n")

print("Este método se basa en el método de Newton con diferencia que al tomar la derivada lo toma como su teorema fundamental.\n")

def secante(x0, x1, f, maxiter, tol):

	for n in range(maxiter):
		y = x1

		x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))

		gy.append(x)
		gx.append(n+2)
		print ("Para la iteración "+str(n+2)+": X = "+str("{:10.10f}".format(x))+"\tError: "+str(abs(x-y)))
		if (abs(x-y)<=tol):
			grafico(gx,gy)
			return [x,n]
		x0 = x1
		x1 = x
	return [x, 999999]

def grafico (x,y):
    plt.plot(gx, gy,'r')
    plt.title('Método de la Secante')
    plt.xlabel("Numéro de iteraciones")
    plt.ylabel("Valor de X")
    plt.show()

# Defina la función a usar

# problema 8 - dirigida 4 - (20-2)
#f = lambda x: x**3 + 4*x**2 - 10
e = 2.7182818284
#f = lambda x: 75*(2*(e**(-0.2*x)) - e**(-0.8*x)) - 88

#problema 4 - dirigida 4 - (20-2)
#f = lambda x: e**(-1*x) - 3*np.sin(2*x)

#problema 5 - dirigida 4 - (20-2)
#f = x * sp.exp(-1*(x**2)) - x * sp.tan(3*x)


# problema 4 CALIFICA 5 - 20-1
# graficando hay una raiz entre 0.5 y 1 (no consideramos el  0)  -> 0.7968121
f = lambda x: x - 1 + e**(-2*x)


# Punto Xo
X0 = 0.5 
gy.append(X0)
gx.append(0)

# Punto X1
X1 = 1
gy.append(X1)
gx.append(1)

# Numéro de iteraciones
maxite=20



print("Tenemos la funcion f(x) \n")

print("Iniciamos con un valor Xo = ",str(X0)," y con el valor X1 = ",str(X1),"\n")

# Poner la cota de error de la raíz
tol = 1.0e-6

[x,k] = secante(X0, X1, f, maxite, tol) 

if k==999999:
	print("El método diverge o no converge para la cota de error pedido")

else:
	print("\nLa raíz buscada es: "+str(x))