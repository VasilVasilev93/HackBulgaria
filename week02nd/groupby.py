def groupby(func, seq):
    dic = {}
    for k in seq:
        result = (func(k))
        if result not in dic:
            dic[result] = [k]
        else:
            dic[result].append(k)
    return dic
