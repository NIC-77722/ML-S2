n = int(input("Ingrese la cantidad de elementos de la lista: "))

lista = []
for i in range(n):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    lista.append(elemento)

print("La lista es:", lista)

item = input("Ingrese el elemento a buscar: ")


cantidad = lista.count(item)

print(f"El elemento '{item}' aparece {cantidad} veces en la lista.")
