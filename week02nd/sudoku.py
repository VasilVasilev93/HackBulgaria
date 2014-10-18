def is_increasing(seq):
    for k in range(0, len(seq) - 1):
        if seq[k] >= seq[k + 1]:
            return False
    return True


def transponse_matrix(matrix):
    r = []
    rm = []

    for row in range(0, len(matrix)):
        for column in range(0, len(matrix)):
            r.append(matrix[column][row])
        rm.append(list(r))
        r = []

    return rm


def check_rows_columns(matrix):
    checkList = []
    count = 0

    for row in range(0, 9):
        for col in range(0, 9):
            checkList.append(matrix[row][col])
        checkList = sorted(checkList)
        if is_increasing(checkList):
            count += 1
            checkList = []

    transponsedmatrix = transponse_matrix(matrix)

    for row in range(0, 9):
        for col in range(0, 9):
            checkList.append(transponsedmatrix[row][col])
        checkList = sorted(checkList)
        if is_increasing(checkList):
            count += 1
            checkList = []

    if count == 18:
        return True


def create_submatrix_3x3(matrix):
    checkList = []
    count = 0
    i = 0
    j = 3
    x = 0
    y = 3
    for submatrix in range(0, 3):
        for row in range(i, j):
            for col in range(x, y):
                checkList.append(matrix[row][col])
            x += 3
            y += 3
            checkList = sorted(checkList)
            if is_increasing(checkList):
                count += 1
                checkList = []
        i += 3
        j += 3
        x = 0
        y = 0
    if count == 9:
        return True


def sudoku_solved(matrix):
    if check_rows_columns(matrix) and create_submatrix_3x3(matrix):
        return True
    return False

print (sudoku_solved([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
