import random


board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def print_board():
    for row in board:
        print(" | ".join(row))
    print("\n")

def get_player_move():
    move = input("Enter your move --> ")
    row,col = move.split(",")
    row=int(row)
    col=int(col)
    board[row][col] = "X"

def computer_move():
    row=random.randint(0,2)
    col=random.randint(0,2)
    board[row][col] = "O"

def player_won() -> bool:
    # Horizontal winning combos:
    winning_row = ["X", "X", "X"]
    for row in board:
        if row == winning_row:
            return True
    
    # Vertical winning combos:
    for col in range(3):
        if board[0][col] == "X" and board[1][col] == "X" and board[2][col] == "X":
            return True
    
    # Diagonal winning combos:
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return True

    return False
    

print("Welcome to tic tac toe.")

while True:
    get_player_move()
    print_board()
    computer_move()
    print_board()
    if player_won():
        print("You won!")
        break