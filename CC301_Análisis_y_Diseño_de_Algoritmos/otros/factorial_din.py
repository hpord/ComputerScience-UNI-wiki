import numpy

def main():
    MAX_FACTORIALES=20        
    n=int(input("\n\tIngrese número n (0<=n<=20): "))
    if n < 0 or n >MAX_FACTORIALES:
      print("Debe ingresar un número en el rango [0..20]")
    else:    
      factorial=numpy.arange(MAX_FACTORIALES+1)
      inicializar_arreglo(factorial, MAX_FACTORIALES)
      print("\n\t{:d}!={:d}\n".format(n, factorial[n]))

def inicializar_arreglo(factorial, n):
    factorial[0] = 1
    for i in range(2, n+1):
        factorial[i] = i * factorial[i - 1] 


if __name__ == '__main__':
    main()
