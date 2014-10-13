# generate_numbers.py
from sys import argv
from random import randint


def main():
    arg1 = argv[1]
    arg2 = argv[2]
    num = ""

    file = open(arg1, "w")
    for i in range(0, int(arg2)):
        num += (str((randint(1, 1000)))) + " "
        file.write(num)
        num = ""
    file.close()

if __name__ == '__main__':
    main()
