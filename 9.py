def union(lista1, lista2):
    return list(set(lista1) | set(lista2))

def interseccion(lista1, lista2):
    return list(set(lista1) & set(lista2))

def diferencia(lista1, lista2):
    return list(set(lista1) - set(lista2))

n = int(input("Ingrese la cantidad de elementos de la primera lista: "))
m = int(input("Ingrese la cantidad de elementos de la segunda lista: "))

lista1 = []
lista2 = []

print("\n--- Ingrese los elementos de la primera lista ---")
for i in range(n):
    valor = int(input(f"Elemento {i+1}: "))
    lista1.append(valor)

print("\n--- Ingrese los elementos de la segunda lista ---")
for i in range(m):
    valor = int(input(f"Elemento {i+1}: "))
    lista2.append(valor)

print("\nPrimera lista:", lista1)
print("Segunda lista:", lista2)

print("\nUnión:", union(lista1, lista2))
print("Intersección:", interseccion(lista1, lista2))