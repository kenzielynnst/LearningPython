board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def print_board():
    for row in board:
        print(" | ".join(row))

def get_player_move():
    move = input("Enter your move --> ")
    row,col = move.split(",")
    row=int(row)
    col=int(col)
    board[row][col] = "X"

print("Welcome to tic tac toe.")

while True:
    get_player_move()
    print_board()