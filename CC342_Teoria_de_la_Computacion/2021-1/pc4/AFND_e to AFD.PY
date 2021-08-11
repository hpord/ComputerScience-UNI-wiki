#a=0
#b=1
#2= null
#3=epsilon
afnd_e = [[2,1,2,2,0,2],
          [2,2,1,3,2,2],
          [2,2,2,1,2,2],
          [2,2,2,2,2,2],
          [2,3,3,2,2,0],
          [2,2,2,0,2,2]]

wiki= [[2,3,2,2,2,2,2,3,2,2,2],
       [2,2,3,2,3,2,2,2,2,2,2],
       [2,2,2,0,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,3,2,2,2,2],
       [2,2,2,2,2,1,2,2,2,2,2],
       [2,2,2,2,2,2,3,2,2,2,2],
       [2,3,2,2,2,2,2,3,2,2,2],
       [2,2,2,2,2,2,2,2,0,2,2],
       [2,2,2,2,2,2,2,2,2,1,2],
       [2,2,2,2,2,2,2,2,2,2,2]]


# def epsilon_util2(M,i,salida):
#     for j in range(9):
#         if(M[i][j]==3):
#             salida.append(j)
#             epsilon_util(M,j,salida)



# def epsilon_util(M,entrada,salida):
#     #Conj.append(i)
#     for i in entrada:
#         epsilon_util2(M,i,salida)



def epsi_indv(M,i,salida):
    for j in range(9):
        if(M[i][j]==3):
            salida.append(j)
            epsi_indv(M,j,salida)

def epsi_total(M,Conj_entrada,salida):
    for i in Conj_entrada:
        epsi_indv(M,i,salida)


# def epsilon(M):
#     temp=[]
#     salida=[]
#     for i in range(9):
#         temp.append(i)
#         epsilon_util(M,i,temp)
#         print(temp)
#         print("-----------------")
#         temp=[]


def particion_util(M,i,entrada,salida):
    for j in range(9):
        if(M[i][j]==entrada):
            salida.append(j)
        

def particion(M,conj,entrada,salida):
    for i in conj:
        particion_util(M,i,entrada,salida)
    
def VectEntrada_To_lista(entrada,lista):
    for i in entrada:
        lista.append(i)

def epsilon(M):
    q=True
    while(q==True):
        entrada=[0]
        temp=[]
        salida=[]
        salida2=[]
        VectEntrada_To_lista(entrada,temp)
        epsi_total(M,entrada,temp)
        print(temp)
        particion(M,temp,0,salida)
        print(salida)
        VectEntrada_To_lista(salida,salida2)
        #salida2.append(5)
        #salida2.append(8)
        epsi_total(M,salida,salida2)
        print(list(set(salida2)))
        #epsilon_util(M,salida,temp)
        #print(temp)
        q=False

epsilon(wiki)
