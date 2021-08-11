import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt


def minimos_cuadrados(X,Y,m=None):

    X=np.transpose(X)
    U=np.ones((X.shape[0],1))
    M=np.hstack((U,X))
    MT=np.transpose(M)
    Y=np.transpose(Y)

    A=np.dot(MT, M)
    b=np.dot(MT, Y)

    #solucion con la inversa
    x=np.dot(sl.inv(A), b)
    x=x.flatten()
    return x[::-1] # para obtener la forma y=ax+b

def ajuste_lineal(X, Y):
    p=minimos_cuadrados(X, Y)
    print("y=",p[0],"x=",p[1])  # corregir esta notación 
    x=np.array(X)
    y=np.array(Y)
    x=x.flatten()
    y=y.flatten()
    y_ajuste=p[0]*x+p[1]
    plt.scatter(x, y)
    plt.plot(x, y_ajuste,color="red")
    plt.title("Ajuste lineal por minimos cuadrados")
    plt.xlabel("eje X")
    plt.ylabel("eje Y")
    plt.show()


#y=ax+b

#valores de y

Y=np.array([[448, 556, 844, 427, 811, 398, 447, 154, 534, 13]],dtype='float')
#valores de x
X=np.array([[176, 168, 202, 138, 213, 159, 193, 122, 185, 153]],dtype='float')

ajuste_lineal(X, Y)








