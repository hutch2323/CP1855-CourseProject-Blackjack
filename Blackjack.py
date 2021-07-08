import card
import db

def displayTitle():
    # Display game title and the betting odds
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def main():

    # Variable used to control the loop of the game. Will only end when not "y"
    playAgain ="y"
    
    # While loop that controls whether or not the user would like to keep playing. Will run at least once.
    while(playAgain == "y"):
        displayTitle()

        # Variable to indicate whether or not the user's bet is valid
        isValidBet = True

        # Variables/lists used to hold the player/dealer's points and player/dealer's hands 
        playerPoints = 0
        dealerPoints = 0
        playerHand = []
        dealerHand = []
        
        # Assign the money from text file to money variable
        money = db.importFile()
        
        # Check to see if minimum balance is greater than 5
        if (db.checkForMinimumBalance(money) == True):
            # Update the money variable to reflect changes
            money = db.updateBalance()
            print("\n################################")
            print("Money 1: " + str(money))
            
            # Get user input for the bet
            betAmount = db.getUserBet(money)

            # Check to see if the bet is valid
            betAmount = db.validateBet(money, betAmount)
        else:
            # If the minimum balance is less than 5 and user doesn't add more money, end the game
            break


        # If the user places a valid bet:
        if (betAmount > 0):
            # Update the money again. The bet, if valid, is processed in validateBet()
            print("\n################################")
            print("Money 2: " + str(money))
            print("After Bet: " + str(db.updateBalance()))
            print("Original Bet Amount: " + str(betAmount))
            
            money = db.updateBalance()
            print("Updated Bet Amount: " + str(betAmount))
            print("################################")
            db.processBet(money, betAmount)
            money = db.updateBalance()           
        else:
            print()
            break

        # create the deck of 52 cards
        deckOfCards = card.createDeck()
        
        # For loop to handle the deal portion of the game. Card to user, then dealer, then user, then dealer
        for i in range(1, 5):
            # if the number in the range is even (2 or 4)
            if (i%2 == 0):
                # process a dealt card for the dealer
                user = "dealer"
                dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
            else: # if the number in the range is odd (1 or 3)
                # process a dealt card for the user/player
                user = "player"
                playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)

        # Show the dealer's show card. One is still hidden (2nd card face down)
        print("\nDEALER'S SHOW CARD:")
        print(dealerHand[0][1] + " of " + dealerHand[0][0])

        # Process the turn for the player. This will prompt user to hit/stand and return the number of points once user stands or busts
        user = "player"
        playerPoints = card.processTurn(playerHand, deckOfCards, user, playerPoints, dealerPoints)

        # Process the turn for the dealer. This will prompt dealer to hit/stand (until at least 17 points) and return the number of points once dealer stands or busts
        user = "dealer"
        dealerPoints = card.processTurn(dealerHand, deckOfCards, user, playerPoints, dealerPoints)
        
        # Display user and dealer's points
        print("\nYOUR POINTS:     " + str(playerPoints))
        print("DEALER'S POINTS: " + str(dealerPoints))

        print("\n################################")
        print("Money: " + str(money))
        print("Bet Amount: " + str(betAmount))
        print("################################")
        # Determine whether the player or dealer wins the game. This function can envoke the processWin() or processTie(), depending on the result
        card.determineResult(playerPoints, dealerPoints, money, betAmount)
        
        # Update the user's balance again to reflect any changes
        money = db.updateBalance()

        # Display user's balance
        print("Money: " + str(money))

        # Ask user whether or not they would like to play again
        playAgain = input("\nPlay again? (y/n): ")
        print()
        

    # Display "bye" messages to signify the end of the game
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
