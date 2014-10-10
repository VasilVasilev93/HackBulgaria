#MUST OPTIMIZE!!!


def list_to_string(t):
    string = ""
    for k in t:
        string += k
    return string


def symbol_sequence(string, symbol):
    for k in range(0, len(string) - 1):
        if string[k] == symbol and k != len(string) - 1:
            if string[k + 1] == symbol:
                string[k] = ""
    string = space_deleting(string)


def space_deleting(mylist):
    mylist = [i for i in mylist if i != '']
    return mylist


def reduce_file_path(path):
    path = list(path)
    count = 0
    symbol_sequence(path, "/")
    for k in range(0, len(path) - 1):
        if path[k] == "." and path[k] and k != len(path) - 1:
            if path[k + 1] == ".":
                i = k + 1
                while i >= 0:
                    if path[i] == "/":
                        count += 1
                    if count == 2:
                        count = 0
                        break
                    path[i] = ""
                    i -= 1
            else:az 
                path[k] = ""
    path = (space_deleting(path))
    symbol_sequence(path, "/")
    path = (space_deleting(path))
    if path[len(path) - 1] == "/" and len(path) > 1:
        path[len(path) - 1] = ""

    return list_to_string(path)
print (reduce_file_path("/srv/./././././"))
print (reduce_file_path("/etc/../etc/../etc/../"))
