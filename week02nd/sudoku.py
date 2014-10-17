def elements_unique(listA):
    if len(set(listA)) == len(listA):
        return True
    return False


def reversed_matrix(matrix):
    r = []
    rm = []

    for row in range(0, len(matrix)):
        for column in range(0, len(matrix)):
            r.append(matrix[column][row])
        rm.append(list(r))
        r = []

    return rm


def sudoku_solved(sudoku):
    count = 0
    rev = reversed_matrix(sudoku)
    for k in range(0, 9):
        if elements_unique(sudoku[k]) and elements_unique(rev[k]):
            count += 1

    m = []
    n = []
    for i in range(3, 6):
        for j in range(3, 6):
            m.append(sudoku[i][j])
        n.append(list(m))
        m = []
    return n

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
