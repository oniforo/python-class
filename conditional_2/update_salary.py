"""
Uma empresa resolveu dar um aumento de salário aos seus colaboradores e deseja 
te contratar para desenvolver o programa que calculará os reajustes. O programa 
deve receber, via teclado, o salário de um colaborador. O percentual de 
reajuste é dado segundo os critérios abaixo:
    salários até R$ 1500,00 (incluindo) : aumento de 20%
    salários entre R$ 1500,01 e R$ 2700,00 : aumento de 15%
    salários entre R$ 2700,01 e R$ 3500,00 : aumento de 10%
    salários de R$ 3500,01 em diante : aumento de 8% 
Após o cálculo do reajuste, informe na tela:
    salário antes do reajuste;
    percentual de reajuste aplicado;
    valor do aumento;
    novo salário, após o reajuste.
"""

def main():
    try:
        _salary = input("Inserir salário do colaborador: ")
        salary = float(_salary)
        salary = round(salary, 2)

        if salary <= 0:
            raise ValueError
        elif salary <= 1500:
            base = 0.20
        elif salary <= 2700:
            base = 0.15
        elif salary <= 3500:
            base = 0.10
        else:
            base = 0.08

        new_salary = (1 + base) * salary
        new_salary = round(new_salary, 2)

        print(f"""
        Salário antes do reajuste:  {salary:,.2f}
        Percentual aplicado:        {base * 100} %
        Valor do aumento:           {(new_salary - salary):,.2f}
        Salário após reajuste:      {new_salary:,.2f}
        """)

    except ValueError:
        print("O valor precisa ser numérico e positivo")
    except KeyboardInterrupt:
        print("\nAbortado pelo usuário")


if __name__ == "__main__":
    main()
    