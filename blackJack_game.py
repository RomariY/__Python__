import random

suits = ('Heart', 'Dimonds', 'Spades', 'Clubs')
ranks = (
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace',
)
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.suit} of {self.rank}'


class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits: 
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

        print(len(self.all_cards))

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        deck_count = 0
        for i in self.all_cards:
            deck_count += 1
        return f"The deck has {deck_count}"

class Hand():
    def __init__(self, ):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.value += new_card.value
        if new_card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        

    def __str__(self):
        text = ""
        for card in self.cards:
            text += str(card) + '| '
        text += f"\nYour rank is: {self.value}"
        return text


class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):  
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chip):
    while True:
        try:
            chip.bet = int(input("Print your bet: "))
        except:
            raise "Not valid input"
        else:
            if chip.bet > chip.total:
                print(f"You don't gave enought chips. You have {chip.total}")
            else:
                break
            

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        inpt = input("Hit or Stand? (H or S)")
        if inpt.lower() == 'h':
            hit(deck,hand)
        elif inpt.lower() == 's':
            print("Player stands!\n Dealers turn")
            playing = False
        else:
            print("Sorry, enter the correct input!")
            continue
        break

def show_some(player,dealer):
    print(f"Player's cards\n{player}\n")
    print(f"Dealer's card\n{dealer.cards[1]}")
    
    
def show_all(player,dealer):
    print(f"Player's cards\n{player}\n")
    print(f"Dealer's card\n{dealer}")


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("WIN PLAYER!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("WIN PLAYER! DEALER BUST!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player, dealer ):
    print("Dealer and player tie! PUSH")

playing = True
while True:
    print("Welcome to BlackJack!")
    # Deck create&&shuffle
    deck = Deck()
    deck.shuffle_deck()

    player_one = Hand()
    player_one.add_card(deck.deal_one())
    player_one.add_card(deck.deal_one())
    print(player_one)


    dealer = Hand()
    dealer.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_one, dealer)

    while playing:
        hit_or_stand(deck, player_one)
        show_some(player_one, dealer)
        if player_one.value > 21:
            player_busts(player_one, dealer, player_chips)
            break
    if player_one.value <= 21:
        while dealer.value < 17:
            hit(deck, dealer)
        show_all(player_one, dealer)
        if dealer.value > 21:
            dealer_busts(player_one,dealer, player_chips)
        elif dealer.value > player_one.value:
            dealer_wins(player_one,dealer, player_chips)
        elif dealer.value < player_one.value:
            player_wins(player_one, dealer, player_chips)
        else:
            push(player_one, dealer)
    
    print(f"Total chips {player_chips.total}")

    new_game = input("Woud you like to play another hand? (y/n)\n")

    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break