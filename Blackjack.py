# CP1855 - Course Project
# Marcus Hutchings - 20048535
# July 14, 2021

import card
import db

def playBlackjack(deckOfCards, money, betAmount):
    # Variables/lists used to hold the player/dealer's points and player/dealer's hands 
    playerPoints = 0
    dealerPoints = 0
    playerHand = []
    dealerHand = []
    
    # For loop to handle the deal portion of the game. Card to user, then dealer, then user, then dealer
    for i in range(1, 5):
        # if the number in the range is even (2 or 4)
        if (i%2 == 0):
            # process a dealt card for the dealer
            user = "dealer"
            dealerPoints = card.processCardDeal(dealerHand, deckOfCards, user, dealerPoints)
            # The dealer's first card (After dealing one to user/player)
            if (i == 2):
                # Show the dealer's show card. Next card hidden (2nd card face down)
                print("\nDEALER'S SHOW CARD:")
                print(dealerHand[0][1] + " of " + dealerHand[0][0])
        else: # if the number in the range is odd (1 or 3)
            # process a dealt card for the user/player
            user = "player"
            playerPoints = card.processCardDeal(playerHand, deckOfCards, user, playerPoints)

    # Process the turn for the player. This will prompt user to hit/stand and return the number of points once user stands or busts
    user = "player"
    playerPoints = card.processTurn(playerHand, deckOfCards, user, playerPoints, dealerPoints)

    # Process the turn for the dealer. This will prompt dealer to hit/stand (until at least 17 points) and return the number of points once dealer stands or busts
    user = "dealer"
    dealerPoints = card.processTurn(dealerHand, deckOfCards, user, playerPoints, dealerPoints)
    
    # Display user and dealer's points
    print("\nYOUR POINTS:     " + str(playerPoints))
    print("DEALER'S POINTS: " + str(dealerPoints))

    # Determine whether the player or dealer wins the game. This function can envoke the processWin() or processTie(), depending on the result
    money = card.determineResult(playerPoints, dealerPoints, money, betAmount)

    # Display user's balance
    print("Money: " + str(money))


# Function used to get/validate/process the user's bet. Will return a betAmount of zero if the bet is invalid, which will end the game in main    
def userBet(money):
    # Tuple used to hold a validation value (whether or not minimum balance is achieved - 0 for < minimum, 1 for >= minimum)
    # and the updated balance (if funds added - otherwise, just returns same money value)
    validatedBalanceTuple = db.checkForMinimumBalance(money)

    # Initialize the betAmount to 0
    betAmount = 0
    
    # Check to see if minimum balance is greater than 5
    if (validatedBalanceTuple[0] == 1):
        # Update the money variable to reflect changes
        money = float(validatedBalanceTuple[1])
        
        # Get user input for the bet
        betAmount = db.getUserBet(money)

        # Check to see if the bet is valid. If not valid, will return value of 0 for betAmount. Function also returns an updated value for money
        betValidationTuple = db.validateBet(money, betAmount)
        money = float(betValidationTuple[0])
        betAmount = float(betValidationTuple[1])
    else:
        # If the minimum balance is less than 5 and user doesn't add more money, return betAmount of zero and money
        return money, betAmount

    # If the user places a valid bet (validated from validateBet and >0):
    if (betAmount > 0):
        money = db.processBet(money, betAmount)
        displayBetSlip(money, betAmount)
        return money, betAmount
    else:
        # If betAmount is set to zero (by validateBet()), return betAmount of 0 and money
        return money, betAmount


# Function that will display the player's bet slip after the bet has been processed
def displayBetSlip(money, betAmount):
    # After processing bet, display the updated money variable, the bet, and the potential payout
    print("\n################################")
    print("Bet successfully placed.")
    print("################################")
    print("Money: " + str(money))
    print("Bet Amount: " + str(betAmount))
    print("Potential Payout: " + str(betAmount * 3/2))
    print("################################")


def displayTitle():
    # Display game title and the betting odds
    print("################################")
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("################################")
    

def main():
    # create the deck of 52 cards
    deckOfCards = card.createDeck()

    # Variable used to control the loop of the game. Will only end when not "y"
    playAgain ="y"
    
    # While loop that controls whether or not the user would like to keep playing. Will run at least once.
    while(playAgain == "y"):
        displayTitle()
        
        # Assign the money from text file to money variable
        money = db.importFile()

        # Tuple used to hold the resultant betAmount and money after userBet() function is called. The userBet() will handle bet related functionality
        betResult = userBet(money)

        # If bet is assigned a value of 0 from userBet() function, end the game. Otherwise, proceed to the actual Blackjack game.
        if (betResult[1] == 0):
            print()
            break

        # Updaate the values of money and betAmount to their respective variables from the returned Tuple from userBet()
        money = betResult[0]
        betAmount = betResult[1]

        # Check to see if the deck should be reshuffled before the turn begins. Will only reshuffle if less than half of original deck remaining
        deckOfCards = card.checkForReshuffle(deckOfCards)

        # Initiate the Blackjack game
        playBlackjack(deckOfCards, money, betAmount)

        # Ask user whether or not they would like to play again
        while True:
            playAgain = input("\nPlay again? (y/n): ")
            if (playAgain.lower() != "y") and (playAgain.lower() != "n"):
                print("Invalid input. Try again!")
                continue
            else:
                break
        print()

        
    # Display "bye" messages to signify the end of the game
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
