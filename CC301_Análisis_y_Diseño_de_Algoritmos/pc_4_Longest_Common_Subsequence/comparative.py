from lcs_naive_recursive import lcs
from lcs_DP import lcsDP
import time 

def main(X, Y):
    
    time_naive, result1, time_DP, result2 = None, None, None, None

    start1 = time.time()
    #result1 = lcs(X, Y, len(X), len(Y))
    done1 = time.time()
    time_naive = done1 - start1

    start2 = time.time()
    result2 = lcsDP(X, Y)
    done2 = time.time()
    time_DP = done2 - start2

    return time_naive, result1, time_DP, result2


if __name__ == '__main__':

    X = "hola A pesar de que la interfaz de Python esta mas pulida y es el foco principal del desarrollo, PyTorch tambien tiene una interfaz en C++"

    Y = "A pesar de que la interfaz de Python esta mas pulida y es el foco principal del desarrollo, PyTorch tambien tiene una interfaz en C++ y java"

    print("\nLongitud de X: {} \nLongitud de Y: {}\n".format(len(X), len(Y)))
    print("\nEjecutando algoritmos..\n")
    time_naive, result1, time_DP, result2 = main(X, Y)
    print("Algoritmo Naive: \n\tTiempo: {}s \tLCS: {} \n\nAlgoritmo DP: \n\tTiempo: {}s \tLCS: {}\n\n".format(time_naive, result1, time_DP, result2))

