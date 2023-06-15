#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for raw in my_list:
        score = score + (raw[0] * raw[1])
        weight = weight + raw[1]
    return (score / weight)
