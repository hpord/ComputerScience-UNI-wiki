import sys 
import numpy as np
#A = [64, 25, 12, 22, 11] 

A = np.random.rand(1, 1000)
  
# Atravesar todos los elementos de la matriz
for i in range(len(A)): 
      
    # Encuentre el elemento mínimo en la matriz restante sin clasificar
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Intercambia el elemento mínimo encontrado con el primer elemento      
    A[i], A[min_idx] = A[min_idx], A[i] 

'''
print ("El arreglo ordenado es:") 
for i in range(len(A)): 
    print ("%d" %A[i]), 
''' 