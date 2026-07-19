import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

# Number picked at random between 1 and 100
chosen_number = random.randint(1, 100)

# Chose Difficulty
def difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if mode == 'easy':
        return 10
    elif mode == 'hard':
        return 5
    else:
        print("Invalid Input. Chose again")
        difficulty()
        return None
number_of_lives = difficulty()

game_over = False
while not game_over:
    print(f"You have {number_of_lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    number_of_lives -= 1
    if guess == chosen_number:
        print(f"You got it! The answer is {chosen_number}.")
        game_over = True
    elif guess > chosen_number:
        print("Too high.\nGuess again.")
    elif guess < chosen_number:
        print("Too low.\nGuess again.")
    elif number_of_lives == 0:
        print("You've run out of guesses. Start Again")
        game_over = True
