# Interpolacion de Lagrange
# Polinomio en forma simbólica
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

print('INTERPOLACIÓN POLINÓMICA DE LAGRANJE',end="\n\n")

print("Es una forma de presentar el polinomio que interpola un conjunto de puntos dado. ",end="\n\n")

# INGRESO , Datos de prueba

'''
# Problema 11 - Dirigida 6 - 20_2
# Datos de X
xi = np.array([30, 40])
# Datos de F(X)
fi = np.array([0.42, 0.46])
# punto a evaluar
x_eval = 32.5
'''


# Problema 12 - Dirigida 6 - 20_2
# Datos de X
#xi = np.array([0.2, 0.4, 0.6, 0.8])
# Datos de F(X)
#fi = np.array([1.22140, 1.49182, 1.82212, 2.22554])
# punto a evaluar
#x_eval = 0.05

# Datos de X
#xi = np.array([12, 14, 16])
# Datos de F(X)
#fi = np.array([0.0830, 0.17136, 0.2020])


xi = np.array([60, 65, 75])
fi = np.array([985.7, 980.5, 974.5])
# punto a evaluar
x_eval = 68



# PROCEDIMIENTO
n = len(xi)
x = sym.Symbol('x')
# Polinomio
polinomio = 0
for i in range(0, n, 1):
    # Termino de Lagrange
    termino = 1
    for j  in range(0, n, 1):
        if (j!=i):
            termino = termino*(x-xi[j])/(xi[i]-xi[j])


    print("El L(",i,") es :", termino)
    polinomio = polinomio + termino*fi[i]
# Expande el polinomio
px = polinomio.expand()

# para evaluacion numérica
pxn = sym.lambdify(x, polinomio)

# Puntos para la gráfica
a = np.min(xi)
b = np.max(xi)

muestras = 100
xi_p = np.linspace(a, b, muestras)
fi_p = pxn(xi_p)

# Salida
print('\nPolinomio de Lagrange, expresiones:')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(px)

print(f'\nEvaluando en {x_eval}: ', end="")
print(pxn(x_eval))

# Gráfica
plt.title('Interpolación Lagrange')
plt.plot(xi, fi, 'o', label = 'Puntos')
plt.plot(xi_p, fi_p, label = 'Polinomio')
plt.legend()
plt.show()
