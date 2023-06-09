#!/usr/bin/python3

def find_op(op, ls_op):
    if op not in ls_op:
        return True
    return False


if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, op, b = int(argv[1]), str(argv[2]), int(argv[3])
    ls_op = {"+": add, "-": sub, "*": mul, "/": div}

    if find_op(op, ls_op):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, ls_op[op](a ,b)))
