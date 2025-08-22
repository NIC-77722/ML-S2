#Ingresar n enteros en una lista A y otros n enteros en una lista B y mostrar la lista de enteros del vector C. Donde cada C[i]=A[i]+B[i].

A=[]
B=[]
C=[]
n=int(input("Ingrese el tamaño de los vectores: "))
for i in range(n):
    A.append(int(input("Ingrese un entero para A: ")))
for i in range(n):
    B.append(int(input("Ingrese un entero para B: ")))
for i in range(n):
    C.append(A[i]+B[i])
print("La lista C es:", C)