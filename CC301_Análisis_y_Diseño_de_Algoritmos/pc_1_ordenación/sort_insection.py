import numpy as np

def insertionSort(arr): 
   
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Mover elementos de arr [0..i-1], que son mayores que key, 
        # a una posición por delante de su posición actual
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
 

##arr = [12, 11, 13, 5, 6] 
arr = np.random.rand(1, 1000)
insertionSort(arr) 
'''
print ("El arreglo ordenado es:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 
'''