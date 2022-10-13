from math import sqrt

def get_coefficients(a, b, c):

    delta = calculate_delta(a, b, c)
    print(f"Delta: {delta}")
    if delta > 0:
        r1, r2 = -b + sqrt(delta), -b - sqrt(delta)
        r1, r2 = r1 / 2 * a, r2 / 2 * a
        print(f"Duas raízes: {r1} e {r2}")
    elif delta < 0:
        print("Não possui resultado real")
    else:
        r1 = -b / 2 * a
        print(f"Única raiz {r1}")


def calculate_delta(a, b, c):
    return (b ** 2 - 4 * a * c)


get_coefficients(1, 2, 1)