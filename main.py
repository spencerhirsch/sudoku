"""
    Authors: Spencer Hirsch, Thomas Johnson
    Course: Introduction to Artificial Intelligence
    Professor: Dr. Mitra
    Project: Pseudo-Sudoku Intermediate Submission
"""

import pandas as pd
import numpy as np
import sys
from board import make_board
import math


"""
    Process the input and validate data. Ensure that the given input
    is in the correct format and set up the board for processing.
"""


def setup(input_size, board_setup):
    board_list = board_setup.split(',') # Break up input string
    board = []                          # Initialize board
    row = []
    count = 1

    """
        Break the input into the correct format so that it takes the shape
        of a traditional board.
    """
    for item in board_list:
        if count % input_size != 0:
            row.append(item)
        else:
            row.append(item)
            board.append(row)
            row = []
        count += 1

    return board


"""
    Solve the puzzle and return the updated board to the callee (main function) for
    further processing. Will be done after each iteration to ensure the algorithm is
    processing one element at a time.
"""

"""
    Iterate through board to find coordinate of an open cell. If found return cordinates.
    If no cell is open then return sentinel values -1, -1.
"""


def find_cell(board, size):
    for i in range (size):
        for j in range (size):
            if board[i][j] == '0':
                return i, j
            
    return -1, -1


"""
    Given the cordinates of an open cell, check if the number we are attempting to place
    will be a valid move. Iterate through row, and then column. Return false at any point
    if we find the move to be invalid, else return true
"""


def valid_move(cord1, cord2, board, size, num):

    # Check row for number
    for i in range (size):
        if board[i][cord2] == str(num):
            #print("Not valid: ", num)
            #print(i, cord2)
            return False

    # Check column for number
    for j in range (size):
        if board[cord1][j] == str(num):
            #print("Not valid: ", num)
            #print(cord1, j)
            return False

    return True

""""
    Backtracking algorithm to solve sudoku puzzle
    Task list so far:
        - Find vacant cell - DONE
        - Check if move is valid - DONE
        - Assign number to valid move - DONE
        - recursively call the function - OPEN
        - Remark cell as empty if solve()... doesn't yield true. - OPEN
            -> This is because the pathway isn't a solution for this number, and we must try another - DONE
        - Upon completion return the solved board - DONE
"""

def solve(board, size):
    
    nums = list(range(1, size + 1))   # list of all possible numbers
    cord1, cord2 = find_cell(board, size)
    print("Checking cords: ", cord1, cord2)

    # Found solution
    if cord1 == -1 and cord2 == -1:
        return True

    for num in nums:
        if (valid_move(cord1, cord2, board, size, num)):
            #print("Valid move: ", num)
            #print(cord1, cord2)

            board[cord1][cord2] = str(num)

            if (solve(board, size)):
                return True

            board[cord1][cord2] = "0"

    return False


"""
    Back-tracking algorithm requires a check to see if the board is of a valid configuration.
    If it is return true if not, return false and continue the search. Checks first that the row,
    doesn't contain any duplicate values and doesn't contain any empty data. Then it does do the
    same to columns.
"""


def is_valid(board):
    for row in board:
        if len(row) != len(set(row)) or ' ' in row:       # Convert list to set to check for duplicates
            return False

    columns = []
    for i in range(len(board)):
        column = [row[i] for row in board]
        columns.append(column)

    for column in columns:
        if len(column) != len(set(column)) or ' ' in column:
            return False

    return True



"""
    Output the board for a better representation for the user. Takes into account
    the size of the input and organizes the board to make it better understood.
    Outputted after each move the AI makes.
"""


def output(board, input_size):
    print("-" * (4 * input_size + 1))
    for row in board:
        index = 0
        for val in row:
            if index == 0:
                print("| %s" % val, end='', sep='', flush=True)
            elif index != input_size - 1:
                print(" | %s" % val, end='', sep='', flush=True)
            else:
                print(" | %s |" % val)
            index += 1
    print("-" * (4 * input_size + 1))


"""
    Driver function that takes the input from the user. Calls all necessary
    function in order to ensure execution of the program.
"""


def main():

    # Reads in input from text file as thats what the doc asked 

    # file_name = sys.argv[1]
    # file = open (file_name, 'r')
    #
    # input_size = int(file.readline())
    # board_setup = file.readline().strip()
    #
    # file.close()
    for i in range(2):
        board_setup, input_size = make_board()
        # input_size = int(math.sqrt(len(board_setup) + 1 / 2))

        #input_size = int(input("Size of board (n x n): "))
        #board_setup = input("Input original board layout by row: ")

        board = setup(input_size, board_setup)              # Set up board with given input
        if is_valid(board):
            output(board, input_size)
            print("Game over.")
        else:
            print("Original Board is: ")
            output(board, input_size)
            if (solve(board, input_size)):
                print("solved board is: ")
                output(board, input_size)
            else:
                print("No solution")
            """"
            dataframe = pd.DataFrame(np.array(board))           # Convert input into pandas dataframe for processing
            dataframe = solve(dataframe, input_size)            # Call function to solve game and return the updated board
            updated_board = dataframe.to_numpy()                # Convert dataframe back to 2d numpy array
            output(updated_board, input_size) 
            """


main()

