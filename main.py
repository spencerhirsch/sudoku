"""
    Authors: Spencer Hirsch, Thomas Johnson
    Course: Introduction to Artificial Intelligence
    Professor: Dr. Mitra
    Project: Pseudo-Sudoku Intermediate Submission
"""

import pandas as pd
import numpy as np


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


def solve(dataframe):
    print(dataframe)

    return dataframe


"""
    Back-tracking algoirthm requires a check to see if the board is of a valid configuration.
    If it is return true if not, return false and continue the search.
"""


def is_valid(board):
    for row in board:
        if len(row) != len(set(row)):
            return False

    columns = []
    for i in range(len(board)):
        column = [row[i] for row in board]
        columns.append(column)

    for column in columns:
        if len(column) != len(set(column)):
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
    input_size = int(input("Size of board (n x n): "))
    board_setup = input("Input original board layout by row: ")
    board = setup(input_size, board_setup)              # Set up board with given input
    if is_valid(board):
        output(board, input_size)
        print("Game over.")
    else:
        dataframe = pd.DataFrame(np.array(board))           # Convert input into pandas dataframe for processing
        dataframe = solve(dataframe)                        # Call function to solve game and return the updated board
        updated_board = dataframe.to_numpy()                # Convert dataframe back to 2d numpy array
        output(updated_board, input_size)                   # Call the output function to show user the progress


main()

