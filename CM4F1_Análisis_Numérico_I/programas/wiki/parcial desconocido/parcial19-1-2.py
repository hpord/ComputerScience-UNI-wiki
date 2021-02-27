for i in range(27):
    if(22*i%27==1):
        print(i)
#numero de condicion relativo: K=lim d->0 {sup ||dx||<=d[ ||df||inf * ||x||inf / ||f||inf * ||dx||inf ]}
#QR= Q,R= np.linalg.qr(A)
#Qt=np.transpose(Q)
#x=np.linalg.solve(R,Qt@b)