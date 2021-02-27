import collections
import math

############################################################
# Problema 1

def encuentraUltimaPalabraAlfabeto(texto):
    """
    Dada una cadena |texto|, devuelve una palabra en |texto| 
    que aparece en ultimo lugar alfabeticamente (es decir, la palabra
     que aparece en ultimo lugar en un diccionario). 
    Una palabra se define por una secuencia maxima de caracteres sin espacios en blanco. 
    """
    # Inicio de Codigo
    diccionario = str(texto).split(" ")
    diccionario = [word.lower() for word in diccionario]
    diccionario.sort()
    return str(diccionario[-1])
    # Fin de Codigo

############################################################
# Problema 2

def distanciaeuclidiana(loc1, loc2): 
    """
    Returna la distancia entre dos localizaciones, donde localizaciones 
    son un par de numeros (por ejemplo (5, 12)).
    """

    # Inicio de Codigo
    x1, y1 = loc1
    x2, y2 = loc2
    x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2) 
    distancia = (x1 - x2)**2 + (y1 - y2)**2
    distancia = distancia**0.5
    return round(distancia, 2)
    # Fin de Codigo
   
############################################################
# Problema 3

def oracionesSimilares(oracion): 
    """
    Dada una oracion (secuencia de palabras), devuelve una lista de todas las oraciones "similares".
    Definimos una oracion como similar a la oracion original si
       - tiene el mismo numero de palabras  y
       - cada par de palabras adyacentes en la nueva oracion tambien aparece en la oracion original 
            (las palabras dentro de cada par deben aparecer en el mismo orden en la oracion de salida
             que en la oracion original).
    Notas:
      - El orden de las oraciones que genere no importa.
      - No debes generar duplicados.
      - La oracion generada puede usar una palabra en la oracion original mas de una vez.
    Ejemplo:
      - Entrada: 'the cat and the mouse'
      - Salida: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (se permiten versiones reordenadas de esta lista)
    """
    # Inicio de Codigo
    import itertools 

    lista_oracion = oracion.split(" ")
    n = len(lista_oracion)
    palabras = [(lista_oracion[i], lista_oracion[i+1]) for i in range(n - 1)]
    posibles_palabras = {}

    for query, key in itertools.groupby(sorted(palabras), key = lambda x: x[0]):
        posibles_palabras[query] = set(k[1] for k in key)

    def generar_similares(secuencia):
        secuencias = []
        if len(secuencia) == n:
            return [secuencia, ]
        for posible_palabra in posibles_palabras.get(secuencia[-1], []):
            secuencias += generar_similares(secuencia + [posible_palabra,])
        return secuencias

    def similares():
        respuestas = []
        for key, _ in posibles_palabras.items():
            respuestas += generar_similares([key, ])
        oracionSimilar = [' '.join(respuesta) for respuesta in respuestas]
        return oracionSimilar

    return similares()

    # Fin de Codigo

############################################################
# Problema4

def productoEscalarvVectorialdisperso(v1, v2):
    """
    Dados dos vectores dispersos |v1| y |v2|, cada uno representado como collection.defaultdict (float),
    devuelve su producto escalar.
    Esta funcion sera util mas adelante para clasificadores lineales.
    """
    # Inicio de Codigo
    import numpy as np

    v1_, v2_ = np.array(list(dict(v1).values())), np.array(list(dict(v2).values()))
    
    dot = np.dot(v1_, v2_)

    return dot.tolist()
    # Fin de Codigo

############################################################
# Problema 5

def incrementoVectorDisperso(v1, escala, v2): 
    """
    Dados dos vectores dispersos |v1| y |v2|, realiza v1 + = escala * v2.
    Esta funcion sera util  para clasificadores lineales.
    """
   # Inicio de Codigo
    import numpy as np
    v1, v2 = np.array(list(dict(v1).values())), np.array(list(dict(v2).values()))
    v1 += (escala * v2)

    
    return v1.tolist()
    # Fin de Codigo

############################################################
# Problema 6

def encontrarUnicaPalabra(texto): 
    """
    Divide la cadena |texto| por espacio en blanco y devuelve el conjunto de 
    palabras que aparecen exactamente una vez.

    """
    # Inicio de Codigo
    unica_vez = []
    candidatos = list(texto.split(" "))
    for palabra in candidatos:
        frecuencia = {x: candidatos.count(x) for x in candidatos}
    
    for key, value in zip(frecuencia.keys(), frecuencia.values()):
        if value == 1:
            unica_vez.append(key) 

    return set(unica_vez)
    # Fin de Codigo

############################################################
# Problema 7

def calculaPolindromoMasLargo(texto): 
    """
    Un palindromo es una cadena que es igual a su reverso (por ejemplo, 'ana'). 
    Calcula la longitud del palindromo mas largo que se puede obtener eliminando
    letras de |texto|.

    Por ejemplo: el palindromo mas largo en 'animal' es 'ama'.
    Tu algoritmo debe ejecutarse en tiempo O(len(texto)^2).
    Primero debes definir una recurrencia antes de comenzar a codificar.
    """
    # Inicio de Codigo
    n = len(texto)
    def obtener_numero(cadena, i, j): # Tomamos dos índices 'i' y 'j'
        if (i >= j): 
            return 0
        
        #comparar el carácter en el índice 'i' y 'j'
        if (cadena[i] == cadena[j]):
            return obtener_numero(cadena, i + 1, j - 1) # recursión sobre la función incrementando i+=1 y disminuyendo j-=1

    # devolvemos el elemento mínimo entre dos valores, y lo aumentamos en 1  
        return (1 + min(obtener_numero(cadena, i + 1, j),
                        obtener_numero(cadena, i, j - 1)))

    def min_numero_borrar(texto):
        return obtener_numero(texto, 0, 
                           len(texto) - 1)

    return int(n - min_numero_borrar(texto))
    # Fin de Codigo
