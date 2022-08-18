"""
Faça um Programa que peça dois números e imprima o maior deles. Caso sejam 
iguais nada deverá ser exibido.
"""

def print_bigger():
    print("\nRetorna o maior entre dois valores numéricos\n")

    try:
        _value1 = input("Inserir o primeiro número: ")
        _value2 = input("Inserir o segundo número: ")
        value1, value2 = float(_value1), float(_value2)
    except ValueError:
        print("O valor precisa ser numérico\n")
        return
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return

    diff = value1 - value2

    if diff > 0:
        print(f"\nO maior é {value1}\n")
    elif diff < 0:
        print(f"\nO maior é {value2}\n")


if __name__ == "__main__":
    print_bigger()