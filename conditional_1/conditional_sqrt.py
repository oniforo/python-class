"""
Faça um Programa que peça um valor numérico qualquer e imprima a raiz quadrada 
do número caso seja maior que 100. Do contrário não faça nada.
"""

import math

def conditional_sqrt():
    print("\nRetorna a raíz quadrada de números maiores que 100\n")

    try:
        _value = input("Inserir um valor numérico: ")
        value = float(_value)
    except ValueError:
        print("O valor precisa ser numérico\n")
        return
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return

    if value > 100:
        print(f"A raíz quadrada de {value} é {round(math.sqrt(value), 4)}\n")


if __name__ == "__main__":
    conditional_sqrt()