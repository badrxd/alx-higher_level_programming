#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    valuePrev = 0

    for char in roman_string:
        if char in dic:
            valueCurrent = dic[char]
            if valueCurrent > valuePrev:
                num += valueCurrent - 2 * valuePrev
            else:
                num += valueCurrent
            valuePrev = valueCurrent
        else:
            return 0
    return num
