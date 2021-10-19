'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
from typing import Sequence


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

    print("")
        

def num_to_cords(square_num):
    col = square_num
    while(col > 3):
        col -= 3
    row = (square_num - 1) // 3
    return [row, col-1]


def put_on_board(board, mark, square_num):
    cords = num_to_cords(square_num)
    board[cords[0]][cords[1]] = mark


def put_on_board_cords(board, mark):
    row = int(input(f"What row does player \'{mark}\' want to place {mark}?: "))
    col = int(input(f"What col does player \'{mark}\' want to place {mark}?: "))
    board[row][col] = mark


def get_free_squares(board):
    list_of_free_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                list_of_free_squares.append([i, j])
    return list_of_free_squares


def make_random_move(board, mark):
    list_of_free_squares = get_free_squares(board)
    if len(list_of_free_squares) != 0:
        random_index = random.randrange(0, len(list_of_free_squares))
        cords = list_of_free_squares[random_index]
        board[cords[0]][cords[1]] = mark


def make_smart_move(board, mark):
    list_of_free_squares = get_free_squares(board)
    for i in range(len(list_of_free_squares)):
        test_cords = list_of_free_squares[i]
        board[test_cords[0]][test_cords[1]] = mark
        if is_win(board, mark):
            return
        board[test_cords[0]][test_cords[1]] = " "
    
    for i in range(len(list_of_free_squares)):
        test_cords = list_of_free_squares[i]
        board[test_cords[0]][test_cords[1]] = "X"
        if is_win(board, "X"):
            board[test_cords[0]][test_cords[1]] = mark
            return
        board[test_cords[0]][test_cords[1]] = " "

    if board[1][1] == " ":
        board[1][1] = mark
        return
        
    make_random_move(board, mark)


def is_row_all_mark(board, row_i, mark):
    for mark_on_board in board[row_i-1]:
        if mark_on_board != mark:
            return False
    return True


def is_col_all_mark(board, col_i, mark):
    for i in range(len(board)):
        if board[i][col_i-1] != mark:
            return False
    return True


def is_diagonal_all_mark(board, mark):
    if board[1][1] == mark:
        if board[0][0] == mark and board[2][2] == mark:
            return True
        if board[2][0] == mark and board[0][2] == mark:
            return True
    return False


def is_win(board, mark):
    for i in range(len(board)):
        if is_row_all_mark(board, i+1, mark) == True:
            return True
    
    for i in range(len(board[0])):
        if is_col_all_mark(board, i+1, mark) == True:
            return True
    
    if is_diagonal_all_mark(board, mark):
        return True
    
    return False


def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
    
if __name__ == '__main__':
    
    board = make_empty_board()  
    
    while(True):
        print_board_and_legend(board)
        player_square_num = int(input("Choose a square: "))
        put_on_board(board, "X", player_square_num)
    
        if is_win(board, "X"):
            print("Player 'X' wins!")
            break
        print()
    
        make_smart_move(board, "O")
    
        if is_win(board, "O"):
            print("Computer 'O' wins!")
            break
    
        if len(get_free_squares(board)) == 0:
            print("TIE!")
            break

    print_board_and_legend(board)