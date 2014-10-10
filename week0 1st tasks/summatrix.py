def sum_matrix(m):
    newsum = 0
    for k in m:
        newsum += sum(k)
    return newsum

print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
