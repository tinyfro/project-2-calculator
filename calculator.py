#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""calculator.py: Lightweight calculator application (still deciding if GUI or Console based). Made for educational and fun purposes."""

__author__      = "tinyfro"
__copyright__   = "Copyright 2023, tinyfro"


import os

def main():
    print("Welcome to this basic calculator application.")
    input("Press Enter to start...")
    user_input()

def clear_cns():
    """Checks for the operating system type -> clears all previous entries and displays from the console."""
    return os.system("cls" if os.name == "nt" else "clear")

def user_input():
    nums_operators = []
    num = int(input("Enter a number:\n"))
    operator = input("Enter an operator:\n")
    while True:
        if num.isdigit() and isinstance(operator, str):
            num = int(num)
            clear_cns()
            operator = str(operator)
            clear_cns()
            nums_operators.append(num)
            nums_operators.append(operator)
        else:
            print("That was not a number, please try again.")
            break

def addition():
    pass

def subtraction():
    pass

def multiplication():
    pass

def division():
    pass

main()
