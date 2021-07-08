import random
import db

"""
This module handles all the card related functions for the blackjack game.
"""

def createDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    pointValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
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
            while True:
                try:
                    aceChoice = int(input("\nYou were dealt an ace. 1 or 11?: "))
                except ValueError:
                    print("Invalid integer number. Try again!")
                    continue
                except Exception as e:
                    print("Unexpected error has occured!")
                    print(type(e), e)
                    db.exitProgram()
                if ((aceChoice == 1) or (aceChoice == 11)):
                    break
                else:
                    print("Invalid selection. Must choose 1 or 11!")
                    continue
                
            if (aceChoice == 1):
                card[2] = 1
            elif (aceChoice == 11):
                card[2] = 11

        elif (user == "dealer"):
            card[2] = 11
            
    elif (card[1] == "Ace") and (score > 10):
        card[2] = 1
            

def processCardDeal(hand, deckOfCards, user, points):
    dealtCard = dealCard(deckOfCards)
    checkForAce(dealtCard, user, points)
    points += dealtCard[2]
    hand.append(dealtCard)
    return points


def processTurn(hand, deck, user, playerPoints, dealerPoints):
    if (user == "player"):
        showHand(hand, user)
        hitOrStand = input("\nHit or stand? (hit/stand): ")

        #while loop to handle player's turn
        while (playerPoints <= 21) and (hitOrStand.lower() == "hit"):
            playerPoints = processCardDeal(hand, deck, user, playerPoints)
                
            showHand(hand, user)

            if (playerPoints >= 21):
                return playerPoints
                break

            hitOrStand = input("\nHit or stand? (hit/stand): ")

        return playerPoints

    elif (user == "dealer"):
        while((dealerPoints < 17) and (playerPoints <= 21)):
            dealerPoints = processCardDeal(hand, deck, user, dealerPoints)

        showHand(hand, user)
        return dealerPoints

def determineResult(playerPoints, dealerPoints, money, betAmount):
    if (playerPoints <=21):
            if((playerPoints > dealerPoints) or (dealerPoints > 21)):
                print("\nYou win.")
                money = db.processWin(money, betAmount)
            elif(playerPoints == dealerPoints):
                print("\nIt's a draw!")
                money = db.processTie(money, betAmount)
            elif (dealerPoints > playerPoints):
                print("\nSorry. You lose.")
    else:
        print("\nSorry. You lose.")

def showHand(hand, user):
    if(user == "player"):
        print("\nYOUR CARDS:")
    elif(user == "dealer"):
        print("\nDEALER'S CARDS:")

    for card in hand:
        print(card[1] + " of " + card[0])
