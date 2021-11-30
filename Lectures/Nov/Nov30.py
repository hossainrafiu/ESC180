def o_will_lose(board):
    """Return True iff o starts and loses with perfect play"""
    if santa.x_won(invert_board(board)):
        return False
    if santa.x_won(board):
        return True

    if board_full(board):
        return False

    # For every placement of O on the board.
    # if x_will_win(board with the placement) is True
    # -> o_will_lose is True

    # If there is a placement such that x_will_win(board with the placement)
    # is False, than we need to return False

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] == "O"
                if not x_will_win(board):
                    board[i][j] = " "
                    return False
    return True

def x_will_win(board):
    """Return True iff X starts and wins with perfect play."""

    # If there is a placement of x such that o_will_lose(board with placement)
    # is True, then return True

    # If for no placement of x o_will_lose(board with placement) is True,
    # return False

    if santa.x_won(board):
        return True
    if santa.x_won(inverted_board(board)):
        return False

    if board_full(board):
        return False

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] == "X"
                if o_will_lose(board):
                    board[i][j] = " "
                    return True
    return False


"""



"""