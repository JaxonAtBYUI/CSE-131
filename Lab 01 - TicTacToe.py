# 1. Name:
#      Jaxon Hamm
#
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
#
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
#
# 4. What was the hardest part? Be as specific as possible.
#      Using the template. I'm not good at understanding what other people mean
#      when they write certain things in their code. I felt that I needed to
#      use the template but I would have written it different had I written the
#      code from scratch. Because of this it took more time and brain power than
#      it really should have.
#
# 5. How long did it take for you to complete the assignment?
#      2 hrs 30 mins

import json
#region CONSTANTS
# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }
#endregion

def read_board():
    '''Read the previously existing board from the file if it exists.'''
    try:
        file = open('ttts.json', 'r')
        text = file.read()
        sav_board = json.loads(text)
        board = sav_board['board']
    except:
        board = blank_board["board"].copy()
    
    return board

def save_board(board):
    '''Save the current game to a file.'''
    assert (len(board) == 9)
    sav_board = {
              "board": board
              }
    with open('ttts.json', 'w') as file:
            json.dump(sav_board, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("---+---+---")
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("---+---+---")
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def is_x_turn(board):
    '''Determine whose turn it is.'''
    count = 0
    for square in board:
        if square != BLANK:
            count += 1

    if count % 2:
        return False
    return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    while not game_done(board, ""):
        # Display the board
        display_board(board)

        # Get input from player.
        square = 0
        not_valid = True
        while not_valid:
            if is_x_turn(board):
                square = input("X> ")
            else: 
                square = input("O> ")
            
            # Input Validation
            if square == 'q':
                not_valid = False
            elif square.isnumeric() and int(square) > 0 and int(square) < 10:
                not_valid = False
            else:
                print("ERROR: Your input must be 1-9 or q.")
        
        # Test to see if they are done playing. If so, save and exit.
        if square == 'q':
            save_board(board)
            return 1

        # Write to the board.
        square = int(square)
        if is_x_turn(board):
            board[square-1] = X
        else:
            board[square-1] = O
    
    # See if they would like to play again.
    if input("Would you like to play a new game? (y/n)") == 'y':
        return 2

    return 3

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
board = read_board()
continue_playing = True
while continue_playing:
    temp = play_game(board)

    if temp == 1:
        continue_playing = False
    elif temp == 2:
        board = blank_board["board"].copy()
    elif temp == 3:
        board = blank_board["board"].copy()
        save_board(board)
        continue_playing = False

