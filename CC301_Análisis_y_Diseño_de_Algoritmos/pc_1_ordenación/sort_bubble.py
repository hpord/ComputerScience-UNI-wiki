import os
import numpy as np
def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n-1): 

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  

arr = np.random.rand(1, 1000)
#arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 

''' 
print ("El arreglo ordenado es:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  
'''