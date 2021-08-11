import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from numpy import pi

'''
Los modelos 3, 5, 6 se ajuntan mejor a los datos, 
por la forma trigonométrica de las funciones que las aproximan

Se dice que un modelo es bueno si lograr generalizar para más
datos al momento de realizar una predicción, es decir que NO SE
SOBREAJUSTA, y analizando las gráficas, el modelo 3 y 5 son los más
adecuados, mientras que el modelo 6 se sobreajusta demasiado a los puntos
'''

def f1(x, a, b):
    return a + b*x

def f2(x, a, b, c):
    return a + b*x + c*(x**2)

def f3(x, a, b, c, d):
    return a + b*x + c*(x**2) + d*(x**3)

def f4(x, a, b, c):
    return a + b*np.cos(pi*x/12)

def f5(x, a, b, c):
    return a + b*np.cos(pi*x/12) + c*np.sin(pi*x/12)

def f6(x, a, b, c, d):
    return a + b*np.cos(pi*x/12) + c*np.sin(pi*x/12) + d*np.cos(pi*x/6)


if __name__ == '__main__':
    
    x = np.array([i for i in range(1, 25)])
    y = np.array([14.8881681, 14.4440225,12.0525027,12.3675752,10.5481282,11.3863987,10.4983225,11.6639894,13.2694491,13.8989505,15.9316936,16.1416243,18.0017962,16.812276,17.5279966,18.5225393,16.9323199,16.980208,15.9428553,17.300932,16.4823317,16.023381,15.0768652,14.6712449])

    xn = np.linspace(0, 24, 200)
    plt.plot(x, y, 'or')

    p0 = [3, 4]
    popt, pcov = optimize.curve_fit(f1, x, y, p0=p0)
    print(f"Parametros para el modelo 1: {popt}\n")
    plt.plot(xn, f1(xn, *popt), label='Modelo 1')

    
    p0 = [3, 4, 3]
    popt, pcov = optimize.curve_fit(f2, x, y, p0=p0)
    print(f"Parametros para el modelo 2: {popt}\n")
    plt.plot(xn, f2(xn, *popt),label='Modelo 2')

    p0 = [3, 4, 3, 3]
    popt, pcov = optimize.curve_fit(f3, x, y, p0=p0)
    print(f"Parametros para el modelo 3: {popt}\n")
    plt.plot(xn, f3(xn, *popt), label='Modelo 3')

    p0 = [3, 4, 3]
    popt, pcov = optimize.curve_fit(f4, x, y, p0=p0)
    print(f"Parametros para el modelo 4: {popt}\n")
    plt.plot(xn, f4(xn, *popt), label='Modelo 4')

    p0 = [3, 4, 3]
    popt, pcov = optimize.curve_fit(f5, x, y, p0=p0)
    print(f"Parametros para el modelo 5: {popt}\n")
    plt.plot(xn, f5(xn, *popt), label='Modelo 5')


    p0 = [3, 4, 3, 3]
    popt, pcov = optimize.curve_fit(f6, x, y, p0=p0)
    print(f"Parametros para el modelo 6: {popt}\n")
    plt.plot(xn, f6(xn, *popt), label='Modelo 6')

    plt.legend()
    plt.show()