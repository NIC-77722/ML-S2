from functions import response, frame

"""
En el curso de Algoritmos se rinden 4 exámenes
de las cuales se elimina la menor nota. Hacer
un programa para ingresar las notas de los 4
exámenes y reportar la nota eliminada y el
promedio final del alumno
"""


def function():
    # data
    print("\nINGRESA 4 NOTAS SEPARADAS POR COMAS\n")
    notas: list[int] = [int(e.strip()) for e in input("> ").split(",")]

    if notas and len(notas) == 4:
        notas.sort()
    else:
        raise

    nota_fail = notas[0]
    notas = notas[1:]
    promedio = int(round(sum(notas) / len(notas), 0))

    # output
    out: str = f"Nota eliminada: {nota_fail} \nPromedio final: {promedio}"
    response(out)


frame(function)
