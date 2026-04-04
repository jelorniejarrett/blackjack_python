import random

def create_deck():
    deck = []

    # cards 2-10 repeated 4 times
    for i in range(2, 11):
        deck.extend([i] * 4)

    # face cards(J Q K) with a value of 10 (4 each)
    deck.extend([10] * 12)   

    # aces
    deck.extend([11] * 4)

    return deck


def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def hand_value(hand):
    return sum(hand)


def play_blackjack():

    deck = create_deck()

    player = []
    dealer = []

    # initial cards
    player.append(draw_card(deck))
    player.append(draw_card(deck))

    dealer.append(draw_card(deck))
    dealer.append(draw_card(deck))

    print("\n--- Blackjack ---")

    # player turn
    while True:

        print("Your hand:", player, "Total:", hand_value(player))
        print("Dealer shows:", dealer[0])

        if hand_value(player) > 21:
            print("Bust! You lose.")
            return

        choice = input("Hit or Stand (h/s): ").lower()

        if choice == "h":
            player.append(draw_card(deck))
        else:
            break

    # dealer turn
    while hand_value(dealer) < 17:
        dealer.append(draw_card(deck))

    print("\nDealer hand:", dealer, "Total:", hand_value(dealer))
    print("Your hand:", player, "Total:", hand_value(player))

    # determine winner
    if hand_value(dealer) > 21:
        print("Dealer busts! You win!")

    elif hand_value(player) > hand_value(dealer):
        print("You win!")

    elif hand_value(player) < hand_value(dealer):
        print("Dealer wins.")

    else:
        print("Push (tie).")


# game loop
while True:

    play_blackjack()

    again = input("\nPlay again? (y/n): ")

    if again.lower() != "y":
        break