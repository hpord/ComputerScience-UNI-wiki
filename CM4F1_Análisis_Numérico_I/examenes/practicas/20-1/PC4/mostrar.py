import numpy as np
def imprimeMatriz(A):
	for i in range(len(A)):
		text = " |"
		m=len(np.shape(A))
		if(m>1):
			for j in range(len(A)):
				varA =str("%8.7f"%A[i][j])
				if(A[i][j]>=100):
					text = text +" "+ varA
				elif(A[i][j]<100 and A[i][j]>=10):
					text = text +"  "+ varA
				elif(A[i][j]<0):
					text = text +"   "+ varA
				else:
					 text = text +"    "+ varA
			print (text+" |")
		elif(m==1):
			varA=str("%8.7f"%A[i])
			if(A[i]>0):
				print("  | " + varA+"|")
			else:
				print("  |" + varA+"|")				
def imprimeSistema(A,x,b,n):
	text = " |"
	for i in range(n):
		for j in range(n):
			varA = str("%8.7f"%A[i][j])
			if(A[i][j]>=0 and A[i][j]<10):
				text = text +" "+varA + " "
			else:
    			 text = text + varA + " "
		varB = str("%8.7f"%b[i])
		if (b[i]<0):
			print (text + "|" +" |"+"".join(x[i])+"|"+" |" + varB+" |")
		else:
			print(text + "|" +" |"+"".join(x[i])+"|"+" | " + varB+" |")
		text =" |"