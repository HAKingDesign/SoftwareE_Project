import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def CreateDeck():
    suits = ['heart', 'diamonds', 'spades', 'clubs']
    
    #values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    #if we want cards to say jack queen king and ace we can use values like we did suits

    deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
    random.shuffle(deck)

    #print deck to see if it works
    for i in range(52):
        print(deck[i].value, deck[i].suit)


    #simulates dealing a hand for blackjack
    deal = input("Would you like a hand (1 for yes)?: ")
    deal = int(deal)
    pos = 0

    while (deal == 1):
        pos = DealCards(deck, pos)
        
        deal = input("Would you like another hand (1 for yes)?: ")
        deal = int(deal)
        
#deals 2 cards at a time returns pos to keep track of position in deck
def DealCards(deck, pos):
    print("Dealing cards: \n")

    print(deck[pos].value, deck[pos].suit , ' ', deck[pos+1].value, deck[pos+1].suit)

    return (pos+2)


CreateDeck()