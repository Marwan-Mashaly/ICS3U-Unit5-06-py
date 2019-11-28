#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program rounds decimal numbers to a decimal point

import math


def round_decimal(decimal_number, decimal_point_check):
    # This function rounds to decimal point given

    answer = decimal_number[0] * (10 ** decimal_point_check)
    answer = answer + 0.5
    round_int = int(answer)
    final_answer = round_int / (10 ** decimal_point_check)

    decimal_number[0] = final_answer


def main():
    # This function gets input from user
    decimal_number = []
    number = input("Enter a number to round: ")
    decimal_point = input("Enter to which decimal point you want to round: ")
    print("")
    try:
        number_check = float(number)
        decimal_point_check = float(decimal_point)
        decimal_number.append(number_check)
        round_decimal(decimal_number, decimal_point_check)
        print(decimal_number)

    except Exception:
        print("Invalid Integer ")
        print("")


if __name__ == "__main__":
    main()
