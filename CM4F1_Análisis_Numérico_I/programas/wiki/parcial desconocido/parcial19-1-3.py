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


def FactLU(A):
	n = A.shape[0]
	a = A.copy()
	P = np.identity(n)
	L = np.identity(n)
	for i in range(n-1):
		p = np.identity(n)
		l = np.identity(n)
		s = np.argmax(np.absolute(a[i:,i]))+i
		if i != s:
			p[:,[i,s]] = p[:,[s,i]]
		a = p.dot(a)
		l[i+1:,i] = -a[i+1:,i]/a[i,i]
		a = l.dot(a)
		P = p.dot(P)
		L = l.dot(p).dot(L)
	L = P.dot(np.linalg.inv(L))
	return P,L,a
def gauss(A, x, b,n1):
	A = A.copy()
	b = b.copy()
	n = A.shape[1]
	for i in range(n-1):
		L = np.identity(n)
		L[i+1:,i] = -A[i+1:,i]/A[i,i]
		A = L.dot(A)
		b = L.dot(b)
	imprimeSistema(A,x,b,n1)
	return solU(A,b)
print("De la lectura, las variables son los coeficientes de cada molecula de la ecuacion quimica dada por:")
print("xMnSO4 + yKMnO4 +  zH2O --> aMnO2 + bK2SO4 + 2H2SO4")
print("(a) El conjunto de ecuaciones que forman son:")
#ecuaciones...
print("Mn: x + y = a")
print("S: x = b + c")
print("O: 4x + 4y + z = 2a + 4b + 4c")
print("K: y = 2b")
print("H: 2z = 2c")
print("El sistema es:")
#print("\nLa calidad de solucion del problema:\n")
#print(str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*(1/np.linalg.cond(A,np.inf)))+" ≤ ||E||∞/||x||∞ ≤ "+str((np.linalg.norm(R,np.inf)/np.linalg.norm(b,np.inf))*np.linalg.cond(A,np.inf)))

n = 5
A =np.array([[ 1, 1, 0, -1, 0],
	[ 1, 0, 0, 0, -1],
	[ 4, 4, 1, -2, -4],
	[ 0, 1, 0, 0, -2],
    [ 0, 0, 2, 0, 0]
	])
x = [["x"], ["y"], ["z"], ["a"], ["b"]]
b = np.array([ 0, 2, 8, 0, 4])
imprimeSistema(A, x, b, n)
print("(b) Sea ||A||inf = "+str(normainfinito(A))+".")
print("Luego, su inversa es:")
Ainv=inversa(A)
imprimeMatriz(Ainv)
print("Con ||A^-1||inf = "+str(normainfinito(Ainv))+", donde el numero de condicion es:")
print("Cond inf (A) = "+str(condicional(A)))
print("(c) Por el metodo de Gauss, se tiene:")
x = gauss(A,x,b,n)
print("La solucion aproximada es:")
print("X: ")
imprimeVector(x,n)
print("Por el metodo LU se tiene:")
P,L,U=FactLU(A)
print("U:")
imprimeMatriz(U)
print("L:")
imprimeMatriz(L)
print("P: ")
imprimeMatriz(P)
y = solL(L,P.dot(b))
x = solU(U,y)
print("Cuya solucion aproximada es:")
print("X: ")
imprimeVector(x,n)
print("Para ambos metodos, se cumple:")
print(str(normainfinito(residual(A,x,b)))+"/("+str(normainfinito(b))+"*"+str(condicional(A))+")"+" <= ||E||inf/||x||inf <= "+str(condicional(A))+"*"+str(normainfinito(residual(A,x,b)))+"/"+str(normainfinito(b)))
print("==>||E||inf/||x||inf="+str(normainfinito(residual(A,x,b))/(normainfinito(b)*condicional(A))))
print("Para este problema los dos metodos resultan ser buenos, dado que la condicion es un valor pequeño.")