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


def player_won() -> bool:
    winning_row = ["X", "X", "X"]
    if board[0] == winning_row:
        return True
    if board[1] == winning_row:
        return True
    if board[2] == winning_row:
        return True
        
    return False
    

print("Welcome to tic tac toe.")

while True:
    get_player_move()
    print_board()
    if player_won():
        print("You won!")
        break