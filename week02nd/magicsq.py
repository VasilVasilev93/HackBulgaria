def magic_square(matrix):
    sumofrows = []
    sumofcolumns = []
    count = 0
    msize = len(matrix)
    for row in range(0, msize):
        sumrow = 0
        sumcolumn = 0
        for column in range(0, msize):
            sumrow += matrix[row][column]
            sumcolumn += matrix[column][row]
        sumofrows.append(sumrow)
        sumofcolumns.append(sumcolumn)

    for k in range(0, msize - 1):
        if sumofrows[k] == sumofrows[k + 1]:
            count += 1

    if sumofcolumns == sumofrows:
        count += 1
    if count == msize:
        return True
    return False

print (magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print (
    (magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
     [16, 3, 10, 5], [9, 6, 15, 4]])))

print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
