empty_list=[]
cant = int(input("Ingrese la cantidad de elementos a ingresar :"))
for i in range (0,cant):
    num=int(input("Ingrese dato :"))
    for q in range (0,len(empty_list)):
        if(q==num):
            print("No debe repetirse.")
        else:
            empty_list.append(num)
print(empty_list)
