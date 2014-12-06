X = "X"
O = "O"
EMPTY = " "
DRAW = "DRAW"
NUM_SQUARES = 9


def ask_move(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])


def possible_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square + 1)
    return moves


def determine_winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return DRAW

    return None


def human_move(board, human):
    legal = possible_moves(board)
    move = None
    while move not in legal:
        move = ask_move("Move (1 - 9):", 1, NUM_SQUARES + 1)
        if move not in legal:
            print("\nSquare already taken, choose another one.\n")
    return move - 1


def block_fork(board, computer, human):
    for move in possible_moves(board):
        board[move - 1] = human
        if determine_winner(board) == human:
            print ("Block the attack!")
            return move - 1

        board[move - 1] = EMPTY
    return False


def best_possible_move(board, computer, human):
    BEST_MOVES = (5, 1, 3, 7, 9, 2, 4, 6, 8)
    for move in BEST_MOVES:
        if move in possible_moves(board):
            print ("Movin around...")
            return move - 1
    return False


def win_if_possible(board, computer, human):
    for move in possible_moves(board):
        board[move - 1] = computer
        if determine_winner(board) == computer:
            print ("Strike!")
            return move - 1
        board[move - 1] = EMPTY
    return False


def computer_move(board, computer, human):
    computer_board = board[:]

    return win_if_possible(computer_board, computer, human) or block_fork(computer_board, computer, human)\
        or best_possible_move(computer_board, computer, human)


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def display_winner(the_winner, computer, human):
    if the_winner != DRAW:
        print(the_winner, "won!\n")
    else:
        print("Draw result.\n")

    if the_winner == computer:
        print("Haha! In your face!")

    elif the_winner == human:
        print("You won!")


def main():
    computer, human = O, X
    turn = X
    board = new_board()
    display_board(board)

    while not determine_winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = determine_winner(board)
    display_winner(the_winner, computer, human)


if __name__ == '__main__':
    main()
