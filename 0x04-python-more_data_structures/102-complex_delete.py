#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    i = 0
    for key in a_dictionary:
        if a_dictionary[key] == value:
            i += 1
    while(i != 0):
        for key in a_dictionary:
            if a_dictionary[key] == value:
                del a_dictionary[key]
                i -= 1
                break
    return a_dictionary
