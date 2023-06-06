#!/usr/bin/python3
def uppercase(str):
    char = ""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            char = chr(ord(str[i]) - 32)
        else:
            char = str[i]
        if i != (len(str) - 1):
            print(char, end="")
        else:
            print(char)
