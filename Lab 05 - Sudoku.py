# 1. Name:
#      Jaxon Hamm
#
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
#
#  3. Assignment Description:
#      Run a game of Sudoku
# 
# 4. What was the hardest part? Be as specific as possible.
#      I completed it last week so I ended up adding an automatic solver to it.
#      The automatic solver works. The first iteration of it was incredibly slow,  
#      taking a few days to solve the hardest board. It turns out print statements
#      are incredibly slow, so after rearanging the avoud 400+ memory checks every
#      step through the loop and removing the print statement, the program can now
#      solve the hardest board given in about 10 minutes.
#
# 5. How long did it take for you to complete the assignment?
#      0 hours

import math
import json
import copy
import os

os.system("")
GREEN = '\033[92m'
ENDC = '\033[0m'

CHAR_COORDS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# Get filename from the user and read the file.
def open_file():
    not_valid = True
    while not_valid:
        filename = input("What is the filename? ")
        # filename = "SudokuE.json"
        try:
            file = open(filename, 'r')
            text = file.read()
            sav_board = json.loads(text)
            board = sav_board['board']
            not_valid = False
        except:
            print("That is not a valid file. Please try again.")

    return board

# Save the board to a file.
def save_file(playing_board):
    sav_board = {
        "board" : playing_board
    }
    filename = input("What would you like to save the file as? ")
    with open(filename, 'w') as file:
            json.dump(sav_board, file)

# Run the function calls and trivial tasks needed for the game to function.
def game(board):
    playing_board = copy.deepcopy(board)
    
    # We just run until the user saves and exits
    while True:
        # Display
        display(board, playing_board)

        # Get Coordinates and or save
        coordinates = get_coord(board)
        if coordinates == -1:
            save_file(playing_board)
            return
        
        # Get and run user action
        user_action(board, playing_board, coordinates)

# Display the board to the user.
def display(board, playing_board):
    print("   A B C D E F G H I")
    for y in range(9):
        print(str(y+1) + "  ", end="")
        for x in range(9):

            # Print bold if its from the original board, the value, or a space.
            if board[y][x] != 0:
                print(str(board[y][x]), end="")
            elif playing_board[y][x] != 0:
                print(GREEN + str(playing_board[y][x]) + ENDC, end="")
            else:
                print(' ', end="")
             
            # Add the vertiacl seperators or a space.
            if x == 2 or x == 5:
                print('|', end="")
            else:
                print(" ", end="")
        
        # Print the endline for the row, and add a separator if needed.
        print()
        if y == 2 or y == 5:
            print("   -----+-----+-----")

# Get a valid Coordinate from the user and convert it to usable coordinates.
def get_coord(board):
    ERROR = "Please enter a valid coordinate or 'Q'."
    while True:
        y = -1
        x = -1
        print("Specify a coordinate to edit or 'Q' to save and quit.")
        response = input("> ")
        if len(response) > 2:

            # Ask the user to input things we can actually use and then restart.
            print(ERROR)
            continue

        for letter in response:
            if letter.isnumeric():
                y = int(letter) -1
            else:
                # Tell the game to save and quit
                if letter.upper() == 'Q':
                    return -1
                elif letter.upper() in CHAR_COORDS:
                    x = CHAR_COORDS.index(letter.upper())
        
        if 0 <= y <= 8 and 0 <= x <= 8:
            if board[y][x] == 0:
                return (x, y)
            else: 
                print("You cannot place a value in a square that has a white value.")
        else:
            print(ERROR)

# Run the input action at the user's specified coordinate.
def user_action(board, playing_board, coordinates):
    
    letter_coords = str(CHAR_COORDS[coordinates[0]]) + str(coordinates[1] + 1)
    user_input = -1

    while True:
        user_input = input("What number goes in " + letter_coords +"? " )

        # If they put in a value, check it and change the board if its valuable.
        if user_input.isnumeric() and 0 <= int(user_input) <= 9:
            if validate(playing_board, coordinates)[int(user_input)]:
                playing_board[coordinates[1]][coordinates[0]] = int(user_input)
                return
            else:
                print("That is not a valid value for " + letter_coords +".")
                return
        elif user_input.isalpha():

            # If they put in 'S' then tell the user what the valid values are.
            if user_input.upper() == 'S':
                print("The valid inputs at " + letter_coords + " are: ", end="")
                valid_inputs = validate(playing_board, coordinates)
                for index in range(10):
                    if valid_inputs[index] == True:
                        print(str(index) + ' ', end="")
                print()
                return

            # If they put in 'Z' automagically solve the entire board for the user :)
            elif user_input.upper() == 'Z':
                    playing_board = solver(board, playing_board)
                    return

# Validate whether a value is valid at a given (x,y) in the sudoku board.
def validate(playing_board, coordinates):
    valid_inputs = [True]*10
    
    # Check the box
    box_column = math.floor(coordinates[1] / 3)
    box_row = math.floor(coordinates[0] / 3)
    for y in range(box_column * 3, (box_column * 3) + 3):
        for x in  range(box_row * 3, (box_row * 3) + 3):
            valid_inputs[playing_board[y][x]] = False

    # Check the row
    for x in range(0, 9):
        valid_inputs[playing_board[coordinates[1]][x]] = False

    # Check the column
    for y in range(0, 9):
        valid_inputs[playing_board[y][coordinates[0]]] = False
    
    return valid_inputs

# Automatically solve a sudoku board and display it for the user.
def solver(board, playing_board):
    x = 0
    y = 0
    going_right = True
    solved = False
    counter = 0

    while not solved:
        
        # Check to see if we've moved off the board in the x direction
        if x < 0:
            y -= 1
            x = 8
        if x > 8:
            y += 1
            x = 0

        
        # Determine if we've solved the board or if it is unsolvable.
        if y < 0:
            print("There is no solution to this board.")
            return
        if y > 8:
            print("The board has been solved.")
            print(counter)
            return
            

        if board[y][x] != 0:
            if going_right:
                x += 1
            else:
                x -= 1
        else:
            going_right = True
            checking = True
            value = playing_board[y][x]
            valid_inputs = validate(playing_board, (x, y))
            while checking:
                value += 1
                if value == 10:
                    playing_board[y][x] = 0
                    going_right = False
                    checking = False
                    x -= 1
                elif valid_inputs[value]:
                    playing_board[y][x] = value
                    checking = False

                    x += 1
        
        counter += 1

# This is all that I need to make the game work after all the function.
board = open_file()
game(board)
