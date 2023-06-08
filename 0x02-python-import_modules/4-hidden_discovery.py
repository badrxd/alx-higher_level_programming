#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4i

    ls = dir(hidden_4)

    for word in ls:
        if word.startswith("_"):
            continue
        else:
            print("{}".format(word))
