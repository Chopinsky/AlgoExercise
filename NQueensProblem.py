#
# Problem: place queens in a chest board, such that no queen will be on the way of any others
#
from __future__ import print_function

BOARD_SIZE = 11

def printSolution(board):
    if board[0] == [0] * len(board):
        print("There is no solution to the board size: " + str(len(board)) + "x" + str(len(board)))
        return

    size = len(board)
    for i in range(size):
        for j in range(size):
            print("  " + str(board[i][j]) + "  ", end="")
        print()


def isSafeToPlay(board, queens, row, col):
    for i in range(len(queens)):
        if queens[i][0] == row or queens[i][1] == col:
            return False

        if abs(queens[i][0]-row) == abs(queens[i][1]-col):
            return False

    return True


def solveNQueens(board, queens, row):
    for col in range(len(board)):
        # Put queen down at (row, col)
        board[row][col] = 1
        done = False

        # Check if it's safe to place this queen here
        if isSafeToPlay(board, queens, row, col):
            if row == len(board) - 1:
                return True
            else:
                newSet = queens + [[row, col]]
                done = solveNQueens(board, newSet, row + 1)

        if done == True:
            # Bubble done event up.
            return True
        else:
            # Reset board to previous state, and continue with the next position.
            board[row][col] = 0

#board = numpy.zeros((BOARD_SIZE, BOARD_SIZE))
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
queens = []
solveNQueens(board, queens, 0)
printSolution(board)
