# Implementación de 'Rat in a Maze' <-> 'Rata en un laberinto' <-> 'Laberinto'

from typing import List
import numpy as np

MAX = 10

# La función devuelve TRUE si el
# movimiento tomado es válido, sino
# se retorna FALSE.
def isSafe(row: int, col: int, 
		m: List[List[int]], n: int,
		visited: List[List[bool]]) -> bool:

	if (row == -1 or row == n or
		col == -1 or col == n or
		visited[row][col] or m[row][col] == 0):
		return False

	return True

# Función para imprimir todas las posibles
# rutas desde (0, 0) hasta (n-1, n-1).
def printPathUtil(row: int, col: int, 
				m: List[List[int]], 
				n: int, path: str,
				possiblePaths: List[str], 
				visited: List[List[bool]]) -> None:

	# Verificamos la posición inicial
	# (es decir. (0, 0)) para comenzar las rutas
	if (row == -1 or row == n or
		col == -1 or col == n or
		visited[row][col] or m[row][col] == 0):
		return

	# Si llega a la última celda (n-1, n-1)
	# entonces se almacena la ruta y retornamos
	if (row == n - 1 and col == n - 1):
		possiblePaths.append(path)
		return

	# Marcamos la celda como visitada
	visited[row][col] = True

	# Probamos las 4 direcciones (abajo (D), izquierda (l),
	# derecha (R), arriba (U)) en el orden dado para obtener
	# las rutas en orden lexicográfico

	# Comprobamos si el movimiento hacia abajo es válido
	if (isSafe(row + 1, col, m, n, visited)):
		path += 'D'
		printPathUtil(row + 1, col, m, n, 
					path, possiblePaths, visited)
		path = path[:-1]

	# Comprobamos si el movimiento hacia la izquierda es válido
	if (isSafe(row, col - 1, m, n, visited)):
		path += 'L'
		printPathUtil(row, col - 1, m, n, 
					path, possiblePaths, visited)
		path = path[:-1]

	# Comprobamos si el movimiento hacia la derecha es válido
	if (isSafe(row, col + 1, m, n, visited)):
		path += 'R'
		printPathUtil(row, col + 1, m, n,
					path, possiblePaths, visited)
		path = path[:-1]

	# Comprobamos si el movimiento hacia arriba es válido
	if (isSafe(row - 1, col, m, n, visited)):
		path += 'U'
		printPathUtil(row - 1, col, m, n,
					path, possiblePaths, visited)
		path = path[:-1]

	# Marcamos la celda como no visitada para
	# otras posibles rutas
	visited[row][col] = False


def printMatrix(stringPath, n):
    matrix = np.zeros(shape=(n, n))

    i, j = 0, 0    
    matrix[i][j] = 1

    for letter in stringPath:
        if letter == 'L':
            j -= 1
            matrix[i][j] = 1

        if letter == 'R':
            j += 1
            matrix[i][j] = 1
        
        if letter == 'U':
            i -= 1
            matrix[i][j] = 1
        
        if letter == 'D':
            i += 1
            matrix[i][j] = 1

    print(matrix)

# función para almacenar e imprimir
# todas las rutas válidas
def printPaths(m: List[List[int]], n: int, showStringPath: bool):

    # almacenamos todas las posibles rutas
    possiblePaths = []
    path = ""
    visited = [[False for _ in range(MAX)] for _ in range(n)]
					
    # llamamaos a la función de utilidad para
    # encontrar las rutas válidas
    printPathUtil(0, 0, m, n, path, possiblePaths, visited)
    print("--------------------------------------------", end="\n")
    for i, p in enumerate(possiblePaths):
       print(f"\nMostrando solución {i+1}: ", end="\n\n")
       printMatrix(stringPath=p, n=n)
       print("--------------------------------------------", end="\n")
    
    if showStringPath:
        print("\nMostrando todas las cadenas las rutas: \n")
        for i in range(len(possiblePaths)):
            print(possiblePaths[i], end = " ")
    print("\n\n")

if __name__ == "__main__":
	
    
    m10 = [ [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
	        [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
	        [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
	        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
	        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
	        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
	        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
	        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1] ]
    n10 = len(m10)
    printPaths(m=m10, n=n10, showStringPath=True)
    



    """ m5 = [ [1, 1, 0, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1]]
    
    n5 = len(m5)
    printPaths(m=m5, n=n5, showStringPath=True) """
	

    '''
    bad = [ [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
			[1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
			[1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
			[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
			[1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
			[1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
			[1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
			[1, 1, 1, 1, 1, 0, 1, 1, 1, 1] ]

    b = len(bad)
    printPaths(m=bad, n=b, showStringPath=False)
    '''
