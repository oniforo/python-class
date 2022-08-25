"""
A pesca amadora em um determinado clube estabelece que os sócios podem pescar 
no máximo 20 kg de pescado. Toda vez que eles trazem um peso de peixes maior
que o estabelecido pelo regulamento de pesca do clube, devem pagar uma multa de
R$ 140,00 por quilo excedente. O clube precisa que você faça um programa que 
leia o peso (peso de peixes) e verifique se há excesso. Se houver, calcular e 
exibir o peso em excesso e o valor da multa. Caso contrário, mostrar uma 
mensagem informando que o sócio está dentro das normas estabelecidas.
"""

def main():
    try:
        _weight = input("Inserir o total de pescado (kg): ")
        weight = float(_weight)

        if 0 <= weight <= 20:
            print("Dentro das normas estabelecidas")
        elif weight < 0:
            raise ValueError
        else:
            excess = weight - 20
            print(f"""
            {round(excess, 5)} kg em excesso
            Multa no valor de R$ {round(140 * excess, 2):.2f}
            """)

    except ValueError:
        print("O valor precisa ser numérico e não negativo")
    except KeyboardInterrupt:
        print("\nAbortado pelo usuário")


if __name__ == "__main__":
    main()
