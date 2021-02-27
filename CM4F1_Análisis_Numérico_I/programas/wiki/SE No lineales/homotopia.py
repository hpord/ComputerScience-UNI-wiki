import sympy as sp

def homotopia(F, x0, N, tol):
    
    var = list(F.free_symbols)
    n = len(var)
    H = 1./N
    JF = F.jacobian(var)
    print('JF(x): ')
    print(JF, end="\n\n")
    
    JFi = JF.inv()
    print('[JF(x)]^{-1}: ')
    print(JFi, end="\n\n")
    
    h = ('i',) + tuple('x_%i^{(i)}'%(i+1) for i in range(n)) +tuple('F_%i(x^{(i)})'%(i+1) for i in range(n)) + ('error',)
    
    print('x^{(0)}: ')
    print(x0, end="\n\n")
    
    print('tol='+"%.7f"%tol, end="\n\n")
    l = []
    i = 1
    Fx0 = F.evalf(subs=dict(zip(var,x0)))
    l.append((0,) + tuple('%.7f'%x0[i] for i in range(n)) + tuple('%.7f'%Fx0[i] for i in range(n)) + ('---',))
    
    while True:
        JFiv = lambda v : JFi.evalf(subs=dict(zip(var,v)))
        k = [-H * JFiv(x0) * Fx0]
        k += [-H * JFiv(x0+k[0]/2) * Fx0]
        k += [-H * JFiv(x0+k[1]/2) * Fx0]
        k += [-H * JFiv(x0+k[2]) * Fx0]
        x0 += (k[0]+2*k[1]+2*k[2]+k[3])/6
        Fx = F.evalf(subs=dict(zip(var, x0)))

        t1 = tuple('%.7f'%x0[j] for j in range(n))
        t2 = tuple('%.7f'%Fx[j] for j in range(n))
        t3 = '%.7f'%Fx.norm(sp.oo)
        l.append((i,) + t1 + t2 + (t3, ))
        
        if Fx.norm() < tol:
            break
        i += 1

    print(h, end="\n\n")
    for row in l:
        print(row, end="\n")
    print("\n")
    return x0

if __name__ == '__main__':
    x1,x2 = sp.symbols('x1 x2')
    F = sp.Matrix([x1*x2-72,x1*x2-3*x1+2*x2-78])
    
    print('F(x): ')
    print(F, end="\n\n")

    x0 = sp.Matrix([3.,6.])
    x = homotopia(F, x0, 7, 0.01)
    print("Matriz 'x': ")
    print(sp.Matrix(x))
