# cat.py
from sys import argv


def cat(filename):
    file_contents = ''
    with open(filename, 'r') as f:
            file_contents = f.read()
    return file_contents


def main():
    file_to_read = argv[1]
    print (cat(file_to_read))

if __name__ == '__main__':
    main()
