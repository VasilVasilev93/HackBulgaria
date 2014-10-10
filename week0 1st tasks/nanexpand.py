def nan_expand(times):
    nan = ""
    if times == 0:
        return ""
    else:
        for i in range(0, times):
            nan += "Not a "
    nan += "NaN"
    return nan

print (nan_expand(5))
