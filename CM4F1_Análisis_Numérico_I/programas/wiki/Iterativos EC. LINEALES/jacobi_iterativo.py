from numpy import array, zeros, diag, diagflat, dot
import time

def jacobi(A, b, N=25, x=None):
                                                                                                                                                          
    if x is None:
        x = zeros(len(A[0]))

    #  Creamos un vector de los elementos diagonales de A y lo restamos de A                                                                                                                                                                  
    D = diag(A)
    R = A - diagflat(D)

    # iteramos N veces 
    print("\n\nIteracion\tValores de X\n")
    print(0, end="\t\t")
    print(x)                                                                                                                                                                    
    for i in range(N):
       print(i + 1, end="\t\t") 
       x = (b - dot(R, x)) / D
       print(x)
    return x

if __name__ == '__main__':

    A = array([[9.0, -2.0, 0.0], [-2.0, 4.0, -1.0], [0.0, -1.0, 1.0]])
    b = array([5.0, 1.0, -0.833])


    inicial = array([0.0, 0.0, 0.0])

    start1 = time.time()
    solucion = jacobi(A, b, N=25, x = inicial)
    done1 = time.time()
    elapsed1 = done1 - start1

    print("\n\nA: ")
    print(A)

    print("\nb: ")
    print(b)

    print("\nx final: ")
    print(solucion, end="\n\n")
    print("Tiempo total: {} seg\n\n".format(elapsed1))