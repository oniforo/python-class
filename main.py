def main():
    return

def calc_area(length, height):
    return int(length) * int(height)

if __name__ == "__main__":
    length = input("Insert length: ")
    height = input("Insert height: ")
    result = calc_area(length, height)
    print(f"The area is {result}.")