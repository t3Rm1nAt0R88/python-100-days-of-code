import random
from art import logo, vs
from game_data import data

def compare_count(count_1, count_2):
    """Returns which has higher number of followers"""
    if count_1 > count_2 :
        return 'A'
    else:
        return 'B'

game_over = False
score = 0
A = random.choice(data)


while not game_over:
    print(logo)
    if score > 0:
        print(f"You're right! Current Score: {score}")
    
    B = random.choice(data)
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
    print(vs)
    print(f"Compare B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
    
    higher_count = compare_count(A["follower_count"], B["follower_count"])
    
    guess = input("Who has more followers? Type 'A' and 'B' ").upper()
    
    # Checking the guess againist the actual higher count
    if guess == higher_count:
        print('\n' * 20)
        A = B
        score += 1
    else:
        print('\n' * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_over = True
