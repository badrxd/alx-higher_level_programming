#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv)
    if length == 1:
        print("0 arguments.")
    else:
        print("{} argument{}:".format((length - 1), 's' if length != 2 else ''))
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
