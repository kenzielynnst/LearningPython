board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def print_board():
    for row in board:
        print(" | ".join(row))

print_board()

print("Welcome to tic tac toe.")
move = input("Enter your move --> ")
row,col = move.split(",")
row=int(row)
col=int(col)
board[row][col] = "X"

print_board()