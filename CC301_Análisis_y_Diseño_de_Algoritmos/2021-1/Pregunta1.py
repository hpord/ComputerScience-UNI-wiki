#Ingresamos por teclado el tamaño de la memoria
pesomemoria=int(input("Ingrese el tamaño de la memoria: "))
#Ingresamos por teclado el tamaño de cada archivo
numarchivos=int(input("Ingrese el numero de archivos: "))
#Defino una lista vacia
tamaño = []
#Recorro la lista con un FOR para llenarla con los tamaños de cada archivo
for i in range(numarchivos):
    kb = int(input("Ingrese el tamaño del archivo: "))
    tamaño.append(kb)
#Con la funcion SORTED, ordeno de menor a mayor la lista de los tamaños de cada archivo
tamañoordenado = sorted(tamaño)
print(tamañoordenado)
contador = 0
aux = 0
for j in range(numarchivos):
    if (aux + tamañoordenado[j]) < pesomemoria:
        aux = aux + tamañoordenado[j]
        contador = contador + 1
    else:
        break
print("La cantidad de elementos fue: ",contador,"\nEl peso total fue: ",aux)
    

