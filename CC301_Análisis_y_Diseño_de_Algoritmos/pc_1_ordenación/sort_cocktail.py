import numpy as np

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
 
        # restablece la bandera intercambiada al entrar en el bucle, 
        # porque podría ser cierto en una iteración anterior.
        swapped = False
 
        # bucle de izquierda a derecha igual que el tipo de burbuja
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
 
        # si no se mueve nada, entonces la matriz se ordena.
        if (swapped == False):
            break
 
        # de lo contrario, restablezca la bandera 
        # intercambiada para que pueda usarse en la siguiente etapa
        swapped = False
 
        # mueva el punto final hacia atrás en uno, porque el 
        # elemento al final está en el lugar que le corresponde
        end = end-1
 
        # de derecha a izquierda, haciendo la misma comparación que en la etapa anterior
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
 
        # aumentar el punto de partida, porque la última etapa habría 
        # movido el siguiente número más pequeño al lugar que le corresponde.
        start = start + 1
 

#a = [5, 1, 4, 2, 8, 0, 2]
a = np.random.rand(1, 1000)
cocktailSort(a)
'''
print ("El arreglo ordenado es:") 
for i in range(len(a)):
    print("% d" % a[i])
'''