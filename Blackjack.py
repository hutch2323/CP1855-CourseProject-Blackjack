import card
import db

def displayTitle():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def main():

    playAgain ="y"
    newBet = "y"
    addFunds = "y"
    isValidBet = True
    
    while(playAgain == "y"):
        displayTitle()
        
        money = db.importFile()
        if (money < 5):
            addFunds = input("\nYour account currently has less than the required $5 to play. Would you like to add additional funds (y/n)?: ")
            if (addFunds.lower() == "y"):
                money = db.addMoney(money)
            else:
                break
            
        print("\nMoney: " + str(money))
        betAmount = float(input("Bet amount: "))

        isValidBet = db.validateBet(money, betAmount)

        if (isValidBet == False):
            print()
            break
        else:
            money = db.refreshFunds()
        
        money = db.processBet(money, betAmount)
        
        deckOfCards = card.createDeck()

        playerPoints = 0
        dealerPoints = 0
        playerHand = []
        dealerHand = []

        user = "player"
        playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)
        
        user = "dealer"
        dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)

        print("\nDEALER'S SHOW CARD:")
        print(dealerHand[0][1] + " of " + dealerHand[0][0])

        user = "player"
        playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)

        user = "dealer"
        dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
        
        user = "player"
        card.showHand(playerHand, user)
        hitOrStand = input("\nHit or stand? (hit/stand): ")
        
        #while loop to handle player's turn
        while (playerPoints <= 21) and (hitOrStand.lower() == "hit"):
            playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)
                
            card.showHand(playerHand, user)

            if (playerPoints >= 21):
                break

            hitOrStand = input("\nHit or stand? (hit/stand): ")

        user = "dealer"
        while((dealerPoints <= 17) and (playerPoints <= 21)):
            dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)


        card.showHand(dealerHand, user)
                
        print("\nYOUR POINTS:     " + str(playerPoints))
        print("DEALER'S POINTS: " + str(dealerPoints))

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

        print("Money: " + str(money))

        playAgain = input("\nPlay again? (y/n): ")
        print()
        
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
