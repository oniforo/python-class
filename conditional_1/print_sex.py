"""
Faça um Programa que leia uma letra do teclado e verifique se uma letra 
digitada é "F" ou "M". Conforme a letra escrever: 

    F - Feminino
    M - Masculino
    Sexo Inválido

Assumir a digitação em caixa alta (maiúscula)
"""

def print_sex():
    print("\nRetorna se o valor inserido é F ou M\n")

    try:
        _value = input("Inserir o sexo (F ou M): ")
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return

    value = _value.upper()

    if value == "M":
        print("M - Masculino\n")
    elif value == "F":
        print("F - Feminino\n")
    else:
        print("Sexo inválido\n")


if __name__ == "__main__":
    print_sex()
