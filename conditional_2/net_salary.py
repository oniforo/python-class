def net_salary():
    
    try:
        _value1 = input("\nInserir o número de horas trabalhadas: ")
        _value2 = input("Inserir o valor da hora: ")
        value1, value2 = float(_value1), float(_value2)
        if value1 <= 0 or value2 <= 0:
            raise ValueError
    except ValueError:
        print("O valor precisa ser numérico e positivo\n")
        return
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return

    gross_salary = round(value1 * value2, 2) # salário bruto

    income_tax = calc_income_tax(gross_salary) # faixa de IR
    gross_income_tax_deduced = income_tax[0] * gross_salary # bruto sem IR

    social_security = 0.11 * (1 - income_tax[0]) * gross_salary # INSS
    syndicate = 0.005 * gross_salary # sindicato
    fgts = 0.08 * gross_salary # FGTS

    total_deductions =  gross_income_tax_deduced + social_security + syndicate
    net_salary = gross_salary - total_deductions

    ir = income_tax[1]

    print(f"""
    Salário Bruto:                  R$ {gross_salary:,.2f}
    (-) IR ({ir}%):                 R$ {gross_income_tax_deduced:,.2f}
    (-) Sindicato (0.5%):           R$ {syndicate:,.2f}
    (-) INSS (11%):                 R$ {social_security:,.2f}
    FGTS (8%):                      R$ {fgts:,.2f}
    Total de descontos:             R$ {total_deductions:,.2f}
    Salário Líquido:                R$ {net_salary:,.2f}
    """)


def calc_income_tax(gross_salary: float) -> float:
    if gross_salary <= 1903.98:
        return 0.000, "0.00"
    elif gross_salary <= 2826.65:
        return 0.075, "7.50"
    elif gross_salary <= 3751.05:
        return 0.150, "15.0"
    elif gross_salary <= 4664.68:
        return 0.225, "22.5"
    else:
        return 0.275, "27.5"
        

if __name__ == "__main__":
    net_salary()