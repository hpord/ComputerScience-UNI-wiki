import numpy as np
import random
from time import sleep

# Creamos el tablero
def create_board():
	return(np.array([[1, 2, 3],
					[4, 5, 6],
					[7, 8, 9]]))


def DisplayBoard(board):
    '''
    la funcion acepta un parametro el cual contiene el estado actual del tablero
    y lo muestra en la consola
    '''
    for row in range(3):
        for column in range(3):
            if board[row][column] in ('X', 'O'):
                print(board[row][column], end=' ')
            else: 
                print("  ", end=' ')
        print("\n\n")


def EnterMove(board):
    '''
    la funcion acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    verifica la entrada y actualiza el tablero acorde a la decision del usuario
    '''
    position = int(input("Ingrese la posición a marcar: "))
    _, positionsOkay = listFreeFields(board)

    while True:
        if position in positionsOkay:
            print("Posición valida..agregando..")
            break
        else:
            position = int(input("Vuelve a ingresar una posición vacía: "))




def MakeListOfFreeFields(board):
    '''
    la función examina el tablero y construye una lista de todos los cuadros vacios
    la lista esta compuesta por tuplas, cada tupla es un par de numeros que indican la fila y columna
    '''
    position = 0
    positionsOkay = []
    listFreeFields = []
    for row in range(3):
        for column in range(3):
            position += 1
            if board[row][column] in ('X', 'O'):
                continue
            else: 
                tup = (row, column)
                listFreeFields.append(tup)
                positionsOkay.append(position)
    return listFreeFields, positionsOkay

def DrawMove(board):
    '''
    la funcion dibuja el movimiento de la maquina y actualiza el tablero
    '''
	selection = possibilities(board)
	current_loc = random.choice(selection)
	board[current_loc] = player
	return(board)

# Check for empty places on board
def possibilities(board):
	l = []
	
	for i in range(len(board)):
		for j in range(len(board)):
			
			if board[i][j] == 0:
				l.append((i, j))
	return(l)

# Checks whether the player has three
# of their marks in a horizontal row
def row_win(board, player):
	for x in range(len(board)):
		win = True
		
		for y in range(len(board)):
			if board[x, y] != player:
				win = False
				continue
				
		if win == True:
			return(win)
	return(win)

# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
	for x in range(len(board)):
		win = True
		
		for y in range(len(board)):
			if board[y][x] != player:
				win = False
				continue
				
		if win == True:
			return(win)
	return(win)

# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
	win = True
	y = 0
	for x in range(len(board)):
		if board[x, x] != player:
			win = False
	if win:
		return win
	win = True
	if win:
		for x in range(len(board)):
			y = len(board) - 1 - x
			if board[x, y] != player:
				win = False
	return win

def VictoryFor(board, sign):
    '''
    la función analiza el estatus del tablero para verificar si
    el jugador que utiliza las Os o las Xs ha ganado el juego
    '''
    winner = 0
	
	if (row_win(board, sign) or
		col_win(board, sign) or
		diag_win(board, sign)):
				
			winner = player
			
	if np.all(board != 0) and winner == 0:
		winner = -1
    
    return winner
    

# Main function to start the game
def play_game():
	board, winner, counter = create_board(), 0, 1
	print(board)
	sleep(2)
	
	while winner == 0:
		for player in [1, 2]:
			board = random_place(board, player)
			print("Board after " + str(counter) + " move")
			print(board)
			sleep(2)
			counter += 1
			winner = evaluate(board)
			if winner != 0:
				break
	return(winner)
