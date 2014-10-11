def groupby(func, seq):
    dic = {}
    for k in seq:
        result = (func(k))
        if result not in dic:
            dic[result] = [k]
        else:
            dic[result].append(k)
    return dic

print (groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
