#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    ln = len(argv)
    if ln == 1:
        print("0 arguments.")
    else:
        print("{} argument{}:".format((ln - 1), 's' if ln != 2 else ''))
        for i in range(1, ln):
            print("{}: {}".format(i, argv[i]))
