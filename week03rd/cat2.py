# cat2.py
from sys import argv


def cat2(filename):
    file_content = ""
    for item in filename:
        print (item)
        file = open(item, "r")
        file_content += file.read()
        file.close()
    print (file_content)
    return file_content


def main():
    filename = []
    for i in range(1, len(argv)):
        filename.append(str(argv[i]))
    cat2(filename)

if __name__ == '__main__':
    main()
