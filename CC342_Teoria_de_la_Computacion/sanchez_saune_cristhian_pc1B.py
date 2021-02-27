from itertools import groupby

def almacenar():
    n = input("Ingrese la cantidad de numeros: ")

    lista = []
    for i in range(int(n)):
        numero = input("Ingresando posición {} : ".format(i))
        lista.append(numero)
    
    return lista

def contar(una_lista): 
    veces = {key: len(list(group)) for key, group in groupby(una_lista)}
    lista_final = []
    for i in range(len(una_lista)):
        if int(veces[una_lista[i]]) >=2:
            lista_final.append(una_lista[i])

    return set(lista_final)


if __name__ == '__main__':

    lista_prueba = almacenar()
    conjunto = contar(una_lista=lista_prueba)
    print("\n\nEl conjunto de elementos repetidos es:\n")
    print(conjunto)
