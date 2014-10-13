# wc.py
from sys import argv


def main():
    arg1 = argv[1]
    arg2 = argv[2]
    if arg1 == "chars":
        file = open(arg2, "r")
        sum = 0
        for char in file.read():
            sum += 1
        file.close()
        print (sum)

    elif arg1 == "words":
        file = open(arg2, "r")
        sum = 0
        for word in file.read().split():
            sum += 1
        print (sum)
    elif arg1 == "lines":
        file = open(arg2, "r")
        sum = 0
        for line in file.read().split("\n"):
            sum += 1
        print (sum)
    else:
        print ("Command %s, not available!!!" % arg1)


if __name__ == '__main__':
    main()
