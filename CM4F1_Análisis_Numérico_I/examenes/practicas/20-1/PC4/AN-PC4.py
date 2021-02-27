import numpy as np
import mostrar
import Iterar
def EsDiagonalDominante(A):
	for i,u in enumerate(A):
		s = sum(abs(v) for j,v in enumerate(u) if i != j)
		d = u[i]
		print("|A[",i,"][",i,"]| = ",d,", sumatoria = ",s,sep='')
		if  (s > d):
			return False
	return True

A = np.loadtxt("matrizPC4.txt")
b = np.loadtxt("vectorPC4.txt")

print("A:")
mostrar.imprimeMatriz(A)
print("b")
mostrar.imprimeMatriz(b)

print("a) La matriz es diagonal dominante?")
if(EsDiagonalDominante(A)):
	print("Si es")
else:
	print("No es")

print("\nb) Metodo de Jacobi:")
I = np.identity(A.shape[0])
cj = np.linalg.inv(np.diag(np.diag(A)))
J = I - cj @ A
cj = cj @ b
print("J:")
mostrar.imprimeMatriz(J)
print("c:")
mostrar.imprimeMatriz(cj)
x = np.zeros_like(b)
print("Solucion:")
Iterar.iterar(J,x,cj,0.01, 12)


print("\nc) Metodo de Gauss-Seidel:")
cg = np.linalg.inv(np.tril(A,0))
G = I - cg @ A
cg = cg @ b
print("G:")
mostrar.imprimeMatriz(J)
print("c:")
mostrar.imprimeMatriz(cj)
x = np.zeros_like(b)
print("Solucion:")
Iterar.iterar(G,x,cg,0.01, 9)

