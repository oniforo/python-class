"""
Create an algorithm that receives two grades of a student
and calculate then print its average
"""

def main():
    try:
        grade1, grade2 = capture_input()
        result = calc_average(grade1, grade2)
        if result:
            print(f"The average is {result}.")
    except:
        return

def capture_input():
    grade1 = input("Insert grade #1: ")
    grade2 = input("Insert grade #2: ")
    try:
        grade1 = float(grade1)
        grade2 = float(grade2)
    except ValueError:
        print("Inputs must be numbers")
        return None, None
    return grade1, grade2

def calc_average(grade1, grade2):
    return (grade1 + grade2) / 2

if __name__ == "__main__":
    main()