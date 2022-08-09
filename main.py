def main():
    return

def calc_area(length, height):
    try:
        area = int(length) * int(height)
    except ValueError:
        print("Inputs must be numbers.")
        return
    return area

if __name__ == "__main__":
    length = input("Insert length: ")
    height = input("Insert height: ")
    result = calc_area(length, height)
    if result: print(f"The area is {result}.")