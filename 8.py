#8.	Calcule la mediana de un conjunto de datos. La mediana de un vector ordenado es el elemento central si el número de términos es impar. Y la semisuma de los términos centrales si el número de términos es par.
def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    
    if n % 2 == 1:
        return datos_ordenados[n // 2]
    else:
        medio1 = datos_ordenados[n // 2 - 1]
        medio2 = datos_ordenados[n // 2]
        return (medio1 + medio2) / 2


valores1 = [6, 2, 9, 1, 7]   
valores2 = [4, 2, 8, 5]      
valores3 = [7, 4, 3]         

print("Mediana 1:", calcular_mediana(valores1))
print("Mediana 2:", calcular_mediana(valores2))
print("Mediana 3:", calcular_mediana(valores3))