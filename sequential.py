"""
A terminal utility that allows users to select a function to run

The functions displayed are algorithms with solutions to the
exercises found in ./material/exercicios-sequencial.docx

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
    
    [1] Calculate the ETA for a download
    [2] Calculate financing's installment
    [3] Calculate the cost of fuel
    [4] Price and quantity of paint
    [5] Price and quantity of paint (2 scenarios)
    [6] Energy and minimum wage
    [7] Standard discount scenarios
    
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
        heading("Calculate the ETA for a download")
        calc_download_eta_input()
    elif selection == "2":
        heading("Calculate financing's installment")
        calc_installment_input()
    elif selection == "3":
        heading("Calculate the cost of fuel")
        calc_fuel_cost_input()
    elif selection == "4":
        heading("Price and quantity of paint")
        calc_paint_amount1_input()
    elif selection == "5":
        heading("Price and quantity of paint (2 scenarios)")
        calc_paint_amount2_input()
    elif selection == "6":
        heading("Energy and minimum wage")
        calc_energy_input()
    elif selection == "7":
        heading("Standard discount scenarios")
        calc_discount_scenarios_input()
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


def calc_download_eta_input() -> None:
    """
    Gets user input, validates and converts it appropriately. 
    
    Gets a file size and average speed as input, converts them into
    floating point numbers, calculates (using calc_download_eta 
    function) and prints its corresponding ETA.

    Returns
    -------
    None
    """
    
    try:
        _filesize = input("Enter the size of the file (in MB): ")
        _speed = input("Enter the download speed (in Mbps): ")
        filesize, speed = float(_filesize), float(_speed)
        if filesize <= 0 or speed <= 0:
            print(f"\n\033[91mInput must be positive and non-zero.\033[00m\n")
        else:
            eta_minutes = calc_download_eta(filesize, speed)
            eta_minutes = round(eta_minutes, 2)
            print(f"\n\033[92mThe ETA is {eta_minutes} minutes\033[00m\n")
    except ValueError:
        print(f"\n\033[91mInputs must be numeric.\033[00m\n")
    except KeyboardInterrupt:
        print(f"\033[91mUser aborted.\033[00m\n")
    

def calc_download_eta(filesize: float, speed: float) -> float:
    """
    Calculates the ETA of a download given a filesize and speed

    Parameters
    ----------
    filesize : float
        The size of the file in MB
    speed : float
        The average download speed in Mbps

    Returns
    -------
    float
        The ETA of the download in minutes
    """

    for _key, _value in locals().items():
        if _value <= 0:
            print(f"Variable {_key} can not be negative or zero")
            raise ValueError()
        elif type(_value) != float:
            print(f"Type of variable {_key} must be float (got {type(_key)})")
            raise TypeError()

    filesize_megabits = filesize * 8
    download_seconds = filesize_megabits / speed
    download_minutes = download_seconds / 60
    download_minutes = round(download_minutes, 2)

    return download_minutes


def calc_installment_input():
    """
    Gets user input, validates and converts it appropriately.

    [Further describe the function]

    Returns
    -------
    None
    """
    
    return


def calc_installment():
    """
    
    """
    
    return


def calc_fuel_cost_input():
    """
    Gets user input, validates and converts it appropriately.

    [Further describe the function]

    Returns
    -------
    None
    """
    
    return


def calc_fuel_cost():
    """
    
    """
    
    return


def calc_paint_amount1_input():
    """
    Gets user input, validates and converts it appropriately.

    [Further describe the function]

    Returns
    -------
    None
    """
    
    return


def calc_paint_amount1():
    """
    
    """
    
    return


def calc_paint_amount2_input():
    """
    Gets user input, validates and converts it appropriately.

    [Further describe the function]

    Returns
    -------
    None
    """
    
    return


def calc_paint_amount2():
    """
    
    """
    
    return


def calc_energy_input():
    """
    Gets user input, validates and converts it appropriately.

    [Further describe the function]

    Returns
    -------
    None
    """
    
    return


def calc_energy():
    """
    
    """
    
    return


def calc_discount_scenarios_input():
    """
    Gets user input, validates and converts it appropriately.

    [Further describe the function]

    Returns
    -------
    None
    """
    
    return


def calc_discount_scenarios():
    """
    
    """
    
    return


if __name__ == "__main__":
    main()
