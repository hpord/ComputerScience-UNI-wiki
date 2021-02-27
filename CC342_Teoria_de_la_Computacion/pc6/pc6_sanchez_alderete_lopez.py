''' TODO: Debug for others case of grammar and examples '''

from colorama import Fore
from colorama import Style
import time 

class Regla:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.cont = 1  # la clase gramática la usa para eligir las reglas

    def __repr__(self):
        '''
        Cuando se imprime una instancia de la clase
        Regla, Python llama automáticamente al método _repr_.

        INPUT: None, pero con el Regla ya inicializado, por ejemplo Regla('Historia', ('Frase','y','Historia'))
        OUTPUT: '1 Historia -> Frase y Historia'
        '''
        right = ''

        for i, r in enumerate(self.right):

            if(len(self.right) == 1):
                right = r

            else:
                right += r
                if i != (len(self.right) - 1):
                    right += " "
        
        stringOutput = str(self.cont) + ' ' + self.left + " -> " + right
        return stringOutput


class Gramatica:

    def __init__(self, semilla):
        import random as r1
        self.random = r1
        self.random.seed(semilla)
        self.dictOfRules = {}
    
    def regla(self, left, right):
        '''
        Agrega una nueva regla a la gramática

        left: cadena, simbolo no terminal en el lado izquierdo de la cadena

        right: tupla, cuyos elementos son cadenas (son los terminales y no terminales al lado derecho de la regla)
        '''
        
        if left in self.dictOfRules.keys():
            # Si existe tal valor, será una tupla. Añadir Regla(izquierda, derecha) al final de esa tupla
            
            r_mod = Regla(left=left, right=right)
            
            '''
            getRight = lambda r: r.right

            if right in list(map(getRight, self.dictOfRules[left])):
                r_mod.cont += 1
            '''
            n = len(self.dictOfRules[left])
            tup = ()

            for i in range(n):
                
                '''
                if right == self.dictOfRules[left][i].right:
                    self.dictOfRules[left][i].cont += 1
                '''

                tup += (self.dictOfRules[left][i], )
            
            tup += (r_mod, )

            self.dictOfRules[left] = tup
        
        else:
            r_new = Regla(left, right)
            self.dictOfRules[left] = (r_new, )
        
    def genera(self):
        '''
        Genera una cadena
        '''

        # Si hay una regla con el lado izquierdo 'Inicio' en el diccionario, llame a generar con la tupla("Inicio",) como argumento, y retorne el resultado. Si no existe dicha regla,entonces genere una excepción, porque no puede generar cadenas sin una regla para 'Inicio'


        # Si hay una regla con el lado izquierdo'Inicio' en el diccionario, llame a generar con la tupla("inicio", )
        if 'Inicio' in self.dictOfRules.keys():
            r = self.generar(strings = ('Inicio', ))
            return r
        
        else:
            raise Exception("\nNo se puede generar cadenas sin una regla para 'Inicio'\n")
    
    def generar(self, strings):
        '''
        string: tupla de cadenas (las cadenas son símbolos terminales y no terminales)
        '''

        resultado = ''
        for s in strings:
            if s in self.dictOfRules.keys():
                # Si la cadena visitada es una clave en el diccionario, entonces es un símbolo no terminal. Llame a 'seleccionar' en la cadena para obtener una tupla de cadenas. Luego llame a generar recursivamente en esa tupla de cadenas, para obtener una nueva cadena. Agregue la nueva cadena al final del resultado, sin un espacio en blanco al final.

                tuplStrings = self.seleccionar(left = s)
                r = self.generar(tuplStrings)
                resultado += r

            else:
                # Si la cadena visitada no es una clave en el diccionario, entonces es un símbolo terminal. Agréguelo al final del resultado, seguido de un espacio en blanco " ". 
                resultado = resultado + s + " "

        
        return resultado

    def seleccionar(self, left):
        
        # 1. Establecer la variable reglas para que sea la tupla de todas las reglas con left en sus lados izquierdos del diccionario. Establezcer la variable total como la suma de todas las variables cont en las reglas
        reglas = self.dictOfRules[left]

        total = sum(r.cont for r in reglas)

        # 2. Establecer la variable índice en un entero elegido al azar. Debe ser mayor o igual que 0, pero menor que total.
        indice = self.random.randint(0, total)

        # 3. Visite cada regla en 'reglas', una a la vez. Reste la variable cont de la regla del índice. Continúe de esta manera hasta que la variable índice sea menor o igual a O. Establecer la variable 'elegido' para la regla que se estaba visitando cuando esto ocurrió. (Como resultado, es más probable que se elijan reglas con grandes variables de conteo que reglas con pequeñas variables de conteo).
        print(f"\nReglas: {reglas}")

        for r in reglas:
            indice -= r.cont
            if indice <= 0:
                elegido = r
        
        # 4. Agregue 1 a las variables cont de todas las reglas en la variable reglas, excepto las elegidas. (Esto hace que sea más probable que se seleccione una regla distinta a la elegida más adelante, lo que proporciona un rango más amplio de cadenas aleatorias)
        print(f"Regla elegida: {elegido}\n")
        time.sleep(0.2) 

        for i, r in enumerate(reglas):
            if r != elegido:
                reglas[i].cont = r.cont + 1

        #Finalmente, devuelve la variable right de elegido, una tupla de cadenas.
        return elegido.right

def menu():

    print("-------------------------")
    print(f"{Fore.GREEN}Menú")
    print("1.- Agregar nueva regla")
    print("2.- Generar cadena")
    print("3.- salir")
    print(f'{Style.RESET_ALL}')

    op = int(input("Ingrese opción:  "))

    return op


if __name__ == '__main__':

    ke = Gramatica(semilla = 144)

    while True:
        op = menu()

        if op == 1:
            izq = input("ingrese parte izq: ")
            der = input("ingrese parte der: ")

            tuplaDer = tuple(der.split(" "))

            ke.regla(left=izq, right=tuplaDer)

            print(f"{Fore.YELLOW}\nmostrando reglas...\n")
            for rules in ke.dictOfRules:
                if len(ke.dictOfRules[rules]) == 1: 
                    print(ke.dictOfRules[rules][0]) 
                
                else:
                    for r in ke.dictOfRules[rules]:
                        print(r)
            print(f'{Style.RESET_ALL}')

        if op == 2:
            print(f"\n{Fore.YELLOW}mostrando reglas disponibles...\n")
            for rules in ke.dictOfRules:
                if len(ke.dictOfRules[rules]) == 1: 
                    print(ke.dictOfRules[rules][0]) 
                
                else:
                    for r in ke.dictOfRules[rules]:
                        print(r)     
            print(f'{Style.RESET_ALL}')

            print("\ngenerando cadena...\n")
            print(f"\t{ke.genera()}\n")

        elif op == 3:
            break

        
