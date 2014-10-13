# cat.py
import sys


def main():
    for arg in sys.argv:
        if arg == __file__:
            continue
        file = open(arg, "r")
        print (file.read())
        file.close()

if __name__ == '__main__':
    main()
