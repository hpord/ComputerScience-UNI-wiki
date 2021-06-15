import numpy as np
import math
def imprimeMatriz(A):
	for i in range(len(A)):
		text = " |"
		m=len(np.shape(A))
		if(m>1):
			for j in range(len(A)):
				varA =str("%8.7f"%A[i][j])
				if(A[i][j]>=100):
					text = text +" "+ varA
				elif(A[i][j]<100 and A[i][j]>=10):
					text = text +"  "+ varA
				else:
					 text = text +"   "+ varA
			print (text+" |")
		elif(m==1):
			varA=str("%8.7f"%A[i])
			if(A[i]>0):
				print("  | " + varA+"|")
			else:
				print("  |" + varA+"|")				
def imprimeSistema(A,x,b,n):
	text = " |"
	for i in range(n):
		for j in range(n):
			varA = str("%8.7f"%A[i][j])
			if(A[i][j]>=0 and A[i][j]<10):
				text = text +" "+varA + " "
			else:
    			 text = text + varA + " "
		varB = str("%8.7f"%b[i])
		if (b[i]<0):
			print (text + "|" +" |"+"".join(x[i])+"|"+" |" + varB+" |")
		else:
			print(text + "|" +" |"+"".join(x[i])+"|"+" | " + varB+" |")
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
def solT(T,d):
	n = T.shape[1]
	a = np.diagonal(T,-1).copy()
	b = np.diagonal(T,0).copy()
	c = np.diagonal(T,1).copy()
	x = d.copy()
	c[0] /= b[0]
	x[0] /= b[0]
	for i in range(1,n):
		m = 1. / (b[i] - a[i-1] * c[i-1])
		if(i < (n-1)):
			c[i] *= m
		x[i] = (x[i] - a[i-1] * x[i-1]) * m
	for i in range(n-2,-1,-1):
		x[i] = x[i] - c[i] * x[i + 1]
	return x

def FactPR(A):
	n = A.shape[0]
	a = np.copy(A)
	P = np.identity(n)
	L = np.identity(n)
	for i in range(n-2):
		p = np.identity(n)
		l = np.identity(n)
		s = np.argmax(np.absolute(a[i+1:,i]))+i+1
		if i != s:
			p[:,[i+1,s]] = p[:,[s,i+1]]
		a = p.dot(a).dot(np.transpose(p))
		l[i+2:,i+1] = -a[i+2:,i]/a[i+1,i]
		a = l.dot(a).dot(np.transpose(l))
		P = p.dot(P)
		L = l.dot(p).dot(L)
	L = P.dot(np.linalg.inv(L))
	return P,L,a
print("Sea un polinomio de tercer grado: ax^3+bx^2+cx+d=n")
print("(a) Las variables serian los coeficientes del polinomio de tercer grado: a, b, c, d.")
print("(b) El sistema es:")
n = 4
A =np.array([[ 1, 1, 1, 1],
	[ 8, 4, 2, 1],
	[ 3, 2, 1, 0],
	[ 12, 2, 0, 0]
	])
x = [["a"], ["b"], ["c"], ["d"]]
b = np.array([ 2, 6, 5, -6])
imprimeSistema(A, x, b, n)
C=np.transpose(A).dot(A)
d=np.transpose(A).dot(b)
print("Por el metodo Parlett-Reid, se tienen:")
P,L,T = FactPR(C)
print('P:')
imprimeMatriz(P)
print('T:')
imprimeMatriz(T)
print('L:')
imprimeMatriz(L)
print("Resolviendo se tiene")
print("x:")
z = solL(L,P.dot(d))
y = solT(T,z)
x = solU(np.transpose(L),y)
imprimeMatriz(x)
print("(d) Se cumple:")
print(str(normainfinito(residual(A,x,b)))+"/("+str(normainfinito(b))+"*"+str(condicional(A))+")"+" <= ||E||inf/||x||inf <= "+str(condicional(A))+"*"+str(normainfinito(residual(A,x,b)))+"/"+str(normainfinito(b)))
print("==>"+str(normainfinito(residual(A,x,b))/(normainfinito(b)*condicional(A)))+"<=||E||inf/||x||inf<="+str(condicional(A)*normainfinito(residual(A,x,b))/normainfinito(b)))
print("Para este problema el metodo de Parlett-Reid resulta ser bueno, dado que la condicion es un valor pequeño.")