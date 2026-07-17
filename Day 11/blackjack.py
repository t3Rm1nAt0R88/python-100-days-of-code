import random
from art import logo

def get_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def get_score(all_cards):
    """Takes a list of cards and Returns the sum of the cards or 0 if its a blackjack"""
    if sum(all_cards) == 21 and len(all_cards) == 2:
        return 0
    if 11 in all_cards and sum(all_cards) > 21:
        all_cards.remove(11)
        all_cards.append(1)
    return sum(all_cards)

def print_scores(card_player, card_computer):
    """Keeps printing user card and updated score along with computer's first card"""
    print(f"Your cards: {card_player}, current score: {get_score(card_player)}")
    print(f"Computer's first card: {card_computer[0]}")

def compare(score_player, score_computer):
    """Compares the score of player against the computer's score"""
    if score_player == score_computer:
        return "Draw! 🙃"
    elif score_computer == 0:
        return "Lose, opponent has BlackJack 😱"
    elif score_player == 0:
        return "Win with a BlackJack 😎"
    elif score_player > 21:
        return "You went over. You Lose 😭"
    elif score_computer > 21:
        return "Opponent went over. You Win 😁"
    elif score_player > score_computer:
        return "You Win 🙂"
    else:
        return "You Lose! 😤"


def play_blackjack():
    """Game Code"""
    print(logo)
    player_cards = []
    computer_cards = []
    # Deal 2 cards to both user and computer
    for _ in range(2):
        player_cards.append(get_card())
        computer_cards.append(get_card())
    print_scores(player_cards, computer_cards)

    # Checking if either has got blackjack or if the user has gone over 21
    if get_score(player_cards) == 0 or get_score(computer_cards) == 0 or get_score(player_cards) > 21:
        print(f"Your final hand: {player_cards}, final score: {get_score(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {get_score(computer_cards)}")
        print(compare(get_score(player_cards), get_score(computer_cards)))
    else:
        # Ask user for more cards
        while input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            player_cards.append(get_card())
            print_scores(player_cards, computer_cards)

            # Does not allow user to get another card if the sum of cards is already over 21
            if get_score(player_cards) > 21:
                break

        # Keep dealing cards to computer till his score is less than 17
        while get_score(computer_cards) < 17 and get_score(computer_cards) !=0 :
            computer_cards.append(get_card())

        # Final Showdown
        print(f"Your final hand: {player_cards}, final score: {get_score(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {get_score(computer_cards)}")
        print(compare(get_score(player_cards), get_score(computer_cards)))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 25)
    play_blackjack()