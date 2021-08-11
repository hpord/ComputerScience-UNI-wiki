#Dimension del array
N=5

def backtracking(lab,x,y,sol):

    if(x == N - 1 and y == N - 1 and lab[x][y] == 1):
        sol[x][y]=1
        return True
    
    if(esSeguro(lab,x,y)==True):
        if(sol[x][y]==1):
            return False
    
        sol[x][y]=1
        
        #Hacia arriba
        if(backtracking(lab,x+1,y,sol)==True):
            return True
        #Hacia derecha
        if(backtracking(lab,x,y+1,sol)==True):
            return True
        #Hacia izquierda
        if(backtracking(lab,x-1,y,sol)==True):
            return True
        #Hacia abajo
        if(backtracking(lab,x,y-1,sol)==True):
            return True

        sol[x][y]=0
        return False
    
    return False


def esSeguro(lab,x,y):
    if(x>=0 and x<N and y >=0 and y < N and lab[x][y]==1):
        return True
    
    return False

def resolverLab(lab):
    sol = [ [0, 0, 0, 0,0],
             [0, 0, 0, 0,0],
             [0, 0, 0, 0,0],
             [0, 0, 0, 0,0],
             [0, 0, 0, 0,0] ]
    
    if(backtracking(lab,0,0,sol)==False):
        print("No existe solucion")
        return False
    
    print(sol)
    return True

if __name__=="__main__":

    lab1 = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]

    lab2=[[1,0,1,0,0],
          [1,1,1,1,1],
          [0,1,0,1,0],
          [1,1,0,1,1],
          [0,1,1,0,1]]
    
    lab3=[[1,0,1,0,0],
          [1,1,1,1,1],
          [0,1,0,1,0],
          [1,1,0,1,1],
          [0,1,1,0,1]]

    resolverLab(lab3)