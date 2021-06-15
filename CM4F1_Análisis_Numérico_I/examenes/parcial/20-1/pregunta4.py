import numpy as np
import math
def imprimeVector(A,n):
    for i in range(n):
        varA=str("%8.7f"%A[i])
        print("  |" + varA+"|")
def imprimeMatriz(A):
	for i in range(len(A)):
		text = " |"
		for j in range(len(A[i])):
			varA =str("%8.7f"%A[i][j])
			if(A[i][j]>=0):
				text = text + varA + "  "
			else:
				 text = text + varA + " "
		print (text+"| ")
	print
def imprimeSistema(A,x,b,n):
	text = " |"
	for i in range(n):
		for j in range(n):
			varA = str("%8.7f"%A[i][j])
			if(A[i][j]>=0):
				text = text +varA + "  "
			else:
    			 text = text + varA + " "
		varB = str("%8.7f"%b[i])
		print (text + "|" +"|"+"".join(x[i])+"|"+"  |" + varB,end="")
		if (b[i]<10):
			print(" |")
		else:
			print("|")
		text =" |"
def normainfinito(A):
    n=np.linalg.norm(A,np.inf)
    return n
def inversa(A):
    I=np.linalg.inv(A)
    return I
def residual(A,x,b):
    R=A.dot(x)-b
    return R
def condicional(A):
    c=np.linalg.cond(A, np.inf)
    return c
def solU(U,b): # Ux = b
	n = U.shape[0]
	x = np.zeros(U.shape[1])
	for m in range(n)[::-1]:
		x[m] = b[m] - sum(U[m,i]*x[i] for i in range(m,n))
		x[m] /= U[m][m]
	return x
def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A
 
def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H
print("(a) Las variables serian: x1, x2, x3, x4, x5, x6, x7.")
print("(b) El sistema es:")
n = 7
A =np.array([[ 1, 0, 1, 0, 0, 0, 0],
	[ 1, -1, 0, 1, 0, 0, 0],
	[ 0, 1, 0, 0, -1, 0, 0],
	[ 0, 0, 0, 0, -1, 0, 1],
    [ 0, 0, 0, 1, 0, 1, -1],
    [ 0, 0, 1, 0, 0, 1, 0]
	])
x = [["x1"], ["x2"], ["x3"], ["x4"], ["x5"], ["x6"], ["x7"]]
b = np.array([ 800, 200, 600, 50, 600, 750])
print('A:')
print(A)
print("x:")
print(x)
print("b:")
print(b)
print("(c) Por el metodo Householder, se tienen:")
print()
Q,R = np.linalg.qr(A)
print('Q:')
print(Q)
print('\nR:')
print(R)
print()
print('\nQR:')
print(Q.dot(R))
b = np.array([56.,25,62,41,10,47])
print('b:')
print(b)
y = np.transpose(Q).dot(b)
x = solU(R,y)
print('x:')
print(x)
print('Ax:')
print(A.dot(x))
#print("(d) Se cumple:")
#print(str(normainfinito(residual(A,x,b)))+"/("+str(normainfinito(b))+"*"+str(condicional(A))+")"+" <= ||E||inf/||x||inf <= "+str(condicional(A))+"*"+str(normainfinito(residual(A,x,b)))+"/"+str(normainfinito(b)))
#print("==>"+str(normainfinito(residual(A,x,b))/(normainfinito(b)*condicional(A)))+"<=||E||inf/||x||inf<="+str(condicional(A)*normainfinito(residual(A,x,b))/normainfinito(b)))
#print("Para este problema el metodo de Parlett-Reid resulta ser bueno, dado que la condicion es un valor pequeño.")
