#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string is None or not isinstance(roman_string, str):
        return number
    rom = {'I': 1, 'V': 5, 
           'X': 10, 'L': 50,
           'C': 100, 'D': 500,
           'M': 1000}
    for i in range(len(roman_string)):
        if roman_string[i] in rom:
            if i > 0 and rom[roman_string[i]] > rom[roman_string[i - 1]]:
                number += rom[roman_string[i]] - 2 * rom[roman_string[i - 1]]
            else:
                number += rom[roman_string[i]]
    return number
