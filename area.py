def main():
    try:
        length, height = capture_input()
        result = calc_area(length, height)
        if result:
            print(f"The area is {result}.")
    except:
        return

def capture_input():
    length = input("Insert length: ")
    height = input("Insert height: ")
    try:
        length = float(length)
        height = float(height)
    except ValueError:
        print("Inputs must be numbers")
        return None, None
    return length, height

def calc_area(length, height):
    return length * height

if __name__ == "__main__":
    main()