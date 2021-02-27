#!/usr/bin/env python

import pruebasUtil, collections, random

pruebas = pruebasUtil.Grader()
respuestas1 = pruebas.load('respuestas')

############################################################
# Problema: Encuentra ultima palabra del alfabeto

pruebas.addBasicPart('1-0-basico', lambda :
        pruebas.requireIsEqual('word', respuestas1.encuentraUltimaPalabraAlfabeto('which is the last word alphabetically')),
        description='caso de prueba simple')

pruebas.addBasicPart('1-1-basico', lambda : pruebas.requireIsEqual('sun', respuestas1.encuentraUltimaPalabraAlfabeto('cat sun dog')), description='caso de prueba simple')
pruebas.addBasicPart('1-2-basico', lambda : pruebas.requireIsEqual('99999', respuestas1.encuentraUltimaPalabraAlfabeto(' '.join(str(x) for x in range(100000)))), description='caso de prueba grande')

############################################################
# Problema : Distancia Euclidiana

pruebas.addBasicPart('2-0-basico', lambda : pruebas.requireIsEqual(5, respuestas1.distanciaeuclidiana((1, 5), (4, 1))), description='caso de prueba simple')

def test():
    random.seed(42)
    for _ in range(100):
        x1 = random.randint(0, 10)
        y1 = random.randint(0, 10)
        x2 = random.randint(0, 10)
        y2 = random.randint(0, 10)
        ans2 = respuestas1.distanciaeuclidiana((x1, y1), (x2, y2))
pruebas.addHiddenPart('2-1-oculto', test, maxPoints=2, description='100 pruebas aleatorias')

############################################################
# Problema: Oraciones Similares

def test():
    pruebas.requireIsEqual(sorted(['a a a a a']), sorted(respuestas1.oracionesSimilares('a a a a a')))
    pruebas.requireIsEqual(sorted(['the cat']), sorted(respuestas1.oracionesSimilares('the cat')))
    pruebas.requireIsEqual(sorted(['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']), sorted(respuestas1.oracionesSimilares('the cat and the mouse')))
pruebas.addBasicPart('3-0-basico', test, maxPoints=1, description='prueba simple')

def genSentence(K, L): 
    return ' '.join(str(random.randint(0, K)) for _ in range(L))

def test():
    random.seed(42)
    for _ in range(10):
        sentence = genSentence(3, 5)
        ans2 = respuestas1.oracionesSimilares(sentence)
pruebas.addHiddenPart('3-1-oculto', test, maxPoints=1, description='pruebas aleatorias')

def test():
    random.seed(42)
    for _ in range(10):
        sentence = genSentence(25, 10)
        ans2 = respuestas1.oracionesSimilares(sentence)
pruebas.addHiddenPart('3-2-oculto', test, maxPoints=2, description='pruebas aleatorias (largas)')


############################################################
# Problema: Producto escalar disperso

def test():
    pruebas.requireIsEqual(25, respuestas1.productoEscalarvVectorialdisperso(collections.defaultdict(float, {'a': 5, 'b': 5}), collections.defaultdict(float, {'a': 2, 'b': 3})))
pruebas.addBasicPart('4-0-basico', test, maxPoints=1, description='prueba simple')

def randvec():
    v = collections.defaultdict(float)
    for i in range(10):
        #v[random.randint(0, 10)] = random.randint(0, 10) - 5
        v[i] = random.randint(0, 10) - 5
    return v
def test():
    random.seed(42)
    for _ in range(10):
        v1 = randvec()
        v2 = randvec()
        ans2 = respuestas1.productoEscalarvVectorialdisperso(v1, v2)
pruebas.addHiddenPart('4-1-oculto', test, maxPoints=2, description='pruebas aleatorias')

############################################################
# Problema: Escala de un vector disperso

def test():
    v = collections.defaultdict(float, {'a': 5, 'b': 6})
    #respuestas1.incrementoVectorDisperso(v, 2, collections.defaultdict(float, {'a': 2, 'b': 3}))
    ans = respuestas1.incrementoVectorDisperso(v, 2, collections.defaultdict(float, {'a': 2, 'b': 3}))
    #  pruebas.requireIsEqual(collections.defaultdict(float, {'a': 11, 'b': 4}), v)
    pruebas.requireIsEqual([9, 12], ans)
pruebas.addBasicPart('5-0-basico', test, description='prueba simple')

def test():
    random.seed(42)
    for _ in range(10):
        v1a = randvec()
        v1b = v1a.copy()
        v2 = randvec()
        respuestas1.incrementoVectorDisperso(v1b, 4, v2)
        for key in list(v1b):
          if v1b[key] == 0:
            del v1b[key]
pruebas.addHiddenPart('5-1-oculto', test, maxPoints=2, description='pruebas aleatorias')

############################################################
# Problema: Encontrar unica palabra

def test3f():
    pruebas.requireIsEqual(set(['quick', 'brown', 'jumps', 'over', 'lazy']), respuestas1.encontrarUnicaPalabra('the quick brown fox jumps over the lazy fox'))
pruebas.addBasicPart('6-0-basico', test3f, description='prueba simple')

def test3f(numTokens, numTypes):
    import random
    random.seed(42)
    text = ' '.join(str(random.randint(0, numTypes)) for _ in range(numTokens))
pruebas.addHiddenPart('6-1-oculto', lambda : test3f(1000, 10), maxPoints=1, description='pruebas aleatorias')
pruebas.addHiddenPart('6-2-oculto', lambda : test3f(10000, 100), maxPoints=1, description='pruebas aleatorias (grande)')

############################################################
# Problema: Calcula el polindromo mas largo de una cadena

def test3g():
    # Pruebas alrededor de casos basicos
    pruebas.requireIsEqual(0, respuestas1.calculaPolindromoMasLargo(""))
    pruebas.requireIsEqual(1, respuestas1.calculaPolindromoMasLargo("a"))
    pruebas.requireIsEqual(2, respuestas1.calculaPolindromoMasLargo("aa"))
    pruebas.requireIsEqual(1, respuestas1.calculaPolindromoMasLargo("ab"))
    pruebas.requireIsEqual(3, respuestas1.calculaPolindromoMasLargo("animal"))
pruebas.addBasicPart('7-0-basico', test3g, description='prueba simple')

def test3g(numChars, length):
    import random
    random.seed(42)
    # Genera una cadena de una longitud dada
    text = ' '.join(chr(random.randint(ord('a'), ord('a') + numChars - 1)) for _ in range(length))
    ans2 = respuestas1.calculaPolindromoMasLargo(text)
pruebas.addHiddenPart('7-2-oculto', lambda : test3g(2, 10), maxPoints=1, maxSeconds=1, description='pruebas aleatorias')
pruebas.addHiddenPart('7-3-oculto', lambda : test3g(10, 10), maxPoints=1, maxSeconds=1, description='pruebas aleatorias (mas caracteres)')
#pruebas.addHiddenPart('7-4-oculto', lambda : test3g(5, 20), maxPoints=1, maxSeconds=1, description='pruebas aleatorias')
#pruebas.addHiddenPart('7-5-oculto', lambda : test3g(5, 400), maxPoints=2, maxSeconds=2, description='pruebas aleatorias (grande)')

pruebas.grade()
