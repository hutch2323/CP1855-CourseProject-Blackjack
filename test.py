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

def main():

    playAgain ="y"
    
    while(playAgain == "y"):
        deckOfCards = createDeck()

        print("Cards in a deck:")

        #for card in deckOfCards:
        #    print(card[1] + " of " + card[0] + ". Value of: " + str(card[2]) + ".")

        print("\nThere are " + str(len(deckOfCards)) + " cards in the deck.")

        turnCounter = 1

        points = 0
        dealtHand = []
        dealerHand = []
        hitOrStand = "hit"

        
        
        while (points <= 21) and (hitOrStand.lower() == "hit"):
            dealtCard = dealCard(deckOfCards)

            if (dealtCard[1] == "Ace"):
                aceChoice = int(input("\nYou were dealt an ace. 1 or 11?: "))
                if (aceChoice == 1):
                    dealtCard[2] = 1
                elif (aceChoice == 11):
                    dealtCard[2] = 11

            dealtHand.append(dealtCard)
                
            print("\nYour Hand:")
            points = 0
            #print("\nThere are " + str(len(deckOfCards)) + " cards in the deck.")
            for card in dealtHand:
                #print(card[1] + " of " + card[0] + ". Value of: " + str(card[2]) + ".")
                print(card[1] + " of " + card[0])
                points += card[2]

            print("\nYour points: " + str(points))
            turnCounter += 1
            if (points >= 21):
                break


            hitOrStand = input("Hit or stand? (hit/stand): ")
                
        if (points <= 21):
            print("\nYou win.")
        else:
            print("\nYou lose.")

        playAgain = input("\nPlay again? (y/n): ")
    

if __name__ == "__main__":
    main()
