import numpy as np
from scipy import linalg

print('MÉTODO DE POTENCIA',end="\n\n")
print("Este método iterativo cálcula sucesivas aproximaciones a los autovectores y autovalores de una matriz",end="\n")

# Matriz de coeficientes ecuacion

# ejercicio 7, dirigida 7, 20-2  
A = np.array([[4, -1, 1],
			  [-1, 3, -2],
			  [1, -2, 3]])
# El X(0) inicial para la iteracion 
x = np.array([[1],
              [0],
              [0]])



print("La matriz de coeficientes A es \n")
print(A)
print("\nEl valor de x(0)")
print(x)
print("\n")

ya = np.zeros((3, 1))
yp = np.zeros((3, 1))
i=1
estado=True


while(estado):
		ya=yp
		yp=A.dot(x)

		if((yp.round(3)==ya.round(3)).all()):
			estado=False
			break

		print("Iteracion "+str(i)+":")

		print("El y("+str(i)+") es")
		print(yp)
		domin=yp.flat[abs(yp).argmax()]
		print("\nEl componente dominante es ="+str(domin.round(3))+"\n")
		x=(1/domin.round(3))*yp
		print("El x("+str(i)+") es")
		print(x)
		print("\n")
		i=i+1


print("--------------------------------------")
print("La solución del valor propio de A es: λ = " + str(domin.round(3)))
print("El vector propio asociado es:\n" + str(np.array(yp)))

print("\nDatos para el calculo del error: ")
e=A.dot(yp)-(domin)*yp
print("\nA * x")
print(A.dot(yp))
print("\nλ * x")
print((domin)*yp)
print("\nA * x - λ * x")
print(e)
error=np.linalg.norm(e,np.inf)
print("\nError: ")
print(error)
	