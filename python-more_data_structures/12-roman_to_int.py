#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0

    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    for x in range(len(roman_string)):
        if x > 0 and r_dict[roman_string[x]] > r_dict[roman_string[x - 1]]:
            number += r_dict[roman_string[x]] - 2 * r_dict[roman_string[x - 1]]
        else:
            number += r_dict[roman_string[x]]

    return number
