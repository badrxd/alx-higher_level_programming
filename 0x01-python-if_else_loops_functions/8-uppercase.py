#!/usr/bin/python3
def uppercase(str):
    text = ""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            text += chr(ord(str[i]) - 32)
        else:
            text += str[i]
    print("{}".format(text))
