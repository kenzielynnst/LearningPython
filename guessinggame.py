import random

def get_valid_number():
    """Keep asking till the dumbass user gives us an integer"""
    while True:
        guess = input("Enter your guess --> ")
        try:
            guess = int(guess)
            print("You guessed: ", guess)
            return guess
        except ValueError:
            print("You must enter a number in digits.")

maxnum = 1000
answer = random.randrange(1, maxnum, 1)
print(f"I have guessed a number between 1 and {maxnum}.\n")

while True:
    guess = get_valid_number()

    if guess > answer:
        print("Your guess is too high")
    if guess < answer:
        print("Your guess is too low")
    if guess == answer:
        print("You guessed correctly")
        break



