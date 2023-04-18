"""
    Authors: Spencer Hirsch, Thomas Johnson
    Course: Introduction to Artificial Intelligence
    Professor: Dr. Mitra
    Project: Pseudo-Sudoku Intermediate Submission
"""

from board import make_board
import matplotlib.pyplot as plt
import time
import pprint
import random as rand

"""
    Process the input and validate data. Ensure that the given input
    is in the correct format and set up the board for processing.
"""


def setup(input_size, board_setup):
    board_list = board_setup.split(",")  # Break up input string
    board = []  # Initialize board
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
    for i in range(size):
        for j in range(size):
            if board[i][j] == "0":
                return i, j

    return -1, -1


"""
    Given the cordinates of an open cell, check if the number we are attempting to place
    will be a valid move. Iterate through row, and then column. Return false at any point
    if we find the move to be invalid, else return true
"""


def valid_move(cord1, cord2, board, size, num):
    # Check row for number
    for i in range(size):
        if board[i][cord2] == str(num):
            # print("Not valid: ", num)
            # print(i, cord2)
            return False

    # Check column for number
    for j in range(size):
        if board[cord1][j] == str(num):
            # print("Not valid: ", num)
            # print(cord1, j)
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
    start = time.time()
    nums = list(range(1, size + 1))  # list of all possible numbers
    cord1, cord2 = find_cell(board, size)
    # print("Checking cords: ", cord1, cord2)

    # Found solution
    if cord1 == -1 and cord2 == -1:
        end = time.time()
        total = end - start
        return True, total

    for num in nums:
        if valid_move(cord1, cord2, board, size, num):
            # print("Valid move: ", num)
            # print(cord1, cord2)

            board[cord1][cord2] = str(num)

            if solve(board, size):
                end = time.time()
                total = end - start
                return True, total

            board[cord1][cord2] = "0"

    end = time.time()
    total = end - start
    return False, total


"""
    Back-tracking algorithm requires a check to see if the board is of a valid configuration.
    If it is return true if not, return false and continue the search. Checks first that the row,
    doesn't contain any duplicate values and doesn't contain any empty data. Then it does do the
    same to columns.
"""


def is_valid(board):
    for row in board:
        if (
            len(row) != len(set(row)) or " " in row
        ):  # Convert list to set to check for duplicates
            return False

    columns = []
    for i in range(len(board)):
        column = [row[i] for row in board]
        columns.append(column)

    for column in columns:
        if len(column) != len(set(column)) or " " in column:
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
                print("| %s" % val, end="", sep="", flush=True)
            elif index != input_size - 1:
                print(" | %s" % val, end="", sep="", flush=True)
            else:
                print(" | %s |" % val)
            index += 1
    print("-" * (4 * input_size + 1))


def calculate(dict):
    number = len(dict[0]) / 30
    times = []
    removed = []
    for i in range(int(number)):
        time = sum(dict[0][:30]) / 30
        del dict[0][:30]
        remove = sum(dict[1][:30]) / 30
        del dict[1][:30]
        times.append(time)
        removed.append(remove)

    return times, removed


"""
    Function that handles plotting the scatter plots for the data. Once plots are constructed, they are saved to the 
    local directory. Parameters for the function are the dictionary that stores the values of the algorithm as well as
    the algorithm that is being plotted.  
"""


def plot(back_time_dict, algo):
    pprint.pprint(back_time_dict)

    for val in back_time_dict:
        x = back_time_dict[val][1]
        y = back_time_dict[val][0]
        plt.scatter(x, y, label=val)
    plt.legend()
    plt.xlabel("Number of Empty Squares")
    plt.ylabel("Computation Time (seconds)")
    plt.title("All points of %s Algorithm" % algo)

    plt.tight_layout()
    plt.savefig("scatter_%s" % algo)

    plt.clf()

    for val in back_time_dict:
        times, removed = calculate(back_time_dict[val])
        x = removed
        y = times
        plt.scatter(x, y, label=val)
    plt.legend()
    plt.xlabel("Number of Empty Squares")
    plt.ylabel("Computation Time (seconds)")
    plt.title("Average of all points of %s Algorithm" % algo)

    plt.tight_layout()
    plt.savefig("scatter_avg_%s" % algo)


"""
    Driver function that takes the input from the user. Calls all necessary
    function in order to ensure execution of the program.
"""


def main():
    values = [25, 50, 75, 100, 150, 200]
    number_of_test = 30
    back_time_dict = {}
    for val in values:  # Iterate values in array of sizes
        time_log_back = []
        removed = []
        important = []
        for num in range(15):
            remove = rand.randrange(val)
            for i in range(number_of_test):  # Test each value 30 times
                total_time = 0
                board_setup, input_size, remove = make_board(
                    val, remove
                )  # Take board data from function that generates boards
                board = setup(input_size, board_setup)  # Set up board with given input
                if is_valid(board):
                    output(board, input_size)
                    print("Game over.")
                else:
                    print("Original Board is: ")
                    output(board, input_size)
                    solved, total_time = solve(board, input_size)
                    if solved:
                        print("solved board is: ")
                        output(board, input_size)
                    else:
                        print("No solution")
                time_log_back.append(total_time)
                removed.append(remove * val)
        important.append(time_log_back)
        important.append(removed)
        back_time_dict[val * val] = important
    plot(back_time_dict, "Backtracking")
    # plot(new_algo_dict, "WHATEVER THE NEW ALGO IS")


main()
