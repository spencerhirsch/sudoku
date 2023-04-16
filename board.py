import random as rand

'''
    Function randomly generates game boards used to test our algorithms. This data is tracked for the output of the
    metrics of our program.
'''


def make_board():
    number_of_test = 1000
    for i in range(number_of_test):
        board_size = rand.randrange(10)
        board = []
        row = []
        for j in range(board_size):
            fill = rand.sample(range(board_size), board_size)
            fill_up = []
            for val in fill:
                fill_up.append(val + 1)

            board.append(fill_up)


        for row in board:
            remove = rand.randrange(board_size)
            indices = rand.sample(range(board_size), remove)

            for val in indices:
                row[val] = 0

        if len(board) > 3:
            board_string = ''
            for val in board:
                board_string += str(val)

            board_string = board_string.replace('[', '').replace(']', ', ').replace(' ', '')
            board_string = board_string[:-1]

            print(board_string)

make_board()
