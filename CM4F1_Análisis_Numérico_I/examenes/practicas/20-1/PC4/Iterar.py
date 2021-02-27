import numpy as np
def iterar(M,x,c,tol,i):
    continuar = True
    j=0
    x_ant=[0,0]
    print("k                                                                   x                                                                  Error")
    while (continuar and j<=i):
        _x = M @ x + c
        if(j<10):
            print(j, end="  ")
        else:
            print(j, end=" ")
        for k in range(len(x)):
            x_k=str("%8.7f"%x[k])
            if(x[k]<10):
                print(" "+x_k, end=" ")
            else:
                print(x_k, end=" ")
        if(j==0):
            print()
        else:
            error=str("%8.7f"%np.linalg.norm(x-x_ant,np.inf))
            print(error)
            continuar = np.linalg.norm(x-x_ant,np.inf) > tol
        j=j+1
        x_ant = x
        x = _x
    return x
'''M = np.array([[0, -0.8333333], [-0.4444444, 0]])
x = np.array([[0],[0]])
c = np.array([[19.629992], [13.718887]])
i = 3
tol = 0.000001
iterar(M, x, c, tol, i)'''