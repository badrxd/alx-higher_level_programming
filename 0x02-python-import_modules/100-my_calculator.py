#!/usr/bin/python3

def find_op(op):
    ls_op = ['+', '-', '*', '/']
    if op not in ls_op:
        return True
    return False


def result(a, op, b):

    from calculator_1 import add, sub, mul, div

    a = int(a)
    b = int(b)

    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == "'*'":
        return mul(a, b)
    else:
        return div(a, b)


if __name__ == "__main__":
    from sys import argv, exit

    a, op, b = argv[1], argv[2], argv[3]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if find_op(op):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, result(a, op, b)))
