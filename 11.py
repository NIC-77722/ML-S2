# Ejercicio 11
f = int(input("Ingrese el número de filas: "))
c = int(input("Ingrese el número de columnas: "))

# Crear matriz ingresada por el usuario
matriz = []
for i in range(f):
    fila = []
    for j in range(c):
        valor = int(input(f"Ingrese elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Calcular la transpuesta
transpuesta = [[matriz[j][i] for j in range(f)] for i in range(c)]

print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
