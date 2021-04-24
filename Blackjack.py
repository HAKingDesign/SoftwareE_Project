import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def main():
    choice = 'y'
    while choice == 'y':
        playGame()
        choice = input("Play again?(y)" )


#creates a list where each card as a suit and a value
def CreateDeck():
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace(Eleven)']

    deck = [Card(value, suit) for value in values for suit in suits]
    #shuffle the list and return it
    random.shuffle(deck)

    return deck
        
#fuction that controls the game
def playGame():
    #get a deck from createDeck
    deck = CreateDeck()

    #pop 2 cards from the deck to the players hand
    hand = [deck.pop(), deck.pop()]

    print("Your hand:" ,hand[0].value ,hand[0].suit ,hand[1].value ,hand[1].suit)
    
    #since i used strings for the values i needed a function to convert them to the proper integer value
    card1 = getValue(hand[0].value)
    card2 = getValue(hand[1].value)

    total = card1 + card2
    print("Total value =", total)

    #the player can keep hitting until the value of there hand is >= 21
    while total <= 21:
        print("(1) to Stand\n(2) to hit")
        choice = input()
        
        #if they hit pop another card and append it to the players hand
        if int(choice) == 2:
            newCard = deck.pop()
            hand.append(newCard)
            newCardValue = getValue(newCard.value)
            total = total + newCardValue
            #ace case: to check if an ace needs to be changed to its one point value
            if total > 21:
                total=0
                ln=len(hand)
                for i in range(ln):
                    if hand[i].value=='Ace(Eleven)':
                        hand[i].value='Ace(One)' 
                for j in range(ln):
                    total=total + getValue(hand[j].value)
            print("Your new hand:") 
            for i in range(len(hand)):
                print(hand[i].value, hand[i].suit)
            print("Total value =", total)
            
            #again need to get the cards real value to add it to the total

        #if the player doesnt enter 2 then they stand 
        #   standing is useless without a dealer so we can add the dealer next time
        else:
            print("You stood with", total)
            break
        
        #if the total is > 21 then the player busts
        if total > 21:    
            print("Sorry you busted")
        #if total is 21 then they got a blackjack
        if total == 21:
            print("BLACKJACK, CONGRATULATIONS!")
            break

#the function to get the true value of the card
def getValue(card):
    if card == "Jack":
        value = 10
    elif card == "Queen":
        value = 10
    elif card == "King":
        value = 10
    elif card == "Ace(Eleven)":
        value = 11
    elif card == "Ace(One)":
        value = 1
    else:
        value = int(card)

    return value
main()