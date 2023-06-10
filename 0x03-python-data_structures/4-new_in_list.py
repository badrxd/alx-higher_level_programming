#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_ls = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return new_ls
    new_ls[idx] = element
    return new_ls
