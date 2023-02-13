### author: Caroline Leicht
### date: 2-3-23
###
### description: This code runs the game of Battleship. One user plays against the computer. The user places four ships on their board and then takes turn with
### the computer to try and hit eachothers ships. The first to hit all four ships wins.
###
### bugs: hit and miss symbols distort board

import random                           # random choice
import string                           # import string (for alphabet)
string.ascii_lowercase                  # alphabet
alphabet = string.ascii_lowercase       # alphabet
alphabet = alphabet[0:25]               # alphabet without the letter 'z'

start_board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]    # list, starting user screen

def print_board(board):
### function prints the battleship board as the game goes
### input: board, function will be called with different boards to print
### output: returns printed board
    start = f''' _____ _____ _____ _____ _____
|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |  {board[0][3]}  |  {board[0][4]}  |
 _____ _____ _____ _____ _____
|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |  {board[1][3]}  |  {board[1][4]}  |
 _____ _____ _____ _____ _____
|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |  {board[2][3]}  |  {board[2][4]}  |
 _____ _____ _____ _____ _____
|  {board[3][0]}  |  {board[3][1]}  |  {board[3][2]}  |  {board[3][3]}  |  {board[3][4]}  |  
 _____ _____ _____ _____ _____
|  {board[4][0]}  |  {board[4][1]}  |  {board[4][2]}  |  {board[4][3]}  |  {board[4][4]}  |
 _____ _____ _____ _____ _____'''
    return start                        # returns board

print(f'''
Directions: 
Please follow the prompts on the screen. If you fail to enter a valid input, you will miss a turn. When either you or the computer hits a
ship, it will be marked with an 💥. When you miss, it will be marked with an ❌. First to sink all four ships wins. Good luck!

your starting board:
{print_board(start_board)}      
''')                                    # prints the start board

def user_screen(new_board, target_board):
### function prints both the target board (that the player is shooting at) and the players board (that shows the computer's moves)
### inputs: new_board - the board the computer is shooting at; target_board - the board the player is shooting at
### outputs: screen - the printed board
    screen = print(f'''
your board:                                             target board:
 _____ _____ _____ _____ _____                           _____ _____ _____ _____ _____                        
|  {new_board[0][0]}  |  {new_board[0][1]}  |  {new_board[0][2]}  |  {new_board[0][3]}  |  {new_board[0][4]}  |                         |  {target_board[0][0]}  |  {target_board[0][1]}  |  {target_board[0][2]}  |  {target_board[0][3]}  |  {target_board[0][4]}  |
 _____ _____ _____ _____ _____                           _____ _____ _____ _____ _____
|  {new_board[1][0]}  |  {new_board[1][1]}  |  {new_board[1][2]}  |  {new_board[1][3]}  |  {new_board[1][4]}  |                         |  {target_board[1][0]}  |  {target_board[1][1]}  |  {target_board[1][2]}  |  {target_board[1][3]}  |  {target_board[1][4]}  |
 _____ _____ _____ _____ _____                           _____ _____ _____ _____ _____
|  {new_board[2][0]}  |  {new_board[2][1]}  |  {new_board[2][2]}  |  {new_board[2][3]}  |  {new_board[2][4]}  |                         |  {target_board[2][0]}  |  {target_board[2][1]}  |  {target_board[2][2]}  |  {target_board[2][3]}  |  {target_board[2][4]}  |
 _____ _____ _____ _____ _____                           _____ _____ _____ _____ _____
|  {new_board[3][0]}  |  {new_board[3][1]}  |  {new_board[3][2]}  |  {new_board[3][3]}  |  {new_board[3][4]}  |                         |  {target_board[3][0]}  |  {target_board[3][1]}  |  {target_board[3][2]}  |  {target_board[3][3]}  |  {target_board[3][4]}  | 
 _____ _____ _____ _____ _____                           _____ _____ _____ _____ _____
|  {new_board[4][0]}  |  {new_board[4][1]}  |  {new_board[4][2]}  |  {new_board[4][3]}  |  {new_board[4][4]}  |                         |  {target_board[4][0]}  |  {target_board[4][1]}  |  {target_board[4][2]}  |  {target_board[4][3]}  |  {target_board[4][4]}  |
 _____ _____ _____ _____ _____                           _____ _____ _____ _____ _____''')
    return screen                                                               # returns printed board

def pick_location():
### function allows the user to pick the location of their battleships on their board
### inputs: NONE
### outputs: letters - 4 letters of the alphabet (excluding z) chosen by the user
    print('you have four ships to place on your board. you may select four letters from your starting board. your ships will be placed in their locations')
    x = 0
    while x == 0:
        letters = input('please input four letters separated by commas: ')          # str, ex: 'a,b,c,d' letters chosen by the user
        letters = letters.split(',')                                                # list, ex: "['a', 'b', 'c', 'd']" makes list, string divided by commas
        length = len(letters)                                                       # int, ex: 4, checks input
        if length == 4:                                                             # bool, if length of letters is 4
            string = letters[0] + letters[1] + letters[2] + letters[3]              # str, ex: 'abcd'
            if string.isalpha():                                                    # bool, if string is made up of letters in the alphabet
                break                                                               # break while loop
    else:                                                                           # bool, if length of letters isn't 4
            x = 0                                                                   # int, 0, for while loop
    return letters                                                                  # returns list of four letters

def show_board(letters, board):
### function takes user chosen letters and replaces them with 'X' in board list
### inputs: letters - user chosen str of 4 letters for pick_location() function; board - list of letters in the alphabet (except z)
### outputs: board - new board with 4 chosen letters replaced with 'X'
    count = 0                                   # int, 0, to subscript for each letter in str letters
    num = len(letters)                          # int, length of letter str
    while count < num:                          # bool, when count is less than 4
        second_move = letters[count]            # str, ex: 'a' subsript for each letter in str letters
        if second_move == 'a':                  # bool, if letter in str is 'a'
            board[0][0] = 'X'                   # str, 'X'
        if second_move == 'b':                  # bool, if letter in str is 'b'
            board[0][1] = 'X'                   # str, 'X'
        if second_move == 'c':                  # bool, if letter in str is 'c'
            board[0][2] = 'X'                   # str, 'X'
        if second_move == 'd':                  # bool, if letter in str is 'd'
            board[0][3] = 'X'                   # str, 'X'
        if second_move == 'e':                  # bool, if letter in str is 'e'
            board[0][4] = 'X'                   # str, 'X'

        if second_move == 'f':                  # bool, if letter in str is 'f'
            board[1][0] = 'X'                   # str, 'X'
        if second_move == 'g':                  # bool, if letter in str is 'g'
            board[1][1] = 'X'                   # str, 'X'
        if second_move == 'h':                  # bool, if letter in str is 'h'
            board[1][2] = 'X'                   # str, 'X'
        if second_move == 'i':                  # bool, if letter in str is 'i'
            board[1][3] = 'X'                   # str, 'X'
        if second_move == 'j':                  # bool, if letter in str is 'j'
            board[1][4] = 'X'                   # str, 'X'

        if second_move == 'k':                  # bool, if letter in str is 'k'
            board[2][0] = 'X'                   # str, 'X'
        if second_move == 'l':                  # bool, if letter in str is 'l'
            board[2][1] = 'X'                   # str, 'X'
        if second_move == 'm':                  # bool, if letter in str is 'm'
            board[2][2] = 'X'                   # str, 'X'
        if second_move == 'n':                  # bool, if letter in str is 'n'
            board[2][3] = 'X'                   # str, 'X'
        if second_move == 'o':                  # bool, if letter in str is 'o'
            board[2][4] = 'X'                   # str, 'X'

        if second_move == 'p':                  # bool, if letter in str is 'p'
            board[3][0] = 'X'                   # str, 'X'
        if second_move == 'q':                  # bool, if letter in str is 'q'
            board[3][1] = 'X'                   # str, 'X'
        if second_move == 'r':                  # bool, if letter in str is 'r'
            board[3][2] = 'X'                   # str, 'X'
        if second_move == 's':                  # bool, if letter in str is 's'
            board[3][3] = 'X'                   # str, 'X'
        if second_move == 't':                  # bool, if letter in str is 't'
            board[3][4] = 'X'                   # str, 'X'

        if second_move == 'u':                  # bool, if letter in str is 'u'
            board[4][0] = 'X'                   # str, 'X'
        if second_move == 'v':                  # bool, if letter in str is 'v'
            board[4][1] = 'X'                   # str, 'X'
        if second_move == 'w':                  # bool, if letter in str is 'w'
            board[4][2] = 'X'                   # str, 'X'
        if second_move == 'x':                  # bool, if letter in str is 'x'
            board[4][3] = 'X'                   # str, 'X'
        if second_move == 'y':                  # bool, if letter in str is 'y'
            board[4][4] = 'X'                   # str, 'X'

        count = count + 1                       # int, ex: '1' to subscript in str letters

    return board                                # returns new board after str letters have been replaced by 'X'

def computer(alphabet):
### function picks random letters to place computer battleships
### inputs: alphabet - str of letter in alphabet (except z)
### outputs: alphabet - str of letters in alphabet (except z) with four letters replaced by 'X'
    letter1 = random.choice(alphabet)           # str, ex: 'a' random letter in alphabet (except z)
    alph = alphabet.replace(letter1, 'X')       # str, ex: 'Xbcdefghijklmnopqrstuvwxy'
    alphabet = alphabet.replace(letter1, '')    # str, ex: 'bcdefghijklmnopqrstuvwxy' alphabet (except z and letter1)

    letter2 = random.choice(alphabet)           # str, ex: 'b' random letter in alphabet (except z and letter1)
    alph = alph.replace(letter2, 'X')           # str, ex: 'XXcdefghijklmnopqrstuvwxy'
    alphabet = alphabet.replace(letter2, '')    # str, ex: 'cdefghijklmnopqrstuvwxy' alphabet (except z, letter1 and letter2)

    letter3 = random.choice(alphabet)           # str, ex: 'c' random letter in alphabet (except z, letter1 and letter2)
    alph = alph.replace(letter3, 'X')           # str, ex: 'XXXdefghijklmnopqrstuvwxy'
    alphabet = alphabet.replace(letter3, '')    # str, ex: 'defghijklmnopqrstuvwxy' alphabet (except z, letter1, letter2 and letter3)

    letter4 = random.choice(alphabet)           # str, ex: 'd' random letter in alphabet (except z, letter1, letter2 and letter3)
    alph = alph.replace(letter4, 'X')           # str, ex: 'XXXXefghijklmnopqrstuvwxy'

    return alph                                 # return str, ex: 'XXXXefghijklmnopqrstuvwxy'

def location(int, alphabet):
### function either takes user input for move letter or randomly chooses a letter in the alphabet (except z and previous computer moves)
### inputs: int - either 1 or 2, dictate whether it is the user's move or the computer's; alphabet - str of letters in alphabet (except z and previous computer
###         moves)
### outputs: move - one letter in alphabet (except z or previous computer moves)
    if int == 1:                                            # bool, if int equals 1, means it is player's move
        move = input('please input letter for move: ')      # str, ex: 'a' single letter input
    if int == 2:                                            # bool, if int equals 2, means it is computer's move
        move = random.choice(alphabet)                      # str, ex: 'b', randomly chooses letter in alphabet (except z and previous computer moves)
    return move                                             # returns letter, either user or computer generated

def move(board, computerboard, move, blank):
### function puts an ❌ or 💥 in location on board based on location(int, alphabet) function
### inputs: board - list of letters in alphabet (except z); computerboard - str of letters in alphabet (except z) and four 'X's; move - letter dictated by
###         location(int, alphabet) function
### outputs: board - list with letters replaced with ❌ or 💥

    if move in computerboard:                               # bool, if letter move is in str of letters
        computerboard = computerboard.replace(move, '❌')   # str, ex: 'XXXXefghijklmno❌qrstuvwxy'

        x = 0                                               # int, '0' for while loop
        while x < 5:                                        # bool, while x is less than 5
            y = 0                                           # int, '0' for while loop
            while y < 5:                                    # bool, while y is less than 5
                if board[x][y] == move:                     # bool, if letter move is equal to spot in board
                    board[x][y] = '❌'                      # list, ex: 'XXXXefghijklmno❌qrstuvwxy' replace letter with ❌
                else:                                       # bool, if letter move is not equal to spot on board
                    y = y + 1                               # int, ex: '1' for while loop
            x = x + 1                                       # int, ex: '1' for while loop

        print('MISS')

    else:                                                   # bool, if move hits a battleship
        x = 0                                               # int, '0' for while loop
        while x < 5:                                        # bool, while x is less than 5
            y = 0                                           # int, '0' for while loop
            while y < 5:                                    # bool, while y is less than 5
                if board[x][y] == move:                     # bool, if letter move is equal to spot in board
                    board[x][y] = '💥'                      # list, ex: 'XX💥Xefghijklmnopqrstuvwxy' replace letter with 💥
                else:                                       # bool. if letter move is not equal to spot in baord
                    y = y + 1                               # int, ex: '1' for while loop
            x = x + 1                                       # int, ex: '1' for while loop
        print('HIT')

        new = str(board)                                    # str, ex: [['X', 'X', 'X', 'X', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', '❌', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
        if 'X' in new:                                      # bool, if 'X' in new str, for computer hits
            x = 0                                           # int, '0' for counter
            while x < 5:                                    # bool, while x is less than 5
                y = 0                                       # int, '0' for counter
                while y < 5:                                # bool, while y is less than 5
                    if blank[x][y] == move:                 # bool, if letter in list is same letter as move
                        break                               # break while loop
                    else:                                   # bool, if letter in list is not same letter as move
                        y = y + 1                           # int, ex: '1' for counter
                if blank[x][y] == move:                     # bool, if letter in list is same letter as move
                    break                                   # break loop
                else:                                       # bool, if letter in list is not same letter as move
                    x = x + 1                               # int, ex: '1' for counter

            board[x][y] = '💥'                               # str, replace letter in board with '💥'

    return board                                            # return board with value replace by ❌ or 💥

def win(board):
### function determines whether either the player or computer has won the game
### input: board - list with hits and miss values shown as ❌ and 💥
### output: win_count - if win_count equals four there is a winner, if it is less than four the game continues (value can not be greater than 4)
    string = board[0][0] + board[0][1] + board[0][2] + board[0][3] + board[0][4] + board[1][0] + board[1][1] + board[1][2] + board[1][3] + board[1][4] + board[2][0] + board[2][1] + board[2][2] + board[2][3] + board[2][4] + board[3][0] + board[3][1] + board[3][2] + board[3][3] + board[3][4] + board[4][0] + board[4][1] + board[4][2] + board[4][3] + board[4][4]
    # str with same values as list board

    start = len(string)                                     # int, 25, length of string, should be equal to length of alphabet without z
    new = string.replace('💥', '')                          # str, ex: 'efghijklmnopqrstuvwxy' takes out 💥 in string
    end = len(new)                                          # int, ex: 21, length of string without 💥s

    win_count = start - end                                 # int, ex: 4, ending length of string subtracted from starting length of string
    return win_count                                        # int, ex 4

def remove_letters(letters, move):
### function removes letters that have been hit from letters string generated by computer(alphabet) function
### inputs: letters - list, length between 1 and 4 of single letters of the alphabet; move - str, one letter generated by computer
### outputs: letters - list, length between 1 and 3 of single letters of the alphabet
    letters = str(letters)                                  # str, ex "['a', 'b', 'c', 'd']"
    letters = letters.replace(',', '')                      # str, ex: "['a' 'b' 'c' 'd']"
    letters = letters.replace('[', '')                      # str, ex: "'a' 'b' 'c' 'd']"
    letters = letters.replace(']', '')                      # str, ex: "'a' 'b' 'c' 'd'"
    letters = letters.replace("'", '')                      # str, ex: "a b c d"
    letters = letters.replace(' ', '')                      # str, ex: "abcd"
    letters = letters.replace(move, '')                     # str, ex: "bcd", removes move from string
    letters = list(letters)                                 # list, ex ['b', 'c', 'd'], list without move letter
    return letters                                          # list, ex: ['b', 'c', 'd']

def main():
### function calls all other functions
### inputs: N/A
### outputs: ' ' - spacer line and removes 'None' return
    board = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
    target = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
    blank_board = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'],['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
    uneditted = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'],['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
    # four of the same basic arrays: five lists, five strings in each list, letters in the alphabet (except z)

    letters = pick_location()                                               # list, ex: ['a', 'b', 'c', 'd'], calls pick_location() function
    new = show_board(letters, board)                                        # list, calls show_board(), ex: [['X', 'X', 'X', 'X', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
    your_board = new[0][0] + new[0][1] + new[0][2] + new[0][3] + new[0][4] + new[1][0] + new[1][1] + new[1][2] + new[1][3] + new[1][4] + new[2][0] + new[2][1] + new[2][2] + new[2][3] + new[2][4] + new[3][0] + new[3][1] + new[3][2] + new[3][3] + new[3][4] + new[4][0] + new[4][1] + new[4][2] + new[4][3] + new[4][4]
    # string version of list new generated by show_board() function

    screen = user_screen(new, target)                                       # NoneType, prints user screen
    print(' ')                                                              # spacer line
    computer_board = computer(alphabet)                                     # str, ex: 'XbcdefXhijklmXopqrstuvXxy' calls computer() function
    alph = 'abcdefghijklmnopqrstuvwxy'                                      # str, letters in the alphabet except z

    x = 0                                                                   # int, 0, for counter
    while x == 0:                                                           # bool, when x equals 0
        player_move = location(1, alph)                                     # str, ex: 'a', player generated, calls location() function
        target = move(target, computer_board, player_move, uneditted)       # list, calls move() function
        player_win = win(target)                                            # int, ex: 4, calls win() function
        if player_win == 4:                                                 # bool, if player_win equals 4, if player hits four battleships
            user_screen(new_board, target)                                  # NoneType, prints user screen
            print('''
YOU WIN!''')                                                                # spacer line, then alerts user that they won
            break                                                           # breaks while loop
        else:                                                               # bool, if player_win doesn't equal 4, no winner yet
            x = 0                                                           # int, 0

        com_move = location(2, alph)                                        # str, ex: 'a', computer generated, calls location() function
        if com_move in letters:                                             # bool, if str com_move is in letters from pick_location() function
            letters = remove_letters(letters, com_move)                     # list, ex: '['a','b','c']' letters without com_move

        alph = alph.replace(com_move, '')                                   # str, ex 'bcdefghijklmnopqrstuvwxy', alphabet without z or com_move
        print(f'''
computer move: {com_move}''')                                               # spacer line, then alerts user of the computer's move
        blank_board = move(blank_board, your_board, com_move, uneditted)    # list, calls move() function

        new_board = show_board(letters, blank_board)                        # list, calls show_board() function

        com_win = win(blank_board)                                          # int, ex: 4, calls win() function
        if com_win == 4:                                                    # bool if str com_win equals 4, if computer hits 4 of player's battleships
            user_screen(new_board, target)                                  # NoneType, prints user screen
            print('''
COMPUTER WINS!''')                                                          # spacer line, then alerts user that computer won
            break                                                           # breaks while loop
        else:                                                               # bool, if str com_win doesn't equal 4, no winner yet
            x = 0                                                           # int, 0

        user_screen(new_board, target)                                      # NoneType, prints user screen
        print(' ')                                                          # spacer line

    return ' '                                                              # spacer line, removes 'None' return


print(main())                                                               # calls and prints main() function,B,