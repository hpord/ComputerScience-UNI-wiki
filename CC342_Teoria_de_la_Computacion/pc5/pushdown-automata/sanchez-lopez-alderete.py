import os

start_input = "" # input word to be found or not found
found = 0 # stores found state
accepted_config = [] # here we will post end configuration that was accepted

# reglas de producción ("read input", "pop stack", "push stack", "next state")
productions = {}

# todos los estados o no terminales (no es realmente necesario)
states = []

# lista de símbolos alfabéticos o terminales (no es realmente necesario)
symbols = []

# lista de símbolos del alfabeto de pila (no es realmente necesario)
stack_symbols = []

# estado inicial
start_symbol = ""

# símbolo de pila de inicio
stack_start = ""

# lista de estados aceptables
acceptable_states = []

# E - aceptar en pila vacía o F - estado aceptable (el valor predeterminado es falso)
accept_with = ""



# Genere de forma recursiva todo el árbol posible y finalice con éxito
def generate(state, input, stack, config):
	global productions
	global found

	total = 0

	# comprobamos el éxito de otro nodo de árbol
	if found:
		return 0

	# comprobamos si nuestro nodo puede terminar con éxito
	if is_found(state, input, stack):
		found = 1 # marcamos que la palabra es aceptada 
				  # para que otros nodos del árbol sepan y terminen 

		
		# añadimos satisfactoriamente la configuración
		accepted_config.extend(config)

		return 1

	# verificamos si hay más movimientos (o tenemos que terminar) 
	moves = get_moves(state, input, stack, config)
	if len(moves) == 0:
		return 0

	
	# para cada movimiento creamos un árbol
	for i in moves:
		total = total + generate(i[0], i[1], i[2], config + [(i[0], i[1], i[2])])  

	return total


# verificamos si el símbolo es terminal o no-terminal
def get_moves(state, input, stack, config):
	global productions

	moves = []

	for i in productions:

		if i != state:
			continue

		for j in productions[i]:
			# print(j)
			current = j
			new = []

			new.append(current[3])

			
			# leemos el símbolo de la cadena de entrada,
			# si es que nosotros tenemos uno
			if len(current[0]) > 0:
				if len(input) > 0 and input[0] == current[0]:
					new.append(input[1:])
				else:
					continue
			else:			
				new.append(input)

			# leemos el símbolo de la pila
			if len(current[1]) > 0:
				if len(stack) > 0 and stack[0] == current[1]:
					new.append(current[2] + stack[1:])
				else:
					continue
			else:
				new.append(current[2] + append)

			moves.append(new)

	return moves


# comprobamos si la palabra ya se generó en algún lugar del pasado
def is_found(state, input, stack):
	global accept_with
	global acceptable_states

	# comprobamos si se leen todos los símbolos
	if len(input) > 0: 
		return 0

	# comprobamos si aceptamos con pila vacía o estado final
	if accept_with == "E":
		if len(stack) < 1:  # aceptar si la pila está vacía
			return 1

		return 0

	else:
		for i in acceptable_states:
			if i == state: # aceptar si estamos en estado terminal
				return 1

		return 0


# imprimimos lista de configuración actual
def print_config(config):
	
	for i in config:
		print(i) 


def parse_file(filename):
	global productions
	global start_symbol
	global start_stack
	global acceptable_states
	global accept_with

	try:
		lines = [line.rstrip() for line in open(filename)]

	except:
		return 0

	# añadimos el estado inicial
	start_symbol = lines[3]

	# añadimos símbolo de pila de inicio
	start_stack = lines[4]

	# lista de estados aceptables
	acceptable_states.extend(lines[5].split())

	# E: aceptar en pila vacía o F: estado aceptable (el valor predeterminado es falso)
	accept_with = lines[6] 

	# agregamos las reglas
	for i in range(7, len(lines)):
		production = lines[i].split()

		configuration = [(production[1], production[2], production[4], production[3])]

		if not production[0] in productions.keys(): 
			productions[production[0]] = []

		configuration = [tuple(s if s != "e" else "" for s in tup) for tup in configuration]

		productions[production[0]].extend(configuration)
    
	print("\nProducciones: ")
	for k in productions:
		print(k, ": ", productions[k])
	
	print("\nSímbolo inicial:  ", start_symbol)
	print("Elemento pila inicial:  ",start_stack)
	print("Estados de aceptación:  ",acceptable_states)
	print("Aceptación con:  ", accept_with)

	return 1


# comprobamos si el símbolo es terminal o no terminal
def done():
	if found:
		print("\nLa cadena de entrada \"" + start_input + "\" es parte del lenguaje de aceptación.") 
	else:
		print("\nLa cadena de entrada \"" + start_input + "\" NO es parte del lenguaje de aceptación.") 



# Aqui ingresamos la ruta del archivo en forma de texto
filename = input("\nIngrese la ruta del archivo de autómatas:  ")
while not parse_file(filename):
	print("Archivo inválido!")
	filename = input("Ingrese la ruta del archivo de autómatas nuevamente:  ")
print("\nAutómata construido\n")

start_input = input("Por favor ingrese su palabra:  ")
print("\nVerificando palabra \"" + start_input + "\" ...\n")




while start_input != "FIN":
	# la magia comienza aquí
	if not generate(start_symbol, start_input, start_stack, [(start_symbol, start_input, start_stack)]):
		done()
	else:
		print_config(accepted_config) # mostramos lista de configuraciones para aceptación
		done()

	print("\n-------------------------------------------------\n")
	start_input = input("Ingrese la siguiente palabra (o FIN):  ")
	print("Verificando palabra \"" + start_input + "\" ...")

	

