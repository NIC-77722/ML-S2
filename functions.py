import os
import time
from typing import Callable


def clear():
    if os.name == "nt":  # windows
        _ = os.system("cls")
    else:  # mac o linux
        _ = os.system("clear")


def timer():
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.5)


def response(r: str):
    print()
    print(len(r) * "-")
    print(r)
    print(len(r) * "-")


def frame(function: Callable):
    while True:
        try:
            clear()
            function()
            print("\nPresiona ENTER para continuar...")
            input()
        except:
            print("\nUps! Inténtalo nuevamente.", end="")
            timer()
