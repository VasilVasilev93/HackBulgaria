def is_decreasing(seq):
    for k in range(0, len(seq) - 1):
        if seq[k] <= seq[k+1]:
            return False
    return True


print (is_decreasing([100, 50, 20]))
