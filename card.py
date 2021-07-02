import random

def createDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    pointValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = []

    cardCounter = 0
    for i in range(len(ranks)):
        for j in range(len(suits)):
            card = [suits[j], ranks[i], pointValues[i]]
            deck.append(card)
            cardCounter += 1
    return deck


def dealCard(deck):
    cardToDeal = random.choice(deck)
    deck.remove(cardToDeal)
    return cardToDeal


def checkForAce(card, user, score):
    if (card[1] == "Ace") and (score <= 10):
        if (user == "player"):
            aceChoice = int(input("\nYou were dealt an ace. 1 or 11?: "))
            if (aceChoice == 1):
                card[2] = 1
            elif (aceChoice == 11):
                card[2] = 11
        elif (user == "dealer"):
            card[2] = 11
            

def processCardDeal(hand, deckOfCards, user, points):
    dealtCard = dealCard(deckOfCards)
    checkForAce(dealtCard, user, points)
    points += dealtCard[2]
    hand.append(dealtCard)
    return points


def showHand(hand, user):
    if(user == "player"):
        print("\nYOUR CARDS")
    elif(user == "dealer"):
        print("\nDEALER'S CARDS")

    for card in hand:
        print(card[1] + " of " + card[0])
