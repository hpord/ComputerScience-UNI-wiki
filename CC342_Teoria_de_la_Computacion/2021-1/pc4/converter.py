#  NFA
class NFA:
    # Initialize NFA
    def __init__(self, S, s0, F, move):
        self.S = S  # (list)
        self.s0 = s0  # (int)
        self.F = F  # (int)
        self.move = move  # state conversion function (list set dict)

	# Calcula el n del conjunto de estados T (en lugar de ε) cierre U
    def getClausura(self, T):
        U = list()  # Coleccion de clausura
        Stack = list()  
        for t in T:
            Stack.append(t)  # pone t en el stack
            U.append(t)  # pone t en U
        # Cuando la stack no está vacía
        while Stack:
            t = Stack.pop()  
            #Si se puede convertir (determine si la clave es 'e' en el diccionario)
            if 'e' in move[t]:
                u = self.move[t]['e'] # obtener el estado después de la conversión u
                 # Si el estado después de la conversión no está en el conjunto de cierre U, sume u a U
                if u not in U:
                    # debido a que u es una lista , se puede hacer un loop
                    for x in u:
                        Stack.append(x)
                        U.append(x)
            # Si no se puede convertir
            else:
                pass
              
        return U

    # metodo smove, T es el conjunto de estados inicial, n es el carácter que se va a reconocer (tipo str) y devuelve el conjunto de estados convertido U
    def smove(self, T, n):
        U = list()  # Almacena el estado establecido después de smove
        for t in T:
            # Si se puede convertir (determine si la clave es 'e' en el diccionario)
            if n in move[t]:
                u = self.move[t][n]  # obtener el estado después de la conversión u
                 # Si el estado después de la conversión no está en el conjunto de cierre U, sume u a U
                if u not in U:
                    # debido a que u es una lista , se puede hacer un loop
                    for x in u:
                        U.append(x)
             # Si no se puede convertir
            else:
                pass
        return U


#  DFA
class DFA:
    # Construct DFA through NFA object N
    def __init__(self, N):
        
        self.s0 = N.getClausura([0])  # (list)
        self.Dstates = [self.s0]  # Almacena el estado del DFA
        self.DstatesFlag = [0]  # El estado del registro está marcado, el número de elementos representa el número que no se ha marcado
        self.F=N.F
        curIndex = 0  # El subíndice de los Estados actualmente procesados
        Dtran = list() # Matriz de transición de estado
        U1 = list()# , utilizado para almacenar el conjunto de estados convertido, fácil de escribir en la matriz de transformación
        U2 = list()# 
        # 
        while self.DstatesFlag:
            self.DstatesFlag.pop()  # Cuando el conjunto de estados de DFA tiene un estado sin marcar T
            # 
            for ch in ['a', 'b']:
                # Encuentra el cierre U después del smove
                U = N.getClausura(N.smove(self.Dstates[curIndex], ch))
                #formato de escritura de construcción de juicio condicional Dtran.append ({'a': U1, 'b': U2})
                if ch == 'a':
                    U1 = U
                else:
                    U2 = U
                # Si U no está en Dstates,se agrega U como un estado sin etiquetar a Dstates
                if U not in self.Dstates:
                    self.Dstates.append(U)#Agrega U al conjunto de estados
                    self.DstatesFlag.append(0)#longitud incrementada en 1, lo que indica un estado sin marcar
                    

            Dtran.append({'a': U1, 'b': U2})#Escribe el resultado de la conversión en la matriz de conversión.
            curIndex+=1 # 1

        self.move = Dtran  # Construir función de transición de estado (conjunto de lista dictado)
        print("AFD estado inicial s0:",self.s0)
        print("AFD estado final F:", self.F)
        print("AFD estados:", self.Dstates)
        print("AFD estados de transicion:", self.move)

        print('Ingrese una cadena :')

    #Analiza un imput para el automata
    def isAccept(self, x):
        print('Analizando para la cadena:',x)
        #  reconoce la cadena
        for ch in x:
            # Debido a que el estado en Dstatea se agrega en orden, el subíndice de objeto A set 0, B corresponde al subíndice 1
             # y la matriz de movimiento también se almacena de esta manera, obtenga el subíndice del estado actual establecido en Dstates
            curindex=self.Dstates.index(self.s0)
            # 
            if ch not in ['a', 'b']:
                break
            self.s0=self.move[curindex][ch]
            print('El estado actual es : ', self.s0)
            #Si el subíndice del conjunto de estados convertido es igual a la longitud de Dstates -1
             # El estado actual de transición es el estado final de Dstates, es decir, el estado final

        if self.F in self.s0:
            print('La cadena ',x,'es Aceptada')
        else:
            print('La cadena ',x,'es rechazada ')
        return 0


if __name__ == '__main__':
    # NFA Start
    #S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Ingrese los estados :")
    S =  eval(input(":"))
    # s0 = 0
    s0 = int(input("Ingrese el estado inicial : "))
    # F = 10
    F = int(input("Ingrese el estado final:"))
    #move = [{'e': [1, 7]}, {'e': [2, 4]}, {'a': [3]}, {'e': [6], }, {'b': [5]}, {'e': [6]}, {'e': [1, 7]}, {'a': [8]}, {'b': [9]}, {'b': [10]},{}]
    print("Ingrese la matriz de transicion : ")
    move = eval(input(":"))

    N = NFA(S, s0, F, move)
    print("Conversion completa :")
    # Construct NFA End

    D=DFA(N)#Build DFA through NFA object N

    #print(D.move)# Output DFA conversion matrix
    while True:
        x = input('Ingrese una cadena:')# 
        if x=='quit' or x=='exit':
            print('Fin del programa')
            break
        D.isAccept(x)