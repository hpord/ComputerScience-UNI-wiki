import numpy as np

def EsDiagonalDominante(A):
	for i,u in enumerate(A):
		s = sum(abs(v) for j,v in enumerate(u) if i != j)
		d = u[i]
		print("|A[",i,"][",i,"]| = ",d,", Σ = ",s,sep='')
		if  s > d:
			return False
	return True

def iterar(M,x,c,tol):
	continuar = True
	j = 0
	while (continuar):
		_x = M @ x + c
		if j > 0:
			print(j,"):",sep="")
			print(x)
			error = np.linalg.norm(x-_x,np.inf)
			print("Error:", error,"\n")
			continuar = np.linalg.norm(x-_x,np.inf) > tol
		x = _x
		j += 1
	return x

A = np.loadtxt("matrizPC4.txt")
b = np.loadtxt("vectorPC4.txt")

print("A:")
print(A)
print("b")
print(b)

print("a) ¿La matriz es diagonal dominante?")
print("Sí es" if EsDiagonalDominante(A) else "No es")
print("\nb) Método de Jacobi:")
I = np.identity(A.shape[0])
cj = np.linalg.inv(np.diag(np.diag(A)))
J = I - cj @ A
cj = cj @ b
print("J:")
print(J)
print("c:")
print(cj)
x = np.zeros_like(b)
print("x⁰:")
print(x)
x = iterar(J,x,cj,0.01)
print("x:")
print(x)

print("\nc) Método de Gauss-Seidel:")
cg = np.linalg.inv(np.tril(A,0))
G = I - cg @ A
cg = cg @ b
print("G:")
print(J)
print("c:")
print(cj)
x = np.zeros_like(b)
print("x⁰:")
print(x)
x = iterar(G,x,cg,0.01)
print("x:")
print(x)
