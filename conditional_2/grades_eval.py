from statistics import mean

def grades_eval():
    print("\nRetorna se o aluno foi aprovado (média >= 7.50)\n")

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

    if final_grade < 4:
        concept = "E"
        status = "Reprovado"
    elif final_grade < 6:
        concept = "D"
        status = "Reprovado"
    elif final_grade < 7.5:
        concept = "C"
        status = "Reprovado"
    elif final_grade < 9:
        concept = "B"
        status = "Aprovado"
    else:
        concept = "A"
        status = "Aprovado"
    
    print(f"""
    Nota 1:     {value1:.2f}  
    Nota 2:     {value2:.2f} 
    Média:      {final_grade:.2f}
    Conceito:   {concept}
    
    Aluno {status}!
    """)


if __name__ == "__main__":
    grades_eval()