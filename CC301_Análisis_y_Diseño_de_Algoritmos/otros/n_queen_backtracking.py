# Python program to solve N Queen using backtracking 
global N 
N = 5
  
def printSolution(board): 
    print("\n")
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end="  ") 
        print("\n")
  

def isSafe(board, row, col): 
      
    """
    Una función de utilidad para comprobar si una reina puede ser colocado en  Tabla[fila] [col]. 
    Tenga en cuenta que esta función se llama cuando las reinas "col" ya están colocadas en las columnas de 0 a col -1.
    Así que tenemos que comprobar solo el lado izquierdo para atacar a las reinas.
    """
    
    # Comprueba esta fila en el lado izquierdo
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Comprueba la diagonal superior en el lado izquierdo 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Comprueba la diagonal inferior en el lado izquierdo
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True
  
def solveNQUtil(board, col): 

    # caso base: si se colocan todas las reinas, devuelve verdadero
    if col >= N: 
        return True
  
    # Considere esta columna e intente colocar esta reina en todas las filas una por una
    for i in range(N): 
  
        if isSafe(board, i, col): 
            # Coloca esta reina en el tablero[i][col] 
            board[i][col] = 1
  
            # recurrir a colocar el resto de las reinas 
            if solveNQUtil(board, col + 1) == True: 
                return True
  
            # Si colocar reina en el tablero [i] [col]
            # no conduce a una solución, entonces reina del tablero[i][col] = 0
            board[i][col] = 0
  
    # si la reina no se puede colocar en ninguna fila en esta columna, devuelva falso
    return False
  

def solveNQ(): 

    """
    Esta función resuelve el problema de N Queen usando Backtracking. Utiliza principalmente solveNQUtil() para
    resolver el problema. Devuelve falso si no se pueden colocar reinas; de lo contrario, devuelve verdadero y
    la colocación de reinas en forma de 1.
    Tenga en cuenta que puede haber más de una solución, esta función imprime una de las soluciones factibles.
    """

    board = [ [0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],  
              [0, 0, 0, 0, 0] 
             ] 
  
    if solveNQUtil(board, 0) == False: 
        print("No existe solucion")
        return False
  
    printSolution(board) 
    return True
  


if __name__ == '__main__':

    """
    Algoritmo Backtracking 
    
    La idea es colocar reinas una por una en diferentes columnas, comenzando desde la columna más a la izquierda. Cuando colocamos a una reina en una columna, buscamos enfrentamientos con reinas ya colocadas. En la columna actual, si encontramos una fila para la que no hay ningún conflicto, marcamos esta fila y columna como parte de la solución. Si no encontramos una fila de este tipo debido a los conflictos, entonces retrocedemos y devolvemos falso.

    1) Comience en la columna más a la izquierda

    2) Si se colocan todas las reinas volver verdadero

    3) Pruebe todas las filas de la columna actual.
        Haga lo siguiente para cada fila probada.
            a) Si la reina se puede colocar con seguridad en esta fila
               entonces marque esta [fila, columna] como parte del
               solución y compruebamos de forma recursiva si colocar
               reina en esta posición lleva a una solución.
            b) Si colocar la reina en [fila, columna] conduce a
               una solución entonces devuelve verdadero.
            c) Si colocar reina no conduce a una solución, entonces
               desmarque esta [fila, columna] (Retroceder) y vaya a
               paso (a) para probar otras filas.

    4) Si se han probado todas las filas y nada funcionó, devuelve falso para activar el retroceso.

    """
    # probamos la función
    solveNQ() 