"""
Faça um programa que leia duas notas de um aluno. O programa deve calcular a 
média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
    A mensagem "Reprovado", se a média for menor do que sete
"""

from statistics import mean

def validate_grade():
    print("\nRetorna se o aluno foi aprovado (média >= 7)\n")

    try:
        _value1 = input("Inserir a primeiro nota: ")
        _value2 = input("Inserir a segunda nota: ")
        value1, value2 = float(_value1), float(_value2)
    except ValueError:
        print("O valor precisa ser numérico\n")
        return
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return

    final_grade = mean([value1, value2])

    if final_grade >= 7:
        print(f"\nAprovado com média {round(final_grade, 2)}\n")
    else:
        print(f"\nReprovado com média {round(final_grade, 2)}\n")


if __name__ == "__main__":
    validate_grade()