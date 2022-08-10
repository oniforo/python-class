from typing import Union, Tuple

"""
1. Faça um algoritmo que leia a largura e altura de uma parede (em 
metros) e exiba a área da Parede.
2. Faça um algoritmo que leia duas notas de um aluno, calcule e exiba a 
média aritmética das notas.
3. Faça um algoritmo que leia o tempo de duração de um evento em uma 
fábrica expressa em segundos e mostre-o expresso em horas, minutos e 
segundos.
4. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, 
meses e dias e mostre-a expressa apenas em dias.
5. Faça um algoritmo que leia as 3 notas de um aluno e calcule a média 
final deste aluno. Considerar que a média é ponderada e que os pesos
das notas são 2,3 e 5, respectivamente.
6. Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) 
e calcule a seguinte expressão:
R = (A + B) ^ 2, S = (B + C) ^ 2 e D = (R + S) / 2
7. O custo ao consumidor de um carro novo é a soma do custo de fábrica 
com a percentagem do distribuidor e dos impostos (aplicados ao custo 
de fábrica). Supondo que a percentagem do distribuidor seja de 28% e 
os impostos de 45%, escrever um algoritmo que leia o custo de fábrica 
de um carro e escreva o custo ao consumidor
"""

def main():

    print("""\nSelect the function you want to run
    
    [1] Calculate area of wall
    [2] Calculate average of two grades
    [3] Convert seconds to hours, minutes and seconds
    [4] Convert years, months and days to days
    [5] Calculate weighted average of three grades
    [6] Calculate sqaured sums and its average
    [7] Calculate customer cost of a car
    
    [0] Cancel
    """)
    try:
        selection = input("Function number: ")
        print("")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")
        return

    if selection == "0":
        return
    elif selection == "1":
        calc_area_input()
    elif selection == "2":
        calc_average_input()
    elif selection == "3":
        seconds_to_hours_input()
    elif selection == "4":
        time_in_days_input()
    elif selection == "5":
        calc_weigthed_average_input()
    elif selection == "6":
        squared_average_input()
    elif selection == "7":
        customer_cost_input()
    else:
        print("\033[91mInvalid option.\033[00m\n")


def calc_area_input():
    try:
        length = input("Enter the length of the wall: ")
        height = input("Enter the height of the wall: ")
        lengthf, heightf = float(length), float(height)
        if lengthf < 0 or heightf < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            area = calc_area(lengthf, heightf)
            print(f"\033[92mThe area of the wall is {area}\033[00m")
    except ValueError:
        print(f"\033[91mInputs must be numeric.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")
    

def calc_area(length: float, height: float) -> float:
    return length * height


def calc_average_input():
    try:
        grade1 = input("Enter grade #1: ")
        grade2 = input("Enter grade #2: ")
        grade1f, grade2f = float(grade1), float(grade2)
        if grade1f < 0 or grade2f < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            average = calc_average(grade1f, grade2f)
            print(f"\033[92mThe average grade is {average}\033[00m")
    except ValueError:
        print(f"\033[91mInputs must be numeric.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")


def calc_average(grade1: float, grade2: float) -> float:
    return (grade1 + grade2) * 0.5


def seconds_to_hours_input():
    try:
        seconds = input("Enter the time in seconds: ")
        secondsi = int(seconds)
        if secondsi < 0:
            print(f"\033[91mInput must be positive.\033[00m")
        else:
            hours, mins, secs = seconds_to_hours(secondsi)
            time = format_hours(hours, mins, secs)
            print(f"\033[92m{time}\033[00m")
    except ValueError:
        print(f"\033[91mInput must be an integer.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")


def seconds_to_hours(seconds: int) -> Tuple[int, int, int]:
    hours = seconds // 3600
    mins = seconds % 3600 // 60
    secs = seconds % 3600 % 60
    return hours, mins, secs


def format_hours(hours: int, mins: int, secs: int) -> str:
    if hours == 0:
        if mins == 0:
            return f"{secs} seconds"
        else:
            return f"{mins} minutes and {secs} seconds"
    else:
        return f"{hours} hours {mins} minutes and {secs} seconds"


def time_in_days_input():
    try:
        print(f"\033[92mPlease provide years, months and days of an age\033[00m")
        _years = input("Years: ")
        _months = input("Months: ")
        _days = input("Days: ")
        years, months, days = int(_years), int(_months), int(_days)
        if years < 0 or months < 0 or days < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            total_days = time_in_days(years, months, days)
            print(f"\033[92mTotal time in days is {total_days}\033[00m")
    except ValueError:
        print(f"\033[91mInputs must be integers.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")


def time_in_days(years: int, months: int, days: int) -> int:
    print("\033[92mConsidering a year of 365 and a month of 30 days\033[00m")
    return years * 365 + months * 30 + days


def calc_weigthed_average_input():
    try:
        _grade1 = input("Enter grade #1: ")
        _grade2 = input("Enter grade #2: ")
        _grade3 = input("Enter grade #3: ")
        grade1, grade2, grade3 = float(_grade1), float(_grade2), float(_grade3)
        if grade1 < 0 or grade2 < 0 or grade3 < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            w_average = calc_weighted_average((grade1, grade2, grade3))
            print(f"\033[92mThe weighted average grade is {w_average}\033[00m")
    except ValueError:
        print(f"\033[91mInputs must be numeric.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")


def calc_weighted_average(
    grades: Tuple[float, float, float], 
    _weights=(2, 3, 5)
) -> float:
    print(f"\033[92mConsidering the weights {_weights}\033[00m")
    weights = list(map(lambda x: x/sum(_weights), _weights))
    cat = list(zip(grades, weights))
    return sum([round(x * y, 2) for x, y in cat])


def squared_average_input():
    try:
        print(f"\033[92mPlease provide three positive integers A, B and C\033[00m")
        _a = input("A: ")
        _b = input("B: ")
        _c = input("C: ")
        a, b, c = int(_a), int(_b), int(_c)
        if a < 0 or b < 0 or c < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            r, s, d = squared_average(a, b, c)
            print(f"\033[92mR: {r} S: {s} D: {d}\033[00m")
    except ValueError:
        print(f"\033[91mInputs must be integers.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")

def squared_average(a: int, b: int, c: int) -> Tuple[int, int, float]:
    print("\033[92mThe following will be calculated\033[00m")
    print("\033[92mR = (A + B) ^ 2, S = (B + C) ^ 2 e D = (R + S) / 2\033[00m")
    r = (a + b) ** 2
    s = (b + c) ** 2
    d = (r + s) * 0.5
    return r, s, d


def customer_cost_input():
    try:
        _cost = input("Enter the factory cost: ")
        cost = float(_cost)
        if cost < 0:
            print(f"\033[91mInput must be positive.\033[00m")
        else:
            cust_cost = customer_cost(cost)
            print(f"\033[92mThe total customer cost is {cust_cost}\033[00m")
    except ValueError:
        print(f"\033[91mInput must be numeric.\033[00m")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m")


def customer_cost(factory_cost: float, dist_perc=0.28, taxes=.45) -> float:
    print(f"\033[92mConsidering a distributor percentage of {round(100 * dist_perc, 2)}%\033[00m")
    print(f"\033[92mConsidering taxes of {round(100 * taxes, 2)}%\033[00m")
    return (1 + dist_perc + taxes) * factory_cost


if __name__ == "__main__":
    main()
