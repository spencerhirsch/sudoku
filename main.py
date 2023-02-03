"""
    Authors: Spencer Hirsch, Thomas Johnson
    Course: Introduction to Artificial Intelligence
    Professor: Dr. Mitra
    Project: Pseudo-Sudoku Intermediate Submission
"""

import pandas as pd


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
    board = setup(input_size, board_setup)
    output(board, input_size)


main()

