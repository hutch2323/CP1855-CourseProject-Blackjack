FILENAME = "money.txt"

def saveFile(money):
    with open(FILENAME, "w") as file:
        file.write(str(money))

def importFile():
    money = 0
    
    with open(FILENAME) as file:
        money = file.readline()

    return float(money)

def refreshFunds():
    money = importFile()
    return money

def processBet(money, betAmount):
    money -= betAmount
    saveFile(money)
    return money

def processWin(money, betAmount):
    money += round(betAmount * (3/2), 2)
    saveFile(money)
    return money

def processTie(money, betAmount):
    money += betAmount
    saveFile(money)
    return money

def addMoney(money):
    money += float(input("\nAmount to add: "))
    saveFile(money)
    return money

def validateBet(money, betAmount):
    while ((betAmount < 5) or (betAmount > 1000)):
        print("\nError, invalid bet amount. Please select an amount between 5 and 1000.")
        print("\nMoney: " + str(money))
        betAmount = float(input("Bet amount: "))

    while (betAmount > money):
        newBet = "y"
        addFunds = "y"
        
        addFunds = input("\nError. Your account currently has less funds than the bet amount. Would you like to add additional funds (y/n)?: ")
        if (addFunds.lower() == "y"):
                money = addMoney(money)
        else:
            newBet = input("\nWould you like to make a different bet (y/n)?: ")
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
        return False
    else:
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
