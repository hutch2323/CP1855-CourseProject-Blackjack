import random
import db

"""
This module handles all the card related functions for the blackjack game.
"""

# Function used to create a deck of cards. Will return the deck (list of list)
def createDeck():
    # Lists used to hold the suits, ranks, and pointValues for each card
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    pointValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = []

    # For loop that will take the suits, ranks and pointValues lists and create a deck of cards
    for i in range(len(ranks)):
        for j in range(len(suits)):
            card = [suits[j], ranks[i], pointValues[i]]
            deck.append(card)
    return deck


# Function that checks whether or not the deck should be reshuffled. If the current deck length is less than half (<26) the original (52), reshuffle before next hand
def checkForReshuffle(deck):
    # If the number of cards currently in the deck is less than 26, reshuffle (recreate the deck)
    if (len(deck) < 26):
        deck = createDeck()
        print("\n***Deck has been reshuffled***")
    return deck


# This function will randomly grab a card from the deck, remove that card from the deck, then return that card
def dealCard(deck):
    cardToDeal = random.choice(deck)
    deck.remove(cardToDeal)
    return cardToDeal


# This function will check the value of each card and determine whether or not it is an Ace
def checkForAce(card, user, score):
    # If the card is an Ace and the current score (before the ace) is <= 10
    if (card[1] == "Ace") and (score <= 10):
        # If the user is the player, give them an option to choose between 1 and 11 for the value of the Ace
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

            # If the user chooses 1, assign the value of 1 for the pointValue of the card. Otherwise, if they 11, assign the value of 11  
            if (aceChoice == 1):
                card[2] = 1
            elif (aceChoice == 11):
                card[2] = 11

        # If the user is the dealer and the current score is <= 10, automatically assign the value of 11 to the Ace
        elif (user == "dealer"):
            card[2] = 11

    # If the card is an ace        
    elif (card[1] == "Ace") and (score > 10):
        card[2] = 1
        
            
# This function will process each card that the dealer deals. It will get the card, check to see if it's an ace, add the points to the user/dealer's total,
# append the card to the user/dealer's hand, then return their point total. It takes the user/dealer's hand, the deck of card, the user (player or dealer)
# their point total as parameters
def processCardDeal(hand, deckOfCards, user, points):
    dealtCard = dealCard(deckOfCards)
    checkForAce(dealtCard, user, points)
    points += dealtCard[2]
    hand.append(dealtCard)
    return points

            
# This function will automate the "turn" or "round", which occurs after the orignal deal is handled
def processTurn(hand, deck, user, playerPoints, dealerPoints):
    if (user == "player"):
        # Show player's hand
        showHand(hand, user)
        # Ask player if they would like to hit (add more cards) or stand (no more cards)
        hitOrStand = input("\nHit or stand? (hit/stand): ")

        #while loop to handle player's turn. Will continue until the player's score is <= 21 or the player "hits" for more cards
        while (playerPoints <= 21) and (hitOrStand.lower() == "hit"):
            # Deal one card to the player
            playerPoints = processCardDeal(hand, deck, user, playerPoints)
                
            showHand(hand, user)

            # If the player's points is >= 21, end the loop and return the player's points
            if (playerPoints >= 21):
                return playerPoints

            hitOrStand = input("\nHit or stand? (hit/stand): ")

        return playerPoints
    

    elif (user == "dealer"):
        # Loop to control Dealer's turn. Will continue until the dealer's points are at least 17 and while the playersPoints are <= 21
        while((dealerPoints < 17) and (playerPoints <= 21)):
            # Deal card to the dealer and get the updated total points
            dealerPoints = processCardDeal(hand, deck, user, dealerPoints)

        #show the dealer's hand
        showHand(hand, user)

        # return dealerPoints
        return dealerPoints
    

# Function to determine who wins the game, or if it is a tie
def determineResult(playerPoints, dealerPoints, money, betAmount):
    # If the player hasn't busted
    if (playerPoints <=21):
            # If the player's points are greater than the dealer's points or the dealer has busted, player wins
            if((playerPoints > dealerPoints) or (dealerPoints > 21)):
                print("\nYou win.")
                # update the account balance (money) by calling the processWin function from db.py
                money = db.processWin(money, betAmount)
            elif(playerPoints == dealerPoints):
                print("\nIt's a draw!")
                # update the account balance (money) by calling the processTie function from db.py
                money = db.processTie(money, betAmount)
            elif (dealerPoints > playerPoints):
                # if dealer has more points and neither has busted, player loses
                print("\nSorry. You lose.")
    else: #If player has busted or the dealerPoints are greater than the player's points, player loses
        print("\nSorry. You lose.")

    return money


# This function will reveal all cards in the hand for the player and dealer
def showHand(hand, user):
    # If the user is player, display title of "Your Cards"
    if(user == "player"):
        print("\nYOUR CARDS:")
    # If the user is dealer, display title of "Dealer's Cards"
    elif(user == "dealer"):
        print("\nDEALER'S CARDS:")

    # Output every card in the hand for the given user (player/dealer)
    for card in hand:
        print(card[1] + " of " + card[0])
