from functions import response, frame

"""
Calcular el monto generado por un capital depositado durante cierta cantidad
de periodos a una tasa de interes determinada y expresada en porcentaje.

Monto = Capital * (1 + tasa/100)^periodos
"""


def function():
    # data
    print("\nINGRESA LA SIGUIENTE INFORMACIÓN:\n")
    capital: float = float(input("S/. Capital invertido > "))
    periodos: int = int(input("Número de periodos > "))
    tasa: float = float(input("% Tasa de interes > "))

    monto: float = capital * (1 + tasa / 100) ** periodos

    # output
    out: str = f"Monto generado: S/.{monto:.2f}"
    response(out)


frame(function)
