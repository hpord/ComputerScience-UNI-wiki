import numpy as np

############################################
def agregarArco(a):
    ini=int(input("Ingrese vertice inicial:"))
    fin=int(input("Ingrese vertice final:"))
    a[ini,fin]=1
    return a
#############################################
def quitarArco(a):
    ini=int(input("Ingrese vertice inicial:"))
    fin=int(input("Ingrese vertice final:"))
    a[ini,fin]=0
    return a
#############################################
def consultarArco(a):
    ini=int(input("Ingrese vertice inicial:"))
    fin=int(input("Ingrese vertice final:"))
    if(a[ini,fin]==1):
        print("Existe arco")
    else:
        print("No existe arco")
#############################################
def ListarArcos(a):
    print(a)
    for i in a:
        for j in i:
            if(a[i,j]==1):
                print("Vert Ini: ",i,"Vert Final: ",j)
                print(j)
#############################################
q=True
a = np.array([[0,1,0,1,1],[0,0,0,0,0],[1,0,1,0,0],[0,0,1,0,0],[1,0,0,0,0]])
while q==True:
    print("1)Agregar arco")
    print("2)Eliminar arco")
    print("3)Consultar arco")
    print("4)Listar arcos")
    print("5)Salir")
    a=int(input("Opcion:"))
    if(a==1):
        agregarArco(a)
    if(a==2):
        quitarArco(a)
    if (a==3):
        consultarArco(a)
    if (a==4):
        ListarArcos(a)
    if (a==5):
        q=False