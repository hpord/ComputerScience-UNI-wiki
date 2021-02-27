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
			if(j==len(A)):
				text = text +str("%8.3f"%A[i][j])
			else:
				 text = text +str("%8.3f"%A[i][j])
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
				 text = text +varA + " "
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

def solL(L,b): # Lx = b
	n = L.shape[0]
	x = np.zeros(L.shape[1])
	for m in range(n):
		x[m] = b[m] - sum(L[m,i]*x[i] for i in range(m))
		x[m] /= L[m][m]
	return x

def solU(U,b): # Ux = b
	n = U.shape[0]
	x = np.zeros(U.shape[1])
	for m in range(n)[::-1]:
		x[m] = b[m] - sum(U[m,i]*x[i] for i in range(m,n))
		x[m] /= U[m][m]
	return x
def solGaussJordan(A,b):
	A = A.copy()
	b = b.copy()
	n = A.shape[1]
	for i in range(n):
		L = np.identity(n)
		L[:,i] = -A[:,i]/A[i,i]
		L[i,i] = 1/A[i,i]
		A = L.dot(A)
		b = L.dot(b)
	return b
print("(a) Las variables son las demandas de cada producto de los primarios, intermedios  y finales:")
print("x1B1, x2B2, x3B3, x4Z1, x5Z2, x6E1, x7E2")
print("(b) El sistema es:")
#print("\nLa calidad de solucion del problema:\n")
#print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))
n = 7
A =np.array([[ 1, 0, 0, -3, -5, 0, 0],
	[ 0, 1, 0, -8, -4, 0, 0],
	[ 0, 0, 1, -2, -6, 0, 0],
	[ 0, 0, 0, 1, 0, -7, -8],
    [ 0, 0, 0, 0, 1, -6, -2],
    [ 0, 0, 0, 0, 0, 1, 0],
    [ 0, 0, 0, 0, 0, 0, 1]
	])
x = [["B1"], ["B2"], ["B3"], ["Z1"], ["Z2"], ["E1"], ["E2"]]
b = np.array([ 5, 8, 10, 5, 2, 3, 4])
imprimeSistema(A, x, b, n)
print("(c) Por el metodo de Gauss-Jordan, se tiene:")
x = solGaussJordan(A,b)
print("La solucion aproximada es:")
print("X: ")
imprimeVector(x,n)
print("(d) Se cumple:")
print(str(normainfinito(residual(A,x,b)))+"/("+str(normainfinito(b))+"*"+str(condicional(A))+")"+" <= ||E||inf/||x||inf <= "+str(condicional(A))+"*"+str(normainfinito(residual(A,x,b)))+"/"+str(normainfinito(b)))
print("==>"+str(normainfinito(residual(A,x,b))/(normainfinito(b)*condicional(A)))+"<=||E||inf/||x||inf<="+str(condicional(A)*normainfinito(residual(A,x,b))/normainfinito(b)))
print("Para este problema el metodo de Gauss-Jordan resulta ser bueno, dado que la condicion es un valor pequeño.")