#!/usr/bin/env python3
def print_last_digit(number):
    result = (number % 10) if number >= 0 else (-number % 10)
    print(result, end='')
    return result
