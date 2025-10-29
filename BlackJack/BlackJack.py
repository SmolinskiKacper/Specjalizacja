import random

def deal_card():
    deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck_of_cards)
    return card



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Push (remis)."
    elif dealer_score == 0:
        return "Dealer ma BLACKJACK. Przegrałeś."
    elif player_score == 0:
        return "Masz BLACKJACK! Wygrałeś!"
    elif player_score > 21:
        return "Przekroczyłeś 21, przegrałeś."
    elif dealer_score > 21:
        return "Dealer przekroczył 21, wygrałeś!"
    elif player_score > dealer_score:
        return "Masz więcej punktów, wygrałeś!"
    else:
        return "Dealer ma więcej punktów, przegrałeś."
def game():
    dealer_cards = []
    player1_cards = []
    dealer_score = -1
    player_score = -2
    is_game_over = False

    for _ in range(2):
        dealer_cards.append(deal_card())
        player1_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player1_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer card: {dealer_cards[0]}")
        print(f"Your cards: {player1_cards}, current score: {player_score}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            deal_card_player = input("Type 'h' for hit or 's' for stand\n").lower()
            if deal_card_player == "h":
                player1_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score <17 and dealer_score > 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player1_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play? type 'y' for yes or 'n' for no ") == "y":
    game()