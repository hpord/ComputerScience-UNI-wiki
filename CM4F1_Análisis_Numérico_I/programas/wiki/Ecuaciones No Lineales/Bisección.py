# Librería numpy
import numpy as np
import math
from  time  import *
import matplotlib.pyplot as plt

print('MÉTODO DE LA BISECCIÓN',end="\n\n")

print("El método de la bisección es un método simple y convergente para calcular la raíz de una función.\n")

"""
Si la función tiene más de una raíz calcula la mas cercana al punto. Si o si en este método mientras se va reduciendo el intervalo
los extremos L y U deben cumplir f(L)f(U)<0.
"""
gx=[]
gy=[]

def  biseccion(f,  a,  b,  e): 
	i = 0
	y = 0
	while b-a>=e:
		c=(a+b)/2
		gx.append(i)
		gy.append(c)
		if i==0:
			print ("Para la iteración "+str(i)+": X = "+str("{:10.10f}".format(c)))
		else:
			print ("Para la iteración "+str(i)+": X = "+str("{:10.10f}".format(c))+"\tError: "+str(abs(c-y)))
		
		y=c
		if f(c)==0:
			grafico(gx,gy)
			return c
		else:
			if f(a)*f(c)>0: 
				a=c
			else:
				b=c
		i  = i + 1
	grafico (gx,gy)
	return c

def grafico (x,y):
    plt.plot(gx, gy, 'r')
    plt.title('Método de la Bisección')
    plt.xlabel("Numéro de iteraciones")
    plt.ylabel("Valor de X")
    plt.show()

# Defina la función a usar
'''def f(x): return x*math.exp(x)-math.pi'''
f = lambda x: 9*(e**(-0.7*x))*np.cos(4*x) - 3.5

# Intervalo inferior
a = 0

# Intervalo superior
b = 0.28

# Poner la cota de error de la raíz
e = 1.0e-4

print("Tenemos la funcion f(t) para el intervalo ["+str(a)+","+str(b)+"]\n")

x = biseccion (f, a, b, e)

print("\nLa raíz buscada es: "+str(x))
