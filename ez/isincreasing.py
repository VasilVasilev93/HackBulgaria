def is_increasing(seq):
    for k in range(0, len(seq) - 1):
        if seq[k] >= seq[k+1]:
            return False
    return True


print (is_increasing([1, 1, 3, 4, 5]))
