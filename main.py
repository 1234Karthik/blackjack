import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    r_card = random.choice(cards)
    return r_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):

    if player_score == computer_score:
        return "Its a draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(art.logo)

    player_cards = []
    computer_cards = []
    is_Playing = True

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())


    while is_Playing:

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {player_cards}, current score = {player_score}")
        print(f"Computers first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_Playing = False
        else:
            hit_play = input("Do u wanna pick a card or pass? y or n: ")
            if hit_play == "y":
                player_cards.append(deal_card())
            else:
                is_Playing = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_score)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play another game of blackjack? Type 'yes' or 'no': ") == 'yes':
    # clear()
    play_game()
