from functions import response, frame

"""
Ingrese un número que represente segundos y determinar
a cuanto equivale en horas, minutos y segundos.

Ejemplo:
Si se ingresa 9500 segundos el programa debería reportar:
    2 horas, 38 minutos y 20 segundos.
"""


def function():
    # data
    print("\nCLOCKY\n")
    num: int = int(input("Cantidad de segundos > "))

    horas = (num // 60) // 60
    minutos = (num // 60) - (horas * 60)
    segundos = num - (minutos * 60) - (horas * 60 * 60)

    # output
    out: str = f"Respuesta: {horas} horas, {minutos} minutos y {segundos} segundos."
    response(out)


frame(function)
