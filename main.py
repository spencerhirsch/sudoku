"""
    Authors: Spencer Hirsch, Thomas Johnson
    Course: Introduction to Artificial Intelligence
    Professor: Dr. Mitra
    Project: Pseudo-Sudoku Intermediate Submission
"""

import pandas as pd
import numpy as np
import sys


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
    print(board)  # Testing purposes to ensure that the 2d matrix is correct

    return board


"""
    Solve the puzzle and return the updated board to the callee (main function) for
    further processing. Will be done after each iteration to ensure the algorithm is
    processing one element at a time.
"""

def find_cell(board, input_size):
    for i in range (input_size):
        for j in range (input_size):
            if board[i][j] == '0':
                return i, j
            
    return -1, -1

def valid_move(cord1, cord2):


    return True

def solve(dataframe, input_size):
    # for row in dataframe:
    nums = list(range(1, input_size + 1))
    print(nums)
    cord1, cord2 = find_cell(dataframe, input_size)

    # Found solution
    if cord1 == -1 and cord2 == -1:
        return True

    """"
    for num in nums:
        if (valid_move(cord1, cord2)):

            dataframe[cord1][cord2] = num

            if (solve(dataframe, input_size)):
                return True

            dataframe[cord1][cord2] = "0"
    """

    return dataframe


"""
    Back-tracking algoirthm requires a check to see if the board is of a valid configuration.
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

    file_name = sys.argv[1]
    file = open (file_name, 'r')

    input_size = int(file.readline())
    board_setup = file.readline()

    file.close()

    #input_size = int(input("Size of board (n x n): "))
    #board_setup = input("Input original board layout by row: ")

    board = setup(input_size, board_setup)              # Set up board with given input
    if is_valid(board):
        output(board, input_size)
        print("Game over.")
    else:
        dataframe = pd.DataFrame(np.array(board))           # Convert input into pandas dataframe for processing
        dataframe = solve(dataframe, input_size)                        # Call function to solve game and return the updated board
        updated_board = dataframe.to_numpy()                # Convert dataframe back to 2d numpy array
        output(updated_board, input_size)                   # Call the output function to show user the progress


main()

