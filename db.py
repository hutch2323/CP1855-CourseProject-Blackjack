import sys

"""
This module handles all the financial calculations for the blackjack game. It also reads a monetary amount from a file, updates the amount, and saves the file.
"""

# Constant/global variable used to hold the file name used by several of the functions in the module
FILENAME = "money.txt"


# This function displays a message and exit the program
def exitProgram():
    print("\nTerminating program.")
    sys.exit()


# This function retrieves a bet amount from the user. It also displays the curent balance (money) parameter while attempting to place a bet. It will return the user's bet amount.
def getUserBet(money):
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
            exitProgram()
        # Validation to ensure that the bet amount is >= 5 and <= 1000
        if ((betAmount < 5) or (betAmount > 1000)):
            print("Error, invalid bet amount. Please select an amount between 5 and 1000.")
            continue
        else:
            break

    return betAmount


# This function checks to see if the user's balance (money parameter) is greater than or equal to 5. If balance is less than 5, user prompted to add additional funds to account.
def checkForMinimumBalance(money):

    # variable that holds whether or not the balance has the minimum amount required to continue. Will be 0 if < minimum, will be 1 if >= minimum.
    isMinimumBalance = 0

    # Tuple will return a boolean (true/false) as well as the current value of money
    #balanceValidation = (isMinimumBalance, money)
    
    while (money < 5):
        addFunds = input("\nYour account ($" + str(money) + ") currently has less than the required $5 to play.\n" +
                             "Would you like to add additional funds (y/n)?: ")
        # If the user wants to add more money to their account, call the addMoney() function. Otherwise, set isMinimumBalance to 0 (false) and return the tuple
        if (addFunds.lower() == "y"):
            money = addMoney(money)
            continue
        else:
            print()
            isMinimumBalance = 0
            return isMinimumBalance, money

    # If the minimum balance is achieved, set isMinimumBalance to 1 (true) and return the tuple of isMinimumBalance and money
    isMinimumBalance = 1
    return isMinimumBalance, money

# Function that takes the current balance (money) as a parameter and updates the file
def saveFile(money):
    try:
        with open(FILENAME, "w") as file:
            file.write(str(money))
    except OSError as e:
        print("An OS error has occured!")
        print(type(e), e)
        exit_program()
    except Exception as e:
        print("Unexpected error has occured!")
        print(type(e), e)
        exitProgram()


# Function used to read the text file and assign the balance value the money variable. This variable is then returned.
def importFile():
    # Initialize money variable to 0
    money = 0

    # If the file isn't found or there is an unexpected error, a message will be displayed and the exitProgram() function will be called
    try:
        with open(FILENAME) as file:
            money = file.readline()
    except FileNotFoundError as e:
        print("Could not find " + FILENAME + " file.")
        exit_program()
    except Exception as e:
        print("Unexpected error has occured!")
        print(type(e), e)
        exitProgram()

    return float(money)

# Function that processes the user's bet. Takes the current balance and betAmount as parameters, removes the bet amount, then updates the file holding the balance
def processBet(money, betAmount):
    money -= betAmount
    saveFile(money)
    return money


# Function that processes a user win. Takes current balance and bet amount as parameters, and adds the betAmount * 3/2 (betting odds) to the balance. Then calls saveFile()
def processWin(money, betAmount):
    money += round(betAmount * (3/2), 2)
    saveFile(money)
    return money


# Function that processes a tie. Takes current balance and bet amount as parameters, and adds (returns) the bet amount back to the user's balance (money). Saves the file and returns the updated balance
def processTie(money, betAmount):
    money += betAmount
    saveFile(money)
    return money


# Function used to handle user adding money to their account balance. Takes the current balance as a parameter, adds the requsted amount, saves the file, and returns new balance (money)
def addMoney(money):
    # Prompts user for an amount of money to add and validates the value
    while True:
        try:
            amountToAdd = float(input("\nAmount to add: "))
        except ValueError:
            print("Invalid number. Please try again!")
            continue
        except Exception as e:
            print("An unexpected error has occured")
            print(type(e), e)
            exitProgram()
        if(amountToAdd > 0):
            break
        else:
            print("Please enter a valid number greater than zero. Try again!")

    # Add funds to current balance (money)
    money += amountToAdd
    saveFile(money)
    return money
    

# Function used to validate the user's bet. Takes the balance (money) and the betAmount as parameters. Will return the bet amount (0 if the bet is cancelled)
def validateBet(money, betAmount):
    # Initialize the options of adding funds or making a new bet to "y"
    newBet = "n"
    addFunds = "n"

    # While loop that will execute until broken/return statement
    while True:
        # If current money is greater than or equal to betAmount, validate and return the resultant tuple
        if (money >= betAmount):
            return money, betAmount

        # While loop used to check if the bet requested exceeds the account balance (money)
        while (betAmount > money):   
            addFunds = input("\nError. Your account ($" + str(money) + ") currently has less funds than the bet amount.\n" +
                             "Would you like to add additional funds (y/n)?: ")
            # If bet amount exceeds money available, ask user if they would like to add funds to their account
            if (addFunds.lower() == "y"):
                    # Call addMoney() function and update money variable with new balance
                    money = addMoney(money)                
            else:
                # If user doesn't want to add more money, ask if they would like to place a different bet
                newBet = input("\nWould you like to make a different bet (y/n)?: ")
                if (newBet.lower() == "y"):
                    # Call getUserBet() function and assign returned value to betAmount variable
                    betAmount = getUserBet(money)
                    continue
                else:
                    # If user doesn't want to add more funds and declines to make a new bet, set bet to 0 and return the resultant tuple
                    betAmount = 0
                    return money, betAmount

            # If the user decides to add more funds (money) and decides to change their previous bet
            if(addFunds.lower() == "y") and (newBet.lower() != "y"):
                confirmBet = "n"
                print("\nMoney: " + str(money))
                print("Bet Amount: " + str(betAmount))
                confirmBet = input("Confirm bet (y/n)?: ")

                # if the bet is confirmed, return the tuple of money and betAmount
                if (confirmBet == "y"):
                    return money, betAmount
                else:
                    # If user doesn't want to add more money, ask if they would like to place a different bet
                    newBet = input("\nWould you like to make a different bet (y/n)?: ")
                    if (newBet.lower() == "y"):
                        # Call getUserBet() function and assign returned value to betAmount variable
                        betAmount = getUserBet(money)
                      
                        continue
                    else:
                        # If user doesn't want to place a new bet, set the betAmount to 0 and return the resultant tuple
                        betAmount = 0
                        return money, betAmount

        # If the user's bet is more than the current balance (money), user declines to add additional funds, and declines to place a new bet, return the resultant tuple
        if ((newBet.lower() != "y") and (addFunds.lower() != "y") and (betAmount > money)):
            betAmount = 0
            return money, betAmount
    
