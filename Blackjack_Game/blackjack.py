import random

suits = ('Hearts', 'Diamond', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))

        self.shuffle()

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def pick_a_card(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10

class Chip():
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

def take_a_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips you wanna bet?"))
        except:
            print("Sorry we only accept integer")
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips to place this bet")
                print("Your chips left : {}".format(chips.total))
            else:
                print("Your bet is placed successfully")
                break

def hit(deck, hand):
    single_card = deck.pick_a_card()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand (H/S)?")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands now dealer's turn..")
            playing = False
        else:
            print("Please enter 'H' for Hit or 'S' for Stand")
            continue
        break

def show_some(player_hand, dealer_hand):
    print("Player Cards Value:{}\nCards:".format(player_hand.value))
    for cards in player_hand.card:
        print(cards)
    print()
    print("Dealer Cards:")
    print(dealer_hand.card[0])
    print("One card hidden")
    print()

def show_all(player_hand, dealer_hand):
    print("Player Cards Value:{}\nCards:".format(player_hand.value))
    for cards in player_hand.card:
        print(cards)
    print()

    print("Dealer Cards:{}\nCards:".format(dealer_hand.value))
    for cards in dealer_hand.card:
        print(cards)
    print()

def push(player_hand, dealer_hand):
    print("PUSH.... its a tie")
def player_wins(player, dealer, chips):
    print("Congo! you win")
    chips.win_bet()
def dealer_wins(player, dealer, chips):
    print("Oops, you lost....")
    chips.lose_bet()
def player_busts(player, dealer, chips):
    print("You Bust")
    chips.lose_bet()
def dealer_busts(player, dealer, chips):
    print("Dealer Busts")
    chips.win_bet()

while True:

    print("welcome to blackjack")
    deck = Deck()
    player_hand = Hand()
    player_hand.add_card(deck.pick_a_card())
    player_hand.add_card(deck.pick_a_card())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.pick_a_card())
    dealer_hand.add_card(deck.pick_a_card())

    chip_value = int(input("How many chips you wanna purchase?"))
    player_chips = Chip(chip_value)

    take_a_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break;
    if(player_hand.value <= 21):
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    print("Total chips : {}".format(player_chips.total))
    new_game = input("New Game?")
    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break
