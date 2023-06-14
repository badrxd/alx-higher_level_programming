#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ls = []
    for i in my_list:
        if i == search:
            i = replace
        ls.append(i)
    return(ls)
