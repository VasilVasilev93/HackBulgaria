def iterations_of_nan_expand(expanded):
    nan = "Not a "
    nan1 = ""
    count = 0
    if expanded == "":
        return 0
    for k in expanded:
        if len(nan) == len(nan1):
            if nan1 == nan:
                count += 1
                nan1 = ""
            else:
                return False
        nan1 += k
    return count

print (iterations_of_nan_expand("Show these people!"))
