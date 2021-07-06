import sys

FILENAME = "money.txt"

def exitProgram():
    print("\nTerminating program.")
    sys.exit()

def checkForMinimumBalance(money):
    while (money < 5):
        addFunds = input("\nYour account ($" + str(money) + ") currently has less than the required $5 to play.\n" +
                             "Would you like to add additional funds (y/n)?: ")
        if (addFunds.lower() == "y"):
            money = addMoney(money)
            continue
        else:
            print()
            return False

    return True

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

def importFile():
    money = 0

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

def updateBalance():
    money = importFile()
    return money

def processBet(money, betAmount):
    money -= betAmount
    saveFile(money)
    
def processWin(money, betAmount):
    money += round(betAmount * (3/2), 2)
    saveFile(money)
    return money

def processTie(money, betAmount):
    money += betAmount
    saveFile(money)
    return money

def addMoney(money):
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

    money += amountToAdd
    saveFile(money)
    return money

def validateBet(money, betAmount):
    newBet = "y"
    addFunds = "y"
    
    while ((betAmount < 5) or (betAmount > 1000)):
        print("\nError, invalid bet amount. Please select an amount between 5 and 1000.")
        print("\nMoney: " + str(money))
        try:
            betAmount = float(input("Bet amount: "))
        except ValueError:
            print("Invalid number. Please try again!\n")
            continue
        except Exception as e:
            print("An unexpected error has occured")
            print(type(e), e)
            exitProgram()

    while (betAmount > money):   
        addFunds = input("\nError. Your account ($" + str(money) + ") currently has less funds than the bet amount.\n" +
                         "Would you like to add additional funds (y/n)?: ")
        if (addFunds.lower() == "y"):
                money = addMoney(money)
        else:
            newBet = input("\nWould you like to make a different bet (y/n)?: ")
            if (newBet.lower() == "y"):
                while True:
                    try:
                        print("\nMoney: " + str(money))
                        betAmount = float(input("Bet amount: "))
                    except ValueError:
                        print("Invalid number. Please try again!\n")
                        continue
                    except Exception as e:
                        print("An unexpected error has occured")
                        print(type(e), e)
                        exitProgram()
                    if ((betAmount < 5) or (betAmount > 1000)):
                        print("Error, invalid bet amount. Please select an amount between 5 and 1000.")
                        continue
                    else:
                        break
            else:
                break

    if ((newBet.lower() != "y") and (addFunds.lower() != "y") and (betAmount > money)):
        return False
    else:
        processBet(money, betAmount)
        return True

#def saveFile(money, fileName):
#    with open(fileName, "w") as file:
#        for item in money:
#            file.write(item +"\n")
            

#def importFile(money, fileName):
#    with open(fileName) as file:
#        for line in file:
#            line = line.replace("\n", "")
#            money.append(line)
