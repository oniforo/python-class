"""
A terminal utility that allows users to select a function to run

The functions displayed are algorithms with solutions to the
exercises found in ./material/exercicios-iniciais.pdf

The code is type hinted and can be subjected to a type checking
utility such as mypy

It is compliant to Python's styling conventions under PEP-8

All functions ending in *_input captures and treats user input while
others process this treated input and are unit tested in the
test_functions.py file
"""

from typing import Union, Tuple

def main() -> None:
    """
    A user interface to capture and process user input

    Through this interface the user is able to select which of the
    functions they wish to run interactively

    Returns
    -------
    None
    """

    print("""\nSelect the function you want to run
    
    [1] Calculate area of wall
    [2] Calculate average of two grades
    [3] Convert seconds to hours, minutes and seconds
    [4] Convert years, months and days to days
    [5] Calculate weighted average of three grades
    [6] Calculate squared sums and its average
    [7] Calculate customer cost of a car
    
    [0] Cancel
    """)

    try:
        selection = input("Function number: ")
        print("")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")
        return

    if selection == "0":
        return
    elif selection == "1":
        heading("Calculate area of wall")
        calc_area_input()
    elif selection == "2":
        heading("Calculate average of two grades")
        calc_average_input()
    elif selection == "3":
        heading("Convert seconds to hours, minutes and seconds")
        seconds_to_hours_input()
    elif selection == "4":
        heading("Convert years, months and days to days")
        time_in_days_input()
    elif selection == "5":
        heading("Calculate weighted average of three grades")
        calc_weigthed_average_input()
    elif selection == "6":
        heading("Calculate squared sums and its average")
        squared_average_input()
    elif selection == "7":
        heading("Calculate customer cost of a car")
        customer_cost_input()
    else:
        print("\033[91mInvalid option.\033[00m\n")


def heading(heading: str, size=60):
    """
    Creates a heading with dashes above and below centralized string

    Parameters
    ----------
    heading : str
        The string to create the heading from
    size : int, optional
        The length of the heading (default is 60)
    Returns
    -------
    None
    """
    dashes = "-" * size
    margin = " " * int((size - len(heading)) / 2)

    print(dashes)
    print(f"{margin}{heading}{margin}")
    print(f"{dashes}\n")


def calc_area_input() -> None:
    """
    Gets user input, validates and converts it appropriately. 
    
    Gets the length and height of a wall as input, converts them into
    floating point numbers, validates them as positive, calculates
    (using calc_area function) and prints its corresponding area.

    Returns
    -------
    None
    """
    
    try:
        length = input("Enter the length of the wall: ")
        height = input("Enter the height of the wall: ")
        lengthf, heightf = float(length), float(height)
        if lengthf < 0 or heightf < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            area = calc_area(lengthf, heightf)
            area = round(area, 2)
            print(f"\n\033[92mThe area of the wall is {area}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInputs must be numeric.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")
    

def calc_area(length: float, height: float) -> float:
    """
    Calculates the area of the wall

    Parameters
    ----------
    length : float
        The length of the wall
    height : float
        The height of the wall

    Returns
    -------
    float
        The area of the wall
    """
    
    return length * height


def calc_average_input() -> None:
    """
    Gets user input, validates and converts it appropriately.
    
    Gets two grades as input, converts them into floating point 
    numbers, validates them as positive, calculates (using calc_average
    function) and prints their corresponding average.

    Returns
    -------
    None
    """

    try:
        grade1 = input("Enter grade #1: ")
        grade2 = input("Enter grade #2: ")
        grade1f, grade2f = float(grade1), float(grade2)
        if grade1f < 0 or grade2f < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            average = calc_average(grade1f, grade2f)
            average = round(average, 2)
            print(f"\n\033[92mThe average grade is {average}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInputs must be numeric.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")


def calc_average(grade1: float, grade2: float) -> float:
    """
    Calculates the average of two grades

    Parameters
    ----------
    grade1 : float
        The first grade
    grade2 : float
        The second grade

    Returns
    -------
    float
        The average of both grades
    """
    
    return (grade1 + grade2) * 0.5


def seconds_to_hours_input() -> None:
    """
    Gets user input, validates and converts it appropriately.
    
    Gets a time in seconds as input, converts it into an integer,
    validates it as positive, calculates (using seconds_to_hours
    function), formats (using format_hours function) and prints it as
    a time in hours, minutes and seconds.

    Returns
    -------
    None
    """

    try:
        seconds = input("Enter the time in seconds: ")
        secondsi = int(seconds)
        if secondsi < 0:
            print(f"\033[91mInput must be positive.\033[00m")
        else:
            hours, mins, secs = seconds_to_hours(secondsi)
            time = format_hours(hours, mins, secs)
            print(f"\n\033[92m{time}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInput must be an integer.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")


def seconds_to_hours(seconds: int) -> Tuple[int, int, int]:
    """
    Converts a time in seconds into hours, minutes and seconds

    Parameters
    ----------
    seconds : int
        The number of seconds

    Returns
    -------
    (int, int, int)
        The number of hours, minutes and seconds, respectively
    """
    
    hours = seconds // 3600
    mins = seconds % 3600 // 60
    secs = seconds % 3600 % 60
    return hours, mins, secs


def format_hours(hours: int, mins: int, secs: int) -> str:
    """
    Converts hours, minutes and seconds into a descriptive string

    Parameters
    ----------
    hours : int
        The number of hours
    mins : int
        The number of minutes
    secs : int
        The number of seconds

    Returns
    -------
    str
        A descriptive time string
    """
    
    if hours == 0:
        if mins == 0:
            return f"{secs} seconds"
        else:
            return f"{mins} minutes and {secs} seconds"
    else:
        return f"{hours} hours {mins} minutes and {secs} seconds"


def time_in_days_input() -> None:
    """
    Gets user input, validates and converts it appropriately.
    
    Gets years, months and days of an age as input, converts them into
    integer, validates as positive, calculates (using time_in_days
    function) and prints the corresponding time in days.

    Returns
    -------
    None
    """

    try:
        print(f"\033[92mPlease provide years, months and days of an age\033[00m\n")
        _years = input("Years: ")
        _months = input("Months: ")
        _days = input("Days: ")
        years, months, days = int(_years), int(_months), int(_days)
        if years < 0 or months < 0 or days < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            total_days = time_in_days(years, months, days)
            print(f"\n\033[92mTotal time in days is {total_days}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInputs must be integers.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")


def time_in_days(years: int, months: int, days: int) -> int:
    """
    Converts an age given in years, months and days to days

    Considers every year has 365 days and every month has 30 days for
    simplification.

    Parameters
    ----------
    years : int
        The number of years
    months : int
        The number of months
    days : int
        The number of days

    Returns
    -------
    int
        The converted age to days only
    """

    print("\nConsidering a year of 365 and a month of 30 days")
    return years * 365 + months * 30 + days


def calc_weigthed_average_input() -> None:
    """
    Gets user input, validates and converts it appropriately.
    
    Gets three grades as input, converts them into floating point
    numbers, validates them as positive, calculates (using 
    calc_weighted_average function) and prints the corresponding 
    weighted average.

    Returns
    -------
    None
    """
    
    try:
        _grade1 = input("Enter grade #1: ")
        _grade2 = input("Enter grade #2: ")
        _grade3 = input("Enter grade #3: ")
        grade1, grade2, grade3 = float(_grade1), float(_grade2), float(_grade3)
        if grade1 < 0 or grade2 < 0 or grade3 < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            w_average = calc_weighted_average((grade1, grade2, grade3))
            print(f"\n\033[92mThe weighted average grade is {w_average}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInputs must be numeric.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")


def calc_weighted_average(
    grades: Tuple[float, float, float], 
    _weights=(2, 3, 5)
) -> float:
    """
    Calculates the weighted average of three grades

    Parameters
    ----------
    grade : (float, float, float)
        The respective grades
    _weights : (int, int, int), optional
        The respective weights (default is (2, 3, 5))
    
    Returns
    -------
    float
        The weighted average of the three grades
    """
    
    print(f"\nConsidering the weights {_weights}")
    weights = list(map(lambda x: x/sum(_weights), _weights))
    cat = list(zip(grades, weights))
    return sum([round(x * y, 2) for x, y in cat])


def squared_average_input() -> None:
    """
    Gets user input, validates and converts it appropriately.
    
    Gets three positive integers A, B and C as input, validates them,
    calculates (using squared_average function) and prints the 
    following expressions:
        R = (A + B) ^ 2
        S = (B + C) ^ 2
        D = (R + S) / 2

    Returns
    -------
    None
    """

    try:
        print(f"\033[92mPlease provide three positive integers A, B and C\033[00m\n")
        _a = input("A: ")
        _b = input("B: ")
        _c = input("C: ")
        a, b, c = int(_a), int(_b), int(_c)
        if a < 0 or b < 0 or c < 0:
            print(f"\033[91mInputs must be positive.\033[00m")
        else:
            r, s, d = squared_average(a, b, c)
            print(f"\n\033[92mR: {r} S: {s} D: {d}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInputs must be integers.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")

def squared_average(a: int, b: int, c: int) -> Tuple[int, int, float]:
    """
    Runs calculation with the given integers A, B and C

    R = (A + B) ^ 2
    S = (B + C) ^ 2
    D = (R + S) / 2

    Parameters
    ----------
    a : int
        An integer
    b : int
        An integer
    c : int
        An integer

    Returns
    -------
    (int, int, float)
        The results of R, S and D as described above, respectively
    """
    
    print("\n\033[92mThe following will be calculated\033[00m")
    print("\033[92mR = (A + B) ^ 2, S = (B + C) ^ 2 e D = (R + S) / 2\033[00m")
    r = (a + b) ** 2
    s = (b + c) ** 2
    d = (r + s) * 0.5
    return r, s, d


def customer_cost_input() -> None:
    """
    Gets user input, validates and converts it appropriately.
    
    Gets the factory cost of a new car as input, converts it into a
    floating point number, calculates (using customer_cost function) 
    and prints the corresponding customer cost.

    Returns
    -------
    None
    """

    try:
        _cost = input("Enter the factory cost: ")
        cost = float(_cost)
        if cost < 0:
            print(f"\033[91mInput must be positive.\033[00m")
        else:
            cust_cost = customer_cost(cost)
            print(f"\n\033[92mThe total customer cost is {cust_cost}\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInput must be numeric.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")


def customer_cost(factory_cost: float, dist_perc=.28, taxes=.45) -> float:
    """
    Calculates customer cost given the factory cost of a car

    The customer cost takes into account the factory cost and also the
    distributor percentage and taxes

    Parameters
    ----------
    factory_cost : float
        The factory cost of the car
    dist_perc : float, optional
        The distributor percentage (default is .28)
    taxes : float, optional
        The taxes (default is .45)

    Returns
    -------
    float
        The customer cost of the car
    """
    
    print(f"\n\033[92mConsidering a distributor percentage of {round(100 * dist_perc, 2)}%\033[00m")
    print(f"\033[92mConsidering taxes of {round(100 * taxes, 2)}%\033[00m")
    
    cust_cost = (1 + dist_perc + taxes) * factory_cost
    cust_cost = round(cust_cost, 2)
    return cust_cost


if __name__ == "__main__":
    main()
