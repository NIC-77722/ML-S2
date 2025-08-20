from functions import response, frame
from datetime import date

"""
Ingresar el día y el mes de una fecha y 
reportar la estación a la que pertenece: 
    verano, otoño, invierno o primavera.
"""

estaciones = [
    {
        "nombre": "Verano",
        "inicio": date(2024, 12, 21),
        "fin": date(2025, 3, 19),
    },
    {
        "nombre": "Otoño",
        "inicio": date(2025, 3, 20),
        "fin": date(2025, 6, 19),
    },
    {
        "nombre": "Invierno",
        "inicio": date(2025, 6, 20),
        "fin": date(2025, 9, 21),
    },
    {
        "nombre": "Primavera",
        "inicio": date(2025, 9, 22),
        "fin": date(2025, 12, 20),
    },
]


def function():
    # data
    print("\nINGRESA UN DÍA Y UN MES DEL PRESENTE AÑO (Ejemplo: 16/8)\n")
    data: list[int] = [int(e.strip()) for e in input("> ").split("/")]

    if not data or len(data) != 2:
        raise

    fecha = date(2025, data[1], data[0])

    # output
    for e in estaciones:
        nombre = e["nombre"]
        inicio = e["inicio"]
        fin = e["fin"]

        if inicio <= fecha <= fin:
            response(f"Estación: {nombre}")
            break


frame(function)
