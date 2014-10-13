# concat.py
from sys import argv


def main():
    for arg in argv:
        if arg == __file__:
            continue
        file1 = open(arg, "r")
        with open("MEGAAATRON.txt", "a") as file3:
            file3.write(file1.read())
        file1.close()
        file3.close()


if __name__ == '__main__':
    main()
