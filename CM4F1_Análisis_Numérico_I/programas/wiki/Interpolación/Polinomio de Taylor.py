import sympy as sy
import numpy as np
from sympy.functions import sin, cos
import matplotlib.pyplot as plt
# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor approximation at c of the function 'function'
def taylor(function, c, n):
    """
    taylor
    -------
    Transforma una funcion complicada a un polinomio por derivadas

    Parametros
    ------------
    function - funcion a transformar
    c - centro de la aproximacion
    n - grado del polinomio

    """
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, c))/(factorial(i))*(x-c)**i
        i += 1
    return p

if __name__ == '__main__':

    print("INTERPOLACIÓN POLINÓMICA DE TAYLOR\n")
    print("La Interpolación de Taylor usa el desarrollo de Taylor de una función en un punto para construir un polinomio de grado 'n' que se aproxima a la función dada.\n")

    # Defines la variable
    x = sy.Symbol('x')

    # Defines la funcion que se va aproximar con Taylor
    f = sin(x)

    func = taylor(f, 0, 4)
    print("La funcion 'f(x)' es: ",end="")
    print(func)

    # Evaluacion en un punto
    y = 5
    print("\nEvaluando en el punto x =", y,":",func.subs(x, y))


    #grafica
    # Puntos para la gráfica
    #a = np.min(xi)
    #b = np.max(xi)
    muestras = 100
    xi_p = np.linspace(-5, 5,muestras)
    fi_p = np.zeros(muestras)
    for i in range(muestras):
        fi_p[i]=func.subs(x,xi_p[i])

    # Gráfica
    plt.title('Polinomio de Taylor')
    plt.plot(xi_p, fi_p, label = 'Polinomio')
    plt.legend()
    plt.show()
