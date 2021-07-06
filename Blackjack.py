import card
import db

def displayTitle():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def main():

    playAgain ="y"
    isValidBet = True
    playerPoints = 0
    dealerPoints = 0
    playerHand = []
    dealerHand = []
    
    while(playAgain == "y"):
        displayTitle()
        
        money = db.importFile()
        
        if (db.checkForMinimumBalance(money) == True):
            money = db.updateBalance()
            while True:
                print("\nMoney: " + str(money))
                try:
                    betAmount = float(input("Bet amount: "))
                except ValueError:
                    print("Invalid number. Please try again!")
                    continue
                except Exception as e:
                    print("Unexpected error has occured!")
                    print(type(e), e)
                    db.exitProgram()
                break
            isValidBet = db.validateBet(money, betAmount)
        else:
            break    


        if (isValidBet == True):
            money = db.updateBalance()
        else:
            print()
            break
        
        deckOfCards = card.createDeck()

        for i in range(1, 5):
            if (i%2 == 0):
                user = "dealer"
                dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
            else:
                user = "player"
                playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)

        #user = "player"
        #playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)
        
        #user = "dealer"
        #dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)

        print("\nDEALER'S SHOW CARD:")
        print(dealerHand[0][1] + " of " + dealerHand[0][0])

        #user = "player"
        #playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)

        #user = "dealer"
        #dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
        
##        user = "player"
##        card.showHand(playerHand, user)
##        hitOrStand = input("\nHit or stand? (hit/stand): ")
##        
##        #while loop to handle player's turn
##        while (playerPoints <= 21) and (hitOrStand.lower() == "hit"):
##            playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)
##                
##            card.showHand(playerHand, user)
##
##            if (playerPoints >= 21):
##                break
##
##            hitOrStand = input("\nHit or stand? (hit/stand): ")
##
##        user = "dealer"
##        while((dealerPoints <= 17) and (playerPoints <= 21)):
##            dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
##
##
##        card.showHand(dealerHand, user)

        user = "player"
        playerPoints = card.processTurn(playerHand, deckOfCards, user, playerPoints, dealerPoints)

        user = "dealer"
        dealerPoints = card.processTurn(dealerHand, deckOfCards, user, playerPoints, dealerPoints)
        
        print("\nYOUR POINTS:     " + str(playerPoints))
        print("DEALER'S POINTS: " + str(dealerPoints))

##        if (playerPoints <=21):
##            if((playerPoints > dealerPoints) or (dealerPoints > 21)):
##                print("\nYou win.")
##                money = db.processWin(money, betAmount)
##            elif(playerPoints == dealerPoints):
##                print("\nIt's a draw!")
##                money = db.processTie(money, betAmount)
##            elif (dealerPoints > playerPoints):
##                print("\nSorry. You lose.")
##        else:
##            print("\nSorry. You lose.")

        card.determineResult(playerPoints, dealerPoints, money, betAmount)

        money = db.updateBalance()

        print("Money: " + str(money))

        playAgain = input("\nPlay again? (y/n): ")
        print()
        
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
