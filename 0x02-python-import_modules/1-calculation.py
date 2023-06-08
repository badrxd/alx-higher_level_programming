#!/usr/bin/python3
if __name__ == "__main__":
    """ Simple function"""
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    ls = [add, "+", sub, '-', mul, '*', div, '/']
    for i in range(0, 8, 2):
        print("{} {} {} = {}".format(a, ls[i + 1], b, ls[i](a, b)))
