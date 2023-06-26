#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    result = ""
    for i in range(x):
        try:
            result += str(my_list[i])
        except IndexError:
            i = i - 1
            break
    print(result)
    return (i + 1)
