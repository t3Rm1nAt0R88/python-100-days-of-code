import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))


if player_choice > 2 or player_choice < 0:
    print("You entered an invalid number. You Lose!")
else:
    print("You Chose: ")
    print(images[player_choice])
    print("Computer Chose: ")
    print(images[computer_choice])
    if computer_choice == player_choice:
        print("Draw")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif player_choice > computer_choice:
        print("You Win!")
    elif computer_choice > player_choice:
        print("You Lose!")
