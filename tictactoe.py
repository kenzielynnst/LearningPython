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
    while board[row][col] == "O" or board[row][col] == "X":
        move = input("Enter your move --> ")
        row,col = move.split(",")
        row=int(row)
        col=int(col)
    board[row][col] = "X"

def computer_move():
    row=random.randint(0,2)
    col=random.randint(0,2)
    while board[row][col] == "O" or board[row][col] == "X":
        row=random.randint(0,2)
        col=random.randint(0,2)
    board[row][col] = "O"

def someone_won(letter) -> bool:  
    # Horizontal winning combos:
    winning_row = [letter, letter, letter]
    for row in board:
        if row == winning_row:
            return True   
    # Vertical winning combos:
    for col in range(3):
        if board[0][col] == letter and board[1][col] == letter and board[2][col] == letter:
            return True   
    # Diagonal winning combos:
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return True
    if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        return True
    return False
    

print("Welcome to tic tac toe.")

while True:
    get_player_move()
    print_board()
    if someone_won("X"):
        print("You won!")
        break
    computer_move()
    print_board()
    if someone_won("O"):
        print("The computer won. You lose.")
        break
