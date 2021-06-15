# Implementación iterativa de gauss-seidel

import time

# Definimos las ecuaciones para ser
# resueltas en forma de diagonal dominante
f1 = lambda x, y, z: (5 + 2*y)/9
f2 = lambda x, y, z: (1 + 2*x + z)/4
f3 = lambda x, y, z: (-0.8333 + y)


# Valores iniciales del problema
x0 = 0
y0 = 0
z0 = 0
contador = 1
iteraciones = int(input('Ingrese el numero de iteraciones: '))
print('\nIteracion\tx\ty\tz\n')


start1 = time.time()
while contador <= iteraciones:

    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(contador, x1 ,y1, z1))
    
    contador += 1
    x0 = x1
    y0 = y1
    z0 = z1
 
done1 = time.time()
elapsed1 = done1 - start1


print('\nSolucion: x=%0.3f, y=%0.3f y z = %0.3f\n'% (x1,y1,z1))
print("Tiempo total: {} seg\n\n".format(elapsed1))
