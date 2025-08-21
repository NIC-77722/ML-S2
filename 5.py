#Ingresar un numero entero y reportar si es perfecto o no. Un número es perfecto cuando es igual a la suma de divisores menores que el.

n = int(input("Ingrese un número entero: "))
suma_divisores = 0
for i in range(1, n):
    if n % i == 0:
        suma_divisores += i
if suma_divisores == n:
    print(n, "es un número perfecto.")
    print("La suma de sus divisores es:", suma_divisores)
else:
    print(n, "no es un número perfecto.")
    print("La suma de sus divisores es:", suma_divisores)
