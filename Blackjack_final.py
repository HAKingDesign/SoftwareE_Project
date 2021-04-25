import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

balance = 100

def main():
    choice = 'y'
    while choice == 'y':
        playGame()
        if balance <= 0:
            print("You ran out of money, Game over.")
            choice = 'n'
        else:
            choice = input("\nPlay again?(y)")
            

#creates a list where each card as a suit and a value
def CreateDeck():
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace(Eleven)']

    deck = [Card(value, suit) for value in values for suit in suits]

    random.shuffle(deck)

    return deck
        
#fuction that controls the game
def playGame():
    print("=================NEW GAME=================")
    global balance

    print("Current Balance:", balance)
    #get a deck from createDeck
    deck = CreateDeck()

    #pop 2 cards from the deck to the players hand and dealers hand
    hand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]

    print("\nDealers hand:" ,dealerHand[0].value ,dealerHand[0].suit , "Hidden")
    print("Your hand:" ,hand[0].value ,hand[0].suit ,hand[1].value ,hand[1].suit)
    
    #since i used strings for the values i needed a function to convert them to the proper integer value
    card1 = getValue(hand[0].value)
    card2 = getValue(hand[1].value)
    dealerCard1 = getValue(dealerHand[0].value)
    dealerCard2 = getValue(dealerHand[1].value)

    total = card1 + card2
    print("Total value =", total)

    #allow user to bet
    print("Enter Bet Amount:", end = '')
    bet = int(getBet())
    
    if bet > balance:
        bet = balance
    print("Bet ammount:", bet)

    #the player can keep hitting until the value of there hand is < 21
    while total < 21:
        print("(1) to Stand\n(2) to hit\n", end = '')
        choice = getChoice()
        
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
                print(hand[i].value, hand[i].suit, end = ' ')
            print("\nTotal value =", total)
        else:
            print("You stood with:", total)
            break
    
    Bust = False
    BlackJack = False
    #if the total is > 21 then the player busts
    if total > 21:
        print("Sorry you busted")
        Bust = True
        balance = balance - bet
    #if total is 21 then they got a blackjack
    if total == 21:
        print("BLACKJACK, CONGRATULATIONS!")
        BlackJack = True
        balance = balance + bet

    if Bust == False and BlackJack == False:
        #reveals the dealers second card
        print("\nDealers hand:" ,dealerHand[0].value ,dealerHand[0].suit , dealerHand[1].value ,dealerHand[1].suit)
        dealerTotal = dealerCard1 + dealerCard2
        print("Dealer total:", dealerTotal)
        
        #dealer keeps getting cards until his had is >= 16
        while dealerTotal < 16:
            newCard = deck.pop()
            dealerHand.append(newCard)

            print("\nDealers hand:") 
            for i in range(len(dealerHand)):
                print(dealerHand[i].value, dealerHand[i].suit, end = ' ')

            newCardValue = getValue(newCard.value)
            dealerTotal = dealerTotal + newCardValue

            print("\nDealer Total:", dealerTotal)

        if dealerTotal > 21:
            print("Dealer Bust, You win!")
            balance = balance + bet
        elif dealerTotal > total:
            print("You lose")
            balance = balance - bet
        elif dealerTotal < total:
            print("You win!")
            balance = balance + bet
        else:
            print("Push")

    print("New balance:", balance)
        
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

#need this to test input
def getBet():
    return input()
def getChoice():
    return input()

main()
