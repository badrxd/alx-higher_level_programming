def best_score(a_dictionary):
    if not a_dictionary:
        return None
    num  = 0
    name = ""
    for key in a_dictionary:
        if a_dictionary[key] > num:
            num = a_dictionary[key]
            name = key
    return(name)
