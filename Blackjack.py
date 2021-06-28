import random
import db

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

def displayTitle():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def main():

    playAgain ="y"
    newBet = "y"
    addFunds = "y"
    
    while(playAgain == "y"):
        displayTitle()
        fileName = "money.txt"
        
        money = db.importFile(fileName)
        if (money < 5):
            addFunds = input("\nYour account currently has less than the required $5 to play. Would you like to add additional funds (y/n)?: ")
            if (addFunds.lower() == "y"):
                money = db.addMoney(money, fileName)
            else:
                break
            
        print("\nMoney: " + str(money))
        betAmount = float(input("Bet amount: "))

        while ((betAmount < 5) or (betAmount > 1000)):
            print("\nError, invalid bet amount. Please select an amount between 5 and 1000.")
            print("\nMoney: " + str(money))
            betAmount = float(input("Bet amount: "))

        while (betAmount > money):
            addFunds = input("\nError. Your account currently has less funds than the bet amount. Would you like to add additional funds (y/n)?: ")
            if (addFunds.lower() == "y"):
                money = db.addMoney(money, fileName)
            else:
                newBet = input("Would you like to make a different bet (y/n)?: ")
                if (newBet.lower() == "y"):
                    print("\nMoney: " + str(money))
                    betAmount = float(input("Bet amount: "))

                    while ((betAmount < 5) or (betAmount > 1000)):
                        print("Error, invalid bet amount. Please select an amount between 5 and 1000.")
                        print("\nMoney: " + str(money))
                        betAmount = float(input("Bet amount: "))
                else:
                    break

        if ((newBet.lower() != "y") and (addFunds.lower() != "y") and (betAmount > money)):
            break
        
        money = db.processBet(money, betAmount, fileName)
        
        deckOfCards = createDeck()

        playerPoints = 0
        dealerPoints = 0
        playerHand = []
        dealerHand = []

        user = "player"
        playerPoints = processCardDeal(playerHand, deckOfCards, user, playerPoints)
        
        user = "dealer"
        dealerPoints = processCardDeal(dealerHand, deckOfCards, user, dealerPoints)

        print("\nDEALER'S SHOW CARD:")
        print(dealerHand[0][1] + " of " + dealerHand[0][0])

        user = "player"
        playerPoints = processCardDeal(playerHand, deckOfCards, user, playerPoints)

        user = "dealer"
        dealerPoints = processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
        
        user = "player"
        showHand(playerHand, user)
        hitOrStand = input("\nHit or stand? (hit/stand): ")
        
        #while loop to handle player's turn
        while (playerPoints <= 21) and (hitOrStand.lower() == "hit"):
            playerPoints = processCardDeal(playerHand, deckOfCards, user, playerPoints)
                
            showHand(playerHand, user)

            if (playerPoints >= 21):
                break

            hitOrStand = input("\nHit or stand? (hit/stand): ")

        user = "dealer"
        while((dealerPoints <= 17) and (playerPoints <= 21)):
            dealerPoints = processCardDeal(dealerHand, deckOfCards, user, dealerPoints)


        showHand(dealerHand, user)
                
        print("\nYOUR POINTS:     " + str(playerPoints))
        print("DEALER'S POINTS: " + str(dealerPoints))

        if (playerPoints <=21):
            if((playerPoints > dealerPoints) or (dealerPoints > 21)):
                print("\nYou win.")
                money = db.processWin(money, betAmount, fileName)
            elif(playerPoints == dealerPoints):
                print("\nIt's a draw!")
                money = db.processTie(money, betAmount, fileName)
            elif (dealerPoints > playerPoints):
                print("\nSorry. You lose.")
        else:
            print("\nSorry. You lose.")

#        if (playerPoints <= 21) and (dealerPoints <= 21):
#            if (playerPoints > dealerPoints):
#                print("\nYou win.")
#                money = db.processWin(money, betAmount, fileName)
#            elif (playerPoints == dealerPoints):
#                print("\nIt's a draw.")
#            else:
#                print("\nYou lose.")
#        elif (playerPoints <= 21) and (dealerPoints > 21):
#            print("\nYou win.")
#            money = db.processWin(money, betAmount, fileName)
#        else:
#            print("\nYou lose.")

        print("Money: " + str(money))

        playAgain = input("\nPlay again? (y/n): ")
        print()
        
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
