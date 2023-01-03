import sys

def is_valid(board, row, col):
    # Check if the placement of the queen at (row, col) is valid
    # by checking if there is another queen in the same row or column
    for i in range(len(board)):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check if there is another queen in the same diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < len(board) and j < len(board):
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def nqueens(board, col):
    # Base case: if all queens have been placed, print the solution
    if col >= len(board):
        print_board(board)
        return

    # Try placing the queen in each row of the current column
    for i in range(len(board)):
        if is_valid(board, i, col):
            # Place the queen and move on to the next column
            board[i][col] = 1
            nqueens(board, col + 1)
            # Backtrack: remove the queen from the current position and try again
            board[i][col] = 0

def print_board(board):
    # Print the solution in the required format
    for row in board:
        print(" ".join(str(x) for x in row))

def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check that the input is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check that N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with all positions empty
    board = [[0 for _ in range(N)] for _ in range(N)]
    nqueens(board, 0)

if __name__ == "__main__":
    main()
