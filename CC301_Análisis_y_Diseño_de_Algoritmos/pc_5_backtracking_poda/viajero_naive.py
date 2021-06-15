# problema del viajero desde el enfoque de fuerza bruta (naive)
 
from sys import maxsize 
from itertools import permutations


 
def travellingSalesmanProblem(graph, s, V):
    # almacenar todos los vértices aparte del vértice de origen
    vertex = []
    for i in range(V): 
        if i != s:
            vertex.append(i)

    # almacenamos el peso mínimo del ciclo Hamiltoniano
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        # almacenamos el peso de la ruta actual (costo)
        current_pathweight = 0
 
        # calculamos el peso de la ruta actual
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # actualizamos el mínimo
        min_path = min(min_path, current_pathweight)
		
    return min_path


# función principal
if __name__ == "__main__":

    # representación matricial del grafo
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25], 
	         [15, 35, 0, 30], 
             [20, 25, 30, 0]]

    s = 0
    print("\nCoste mínimo : ", end="")
    print(travellingSalesmanProblem(graph, s, V=4))


