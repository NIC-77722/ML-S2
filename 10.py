# Ejercicio 10
n = int(input("Ingrese la cantidad de elementos de la primera lista: "))
lista1 = [input(f"Elemento {i+1} de la lista 1: ") for i in range(n)]

m = int(input("Ingrese la cantidad de elementos de la segunda lista: "))
lista2 = [input(f"Elemento {i+1} de la lista 2: ") for i in range(m)]

if lista1 == lista2:
    print("Las listas son iguales")
else:
    print("Las listas no son iguales")
