"""
Implementacion del metodo de newton
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def newton_poly(x, y):
    """
    Calculo de la ecuacion del polinomio de newton
    
    input
    x, y: puntos (x, y) a interpolar
    
    output:
    polinomio simbolico  de la forma newton que interpola los puntos (x, y)
    """

    t = sp.symbols('t')
    
    n = len(x)
    pn = 0*t #inicializando el polinomio de newton
    c = coeff_newton_poly(x, y)
    
    for k in range(n):
        pn += c[k]*np.prod([(t-x[j]) for j in range(k)])
    print("Polinomio de Newton")
    print('P(t) = '+ str(pn))
 
    return pn



def coeff_newton_poly(x, y):
    """
    Calcula los coeficientes del polinomio de interpolacion
    de la forma de newton
    
    input
    x, y: puntos (x, y) a interpolar
    
    output:
    array con coefientes del polinomio de interpolacion
    de la forma de newton. 
    """

    n = len(x)
    c = np.array([y[0]])  # coeficientes del polinomio de interpolacion
    
    for k in range(1, n):
        d = x[k] - x[k-1]
        u = c[k-1]
        for i in range(k-2, -1, -1):
            u = u*(x[k] - x[i]) + c[i]
            d *= x[k] - x[i]
        c = np.append(c, (y[k]-u)/d)
    print("Coeficientes del polinomio: ")
    print(c[::-1], end="\n\n")
    
    return c


def plot_newton_poly(f, x, y, DISCRET=1000):
    """
    Grafica el polinomio de newton que interpola los puntos (x, y)

    input
    f: funcion simbolica definida con la funcion lambda
    x, y: puntos interpolados (xi, yi)

    ouput
    grafica del polinomio de lagrange en [a, b]
    """
    a, b = min(x), max(x)
    xab = np.linspace(a, b, DISCRET) #discretizacion del intervalo [a, b]

    fxab = np.array([])
    for u in xab:
        fxab = np.append(fxab, f(u))
    
    plt.plot(x, y, "o")
    plt.plot(xab, fxab, label="Newton")
    plt.title("Polinomio de interpolacion de la forma de newton")
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

if __name__=='__main__':
	x = np.array([50, 60, 65, 75, 80])
	y = np.array([988, 985.7, 980.5, 974.5, 971.6])
	f = newton_poly(x, y)
	plot_newton_poly(sp.lambdify(f.free_symbols,f), x, y)
