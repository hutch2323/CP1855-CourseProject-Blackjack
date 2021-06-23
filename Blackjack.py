import random

def createDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    pointValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = []

    cardCounter = 0
    for i in range(len(ranks)):
        for j in range(len(suits)):
            card = [suits[j], ranks[i], pointValues[i]]
            deck.append(card)
            #deck[cardCounter][0] = suits[j]
            #deck[cardCounter][1] = ranks[i]
            #deck[cardCounter][2] = pointValues[i]
            cardCounter += 1
    return deck


def dealCard(deck):
    cardToDeal = random.choice(deck)
    deck.remove(cardToDeal)
    return cardToDeal


def checkForAce(card, user, score):
    if (dealtCard[1] == "Ace") and (score <= 10):
        if (user == "player"):
            aceChoice = int(input("\nYou were dealt an ace. 1 or 11?: "))
            if (aceChoice == 1):
                dealtCard[2] = 1
            elif (aceChoice == 11):
                dealtCard[2] = 11
        elif (user == "dealer"):
            card[2] = 11

def main():

    playAgain ="y"
    
    while(playAgain == "y"):
        deckOfCards = createDeck()

        print("Cards in a deck:")

        #for card in deckOfCards:
        #    print(card[1] + " of " + card[0] + ". Value of: " + str(card[2]) + ".")

        print("\nThere are " + str(len(deckOfCards)) + " cards in the deck.")

        turnCounter = 1

        playerPoints = 0
        dealerPoints = 0
        playerHand = []
        dealerHand = []
        user = "dealer"
        hitOrStand = "hit"

        dealtCard = dealCard(deckOfCards)

        checkForAce(dealtCard, user, dealerPoints)

        dealerPoints += dealtCard[2]

        dealerHand.append(dealtCard)

        print("DEALER's SHOW CARD:")
        print(dealtCard[1] + " of " + dealtCard[0])
        
        user = "player"
        while (playerPoints <= 21) and (hitOrStand.lower() == "hit"):
            dealtCard = dealCard(deckOfCards)

            #check for ace
            checkForAce(dealtCard, user, userPoints)

            playerHand.append(dealtCard)
                
            print("\nYour Hand:")
            playerPoints += dealtCard[2]
            #print("\nThere are " + str(len(deckOfCards)) + " cards in the deck.")
            for card in playerHand:
                #print(card[1] + " of " + card[0] + ". Value of: " + str(card[2]) + ".")
                print(card[1] + " of " + card[0])

            print("\nYour points: " + str(points))
            turnCounter += 1
            if (playerPoints >= 21):
                break


            hitOrStand = input("Hit or stand? (hit/stand): ")
                
        if (playerPoints <= 21):
            if (playerPoints > dealerPoints):
                print("\nYou win.")
            elif (playerPoints = dealerPoints):
                print("\nIt's a draw.")
            else:
                print("\nYou lose.")
        else:
            print("\nYou lose.")

        playAgain = input("\nPlay again? (y/n): ")
    

if __name__ == "__main__":
    main()
