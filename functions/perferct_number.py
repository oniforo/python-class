from itertools import combinations
from functools import reduce

def get_divisors(number: int, divisors=[1], i=2) -> bool:
    
    while i <= number:
        if number % i == 0:
            print(i)
            number = number / i
            divisors.append(i)
        else:
            i += 1

    return divisors


def get_permutations(divisors: list, div_comb=[]):

    for i in range(2, len(divisors)):
        div_comb += list(combinations(divisors, i))

    return list(div_comb)


def list_divisors(permutations):
    result = [reduce((lambda x, y: x * y), permutation) for permutation in permutations]
    return [1] + sorted((set(result)))[:-1]


def is_perfect_number(number: int, divisors: list):
    total = sum(divisors)
    print(f"A soma dos divisores é {total}")
    return total == number


if __name__ == "__main__":

    number = 496
    a = get_divisors(number)
    b = get_permutations(a)
    c = list_divisors(b)
    d = is_perfect_number(number, c)

    print(c, d)
