"""
Faça um programa que peça um valor numérico qualquer e mostre na tela se o 
valor é positivo ou negativo.
"""

def check_sign():
    print("\nRetorna se o valor inserido é positivo (>=0) ou negativo\n")

    try:
        _value = input("Inserir um valor numérico: ")
        value = float(_value)
    except ValueError:
        print("O valor precisa ser numérico\n")
        return
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return

    if value < 0:
        print("Negativo\n")
    else:
        print("Positivo\n")


if __name__ == "__main__":
    check_sign()