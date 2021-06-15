# problema del viajero desde el enfoque de poda y ramificación (Branch y Bound)
 
import math 
import matplotlib.pyplot as plt
import time
import numpy as np
from os import listdir
from os.path import isfile, join
from viajero_naive import travellingSalesmanProblem

maxsize = float('inf') 


def copyToFinal(curr_path):
    """
    Función para copiar la solución temporal a la solución final
    """

    final_path[:N + 1] = curr_path[:] 
    final_path[N] = curr_path[0] 


def firstMin(adj, i): 

    """
    Función para encontrar el costo de arista mínimo que tiene un final en el vértice i
    """

    min = maxsize 
    for k in range(N): 
        if adj[i][k] < min and i != k: 
            min = adj[i][k] 

    return min


def secondMin(adj, i): 
    """
    Función para encontrar el segundo costo de arista mínimo que tiene un final en el vértice 'i'
    """

    first, second = maxsize, maxsize 
    for j in range(N): 
        if i == j: 		
            continue
        if adj[i][j] <= first: 
            second = first
            first = adj[i][j] 
	
        elif(adj[i][j] <= second and adj[i][j] != first):
            second = adj[i][j] 

    return second 

 
def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited): 

    """
    función que toma como argumentos:

    - curr_bound -> límite inferior del nodo raíz
    - curr_weight -> almacena el peso de la ruta hasta ahora
    - level -> nivel actual mientras se mueve  en el árbol 
              del espacio de búsqueda
    - curr_path [] -> donde se almacena la solución que luego 
                      se copiaría a final_path 

    """
    global final_res 
	
    # El caso base es cuando hemos alcanzado el nivel N, lo que 
    # significa que hemos cubierto todos los nodos una vez.
    if level == N:

    # compruebe si hay una arista desde el último vértice 
    # en la ruta de regreso al primer vértice 
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
			
	    # curr_res tiene el peso total de la solución
            # que obtuvimos
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res 
        return

    # para cualquier otro nivel, iterar para todos los vértices 
    # para construir el árbol del espacio de búsqueda de 
    # forma recursiva
    for i in range(N): 
		
        # Considere el siguiente vértice si no es el mismo 
        # (entrada diagonal en la matriz de adyacencia y no 
        # se ha visitado ya)
        if(adj[curr_path[level-1]][i] != 0 and visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i] 

	    # cálculo diferente de curr_bound para el nivel 2 
            # de los otros niveles
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2) 

	        # curr_bound + curr_weight es el límite inferior 
            # real para el nodo al que hemos llegado.
	        # Si el límite inferior actual <final_res, 
            # necesitamos explorar más el nodo
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
				
	        # llamamos a TSPRec para el siguiente nivel
                TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited) 

	        # De lo contrario, tenemos que podar el nodo 
            # reiniciando todos los cambios a curr_weight 
            # y curr_bound
            curr_weight -= adj[curr_path[level - 1]][i] 
            curr_bound = temp 

	    # También restablece la matriz visitada
            visited = [False] * len(visited)
            for j in range(level):
               if curr_path[j] != -1:
                  visited[curr_path[j]] = True


def TSP(adj): 
    """
    Esta función configura final_path
    """
	
	# Calcule el límite inferior inicial para el nodo raíz 
    # usando la fórmula 1/2 * (suma del primer min + segundo min) para todas las aritas. También inicialice curr_path y 
    # la matriz visitada
    curr_bound = 0
    curr_path = [-1] * (N + 1)  
    visited = [False] * N 

    # Calcular el límite inicial
    for i in range(N): 
        curr_bound += (firstMin(adj, i) + secondMin(adj, i)) 

    # Redondear el límite (la ramificación) inferior a un 
    # número entero
    curr_bound = math.ceil(curr_bound / 2) 

    # Comenzamos en el vértice 1, por lo que el primer vértice en curr_path [] es 0 
    visited[0] = True
    curr_path[0] = 0

    # Llamamos a TSPRec para curr_weight igual a 0 y nivel 1
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited) 


def plot(data, nameAxis, nameTitle):
    """
    función para graficar 
    """

    colors = ['b', 'm', 'y', 'g', 'r', 'k', 'w', 'c']
    for indexColor, axis in enumerate(data):

        nameData, axisX, axisY = axis
        plt.plot(axisX, axisY, color=colors[indexColor], linestyle='dashed', linewidth = 3, 
                 marker='o', markersize=10, label = nameData)

    # nombramos los ejes
    nameX, nameY = nameAxis
    plt.xlabel(nameX)
    plt.ylabel(nameY) 

    # escribimos el 'título del gráfico 
    plt.title(nameTitle)

    # añadimos las leyendas
    plt.legend() 
    plt.show()    


if __name__ == '__main__':

    
    files = [f for f in listdir('./matrices/') if isfile(join('./matrices/', f))]
    
    sizeMatrix = []

    timeNaive = []
    timePrune = []

    for file_name in files:

        print("\n----------------------------------\n")
        
        
        # Matriz de adyacencia para el grafo dado
        adj = np.loadtxt(f'./matrices/{file_name}', delimiter=',')
        N = adj.shape[0]
        sizeMatrix.append(N)
        print(f'Dimensión : {N}\n')


        print("Ejecutando algoritmo de fuerza bruta...")
        s = 0
        start_1 = time.time()
        a1 = travellingSalesmanProblem(graph=adj, s=s, V=N)
        done_1 = time.time()
        timeNaive.append(done_1 - start_1)


        # final_path [] almacena la solución final
        # es decir, el // camino del viajero.
        final_path = [None] * (N + 1) 

        # visited[] realiza un seguimiento de los nodos 
        # ya visitados en una ruta particular
        visited = [False] * N 

        # Almacena el peso mínimo final del recorrido más corto.
        final_res = maxsize 

        
        print("\nEjecutando algoritmo de Poda...")
        start_2 = time.time()
        TSP(adj=adj)
        done_2 = time.time()
        timePrune.append(done_2 - start_2)

        # si los resultados son diferentes, lanza un assertion,
        # para corregir este error, genere nuevas matrices e
        # intente de nuevo
        a2 = final_res
        assert a1==a2, a1 + " y " + a2

        
        print("\nCoste mínimo :", final_res) 
        print("\nRuta tomada : ", end = ' ') 
        for i in range(N + 1): 
            print(final_path[i], end = ' ')

    print("\n\n")

    data = [['Fuerza bruta', sizeMatrix, timeNaive], ['Poda', sizeMatrix, timePrune]]
    nameAxis = ['Tamaño de la matriz de adyacencia', 'tiempo (s)']
    nameTitle = 'Fuerza bruta VS Método de poda'
    plot(data=data, nameAxis=nameAxis, nameTitle=nameTitle)