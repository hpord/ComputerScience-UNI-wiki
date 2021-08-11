class AFD:
    def __init__(self):
        self.estados = ['S0', 'S1', 'S2']
        self.estado_aceptacion = None
        self.identificador_OK = None
        self.estado_inicial = None
        self.estado_final = None


    def start(self):
        '''
        inicializar el indicador de posicion y llamar al estado inicial
        '''
        print("AFD inicializado...")
        self.estado_aceptacion = self.estados[1]
        self.estado_inicial = self.estados[0]

    def transicion(self, estado, simbolo):
        
        if estado == 'S0' and simbolo == '0':
            return 'S0'
        
        if estado == 'S0' and simbolo == '1':
            return 'S1'
        
        if estado == 'S1' and simbolo == '0':
            return 'S2'

        if estado == 'S1' and simbolo == '1':
            return 'S1'
        
        if estado == 'S2' and simbolo == '0':
            return 'S0'
        
        if estado == 'S2' and simbolo == '1':
            return 'S2'



    def verificar(self, cadena):

        if self.estado_final == self.estado_aceptacion:
            print("La cadena pertenece al lenguaje de aceptacion")
            self.identificador_OK = True
        else: 
            print("La cadena NO pertenece al lenguaje de aceptacion")
            self.error()

    def error(self):
        '''
        establecer en falso a la variable identificador_OK 
        '''
        self.identificador_OK = False

    def imprimirCamino(self, cadena):
        print("\nImprimiendo recorrido de la cadena '{}': ".format(cadena))
        estado = self.estado_inicial
        print(self.estado_inicial, end="  ")

        for simbolo in cadena:
            estado = self.transicion(estado, simbolo)
            print(estado, end = "  ")
            
        
        print("\n")
        self.estado_final = estado
        




if __name__ == '__main__':

    cadena_entrada = input("\nIngrese una cadena de entrada: ")
    M = AFD()
    M.start()
    M.imprimirCamino(cadena = cadena_entrada)

    M.verificar(cadena = cadena_entrada)