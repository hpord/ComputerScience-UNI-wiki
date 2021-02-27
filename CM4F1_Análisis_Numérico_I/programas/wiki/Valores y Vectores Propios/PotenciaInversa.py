from __future__ import print_function
import numpy as np

print('MÉTODO DE POTENCIA INVERSA',end="\n\n")

print("Este método sirve para el cálculo del autovector asociado a un autovalor conocido",end="\n")


# Matriz de coeficientes ecuacion
A = np.array([[0, 11.0, -5.0],
			  [-2.0, 17.0, -7.0],
			  [-4.0, 26.0, -10.0]])
# El X(0) inicial para la iteracion 
x = np.array([[0],
              [0],
              [0.5]])

print("La matriz de coeficientes A es \n")
print(A)


A_inv = np.linalg.inv(A)

print("\nMatriz A:")
print(A)
print("\nMatriz inversa de A:")
print(A_inv)   
print("\nVector x(0):")
print(x)

y=np.zeros((3,1))
y_c=np.zeros((3,1))
contador = 1    
estado=True
    
while(estado):
	y_c=y
	y=A_inv.dot(x)

	if((y.round(3)==y_c.round(3)).all()):
		print("----------")
		estado=False 
		break

	print('\nIteracion '+str(contador)+':')
		
	print("\ny(",end='')
	print(contador,end='')
	print('):')
	print(y)
	
	#Obtiene el maximo valor en valor absoluto
	c=y.flat[abs(y).argmax()]
	
	print('\nλ(' ,end='')
	print(contador,end='')
	print(')=',end='')
	print(c.round(3))
	x=(1/c.round(3))*y
	print("\nx(",end='')
	print(contador,end='')
	print('):')
	print(x)
	
	#Cuenta el total de iteraciones realizadas
	contador=contador+1
 
print("\nResultados para ",end='')
print(contador-1,end='')
print(' iteraciones:')
print('*Autovalor Minimo de A, λ = ', end='')
print(1/c.round(3))
print("*Autovector Asociado, v:")
print(y.round(3))
print("\nDatos para el calculo del error:\n")
e=A.dot(y)-(1/c)*y
print("<<A * v>>")
print(A.dot(y))
print("\n<<λ * v>>")
print((1/c)*y)
print("\n<<A * v - λ * v>>")
print(e)
error=np.linalg.norm(e,np.inf)
print("\nError:",end='')
print(error)



# Recomendaciones:

'''Tener en cuenta que la matriz A debe ser una matriz invertible, no singular'''