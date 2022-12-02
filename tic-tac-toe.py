### Author: Caroline Leicht
### Date: 11-30-22
###
### Description: This code runs the game of tic-tac-toe. It is a two player game. X player goes first. O player goes second.
### the game will result in the X player winning, the O player winning, or a tie
###
### bug: only accepts letters a - i, will break with others

start_board = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]           # list, tictactoe board at the beginning of the game
print('Player X gets first move. Player O gets second move. Good luck!')    # communicates with users

def print_board(board):
### function prints the tic tac toe board as the game goes
### input: board, in beginning of game function prints start board, function will be called with different boards to print after
### output: returns printed board
    start = f''' _____ _____ _____  
|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  | 
 _____ _____ _____ 
|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  | 
 _____ _____ _____     
|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |   
 _____ _____ _____ '''
    return start                                                            # returns board

print(' ')                                                                  # blank line between board and next print statement
print(print_board(start_board))                                             # prints board at beginning of game

def move(board, letter, y):
### function allows users to place an X or O on the spot they chose
### inputs: board (list); letter (str that represents the spot the user has chosen); y (int that dictates whether it is X or O's turn)
### output: new booard (list) after letter has been replaced with an X or O
    if letter == 'a':               # bool, if user selects spot a
        if y == 0:                  # bool, if X player's turn
            board[0][0] = 'X'       # str, replaces 'a' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[0][0] = 'O'       # str, replace 'a' with 'O'
        return board                # list, return board
    elif letter == 'b':             # bool, if user selects spot b
        if y == 0:                  # bool, if X player's turn
            board[0][1] = 'X'       # str, replace 'b' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[0][1] = 'O'       # str, replace 'b' with 'O'
        return board                # list, return board
    elif letter == 'c':             # bool, if user selects spot c
        if y == 0:                  # bool, if X player's turn
            board[0][2] = 'X'       # str, replace 'c' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[0][2] = 'O'       # str, replace 'c' with 'O'
        return board                # list, return board
    elif letter == 'd':             # bool, if user selects spot d
        if y == 0:                  # bool, if X player's turn
            board[1][0] = 'X'       # str, replace 'd' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[1][0] = 'O'       # str, replace 'd' with 'O'
        return board                # list, return board
    elif letter == 'e':             # bool, if user selects spot e
        if y == 0:                  # bool, if X player's turn
            board[1][1] = 'X'       # str, replace 'e' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[1][1] = 'O'       # str, replace, 'e' with 'O'
        return board                # list, return board
    elif letter == 'f':             # bool, if user selects spot f
        if y == 0:                  # bool, if X player's turn
            board[1][2] = 'X'       # str, replace 'f' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[1][2] = 'O'       # str, replace 'f' with 'O'
        return board                # list, return board
    elif letter == 'g':             # bool, if user selects g
        if y == 0:                  # bool, if X player's turn
            board[2][0] = 'X'       # str, replace 'g' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[2][0] = 'O'       # str, replace 'g' with 'O'
        return board                # list, return board
    elif letter == 'h':             # bool, if user selects spot h
        if y == 0:                  # bool, if X player's turn
            board[2][1] = 'X'       # str, replace 'h' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[2][1] = 'O'       # str, replace 'h' with 'O'
        return board                # list, return board
    elif letter == 'i':             # bool, if user selects spot i
        if y == 0:                  # bool, if X player's turn
            board[2][2] = 'X'       # str, replace 'i' with 'X'
        elif y == 1:                # bool, if O player's turn
            board[2][2] = 'O'       # str, replace 'i' with 'O'
        return board                # list, return board

def X(board):
### function takes input from X player
### inputs: board (list); y (int that dictates who's turn it is)
### outputs: returns x_player (str, player input)
    print(' ')                                                                                          # blank spacer line
    x_player = input('Player X, please input the letter spot where you would like to place an X: ')     # str, ex: 'a', user communicates where they would like to place an 'X'
    print(' ')                                                                                          # blank spacer line
    return x_player                                                                                     # str, player input

def O(board):
### function takes input from X player
### inputs: board (list); y (int that dictates who's turn it is)
### outputs: returns o_player (str, player input)
    print(' ')                                                                                          # blank spacer line
    o_player = input('Player O, please input the letter spot where you would like to place an O: ')     # str, ex: 'a', user communicates where they would like to place an 'O'
    print(' ')                                                                                          # blank spacer line
    return o_player                                                                                     # str, player input

def win(board):
### function determines who wins the game
### input: board (list)
### output: score (int; if score = 1 X wins, if score = -1 O wins, if score = 0 game continues)
    if board[0] == ['X', 'X', 'X'] or board[1] == ['X', 'X', 'X'] or board[2] == ['X', 'X', 'X']:       # bool, potential winning combination
        score = 1                                                                                       # int, 1, X player wins
        return score                                                                                    # int, return 1
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':                              # bool, potential winning combination
        score = 1                                                                                       # int, 1, X player wins
        return score                                                                                    # int, return 1
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':                              # bool, potential winning combination
        score = 1                                                                                       # int, 1, X player wins
        return score                                                                                    # int, return 1
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':                              # bool, potential winning combination
        score = 1                                                                                       # int, 1, X player wins
        return score                                                                                    # int, return 1
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':                              # bool, potential winning combination
        score = 1                                                                                       # int, 1, X player wins
        return score                                                                                    # int, return 1
    elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':                              # bool, potential winning combination
        score = 1                                                                                       # int, 1, X player wins
        return score                                                                                    # int, return 1

    if board[0] == ['O', 'O', 'O'] or board[1] == ['O', 'O', 'O'] or board[2] == ['O', 'O', 'O']:       # bool, potential winning combination
        score = -1                                                                                      # int, -1, O player wins
        return score                                                                                    # int, return -1
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':                              # bool, potential winning combination
        score = -1                                                                                      # int, -1, O player wins
        return score                                                                                    # int, return -1
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':                              # bool, potential winning combination
        score = -1                                                                                      # int, -1, O player wins
        return score                                                                                    # int, return -1
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':                              # bool, potential winning combination
        score = -1                                                                                      # int, -1, O player wins
        return score                                                                                    # int, return -1
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':                              # bool, potential winning combination
        score = -1                                                                                      # int, -1, O player wins
        return score                                                                                    # int, return -1
    elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':                              # bool, potential winning combination
        score = -1                                                                                      # int, -1, O player wins
        return score                                                                                    # int, return -1

    else:                                                                                               # bool, no player has won
        score = 0                                                                                       # int, 0, game continues
        return score                                                                                    # int, return 0

def main():
### main function, calls all other functions
### no intputs
### output: prints board and communicates results of game to users
    board = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]     # list, board before edited in functions
    y = 0                                                           # int, 0, variable will dictate which player's turn it is
    turns = 0                                                       # int, 0, variable counts number of inputs the users have played

    while turns < 9:                                                # loop, so game continues until someone wins or a tie is reached
        x_player = X(board)                                         # str, ex: 'a', input from user, calls X() function
        board = move(board, x_player, y)                            # list, new board after 'X' has been substituted for user input letter
        print(print_board(board))                                   # print, call print_board() function
        score = win(board)                                          # int, ex: '1', calls win() function, determines if there is a winner yet
        if score == 1:                                              # bool, if score = 1, player X wins
            return print('''                                        
X player won the game!
''')                                                                # 1st line: spacer line; 2nd line: 'X player won the game!'; 3rd line: spacer line
        y = y + 1                                                   # int, 1, tells move() function to place an 'O' for next turn
        turns = turns + 1                                           # int, ex: '1', controls while loop

        if turns >= 8:                                              # bool, if turns = 8 and no one has won, the board is full
            return print('''
the game has ended in a tie
''')                                                                # 1st line: spacer line; 2nd line: 'the game has ended in a tie'; 3rd line: spacer line

        o_player = O(board)                                         # str, ex: 'b', input from user, calls O() function
        board = move(board, o_player, y)                            # list, new board after 'O' has been substituted for user input letter
        print(print_board(board))                                   # print, call print_board() function
        score = win(board)                                          # int, ex: '-1', calls win() function, determines if there is a winner yet
        if score == -1:                                             # bool, if score = -1, player O wins
            return print('''
O player won the game!
''')                                                                # 1st line: spacer line; 2nd line: 'O player won the game!'; 3rd line: spacer line
        y = y - 1                                                   # int, 0, tells move() function to place an 'X' for next turn
        turns = turns + 1                                           # int, ex: '2', controls while loop

print(main())               