def saveFile(money, fileName):
    with open(fileName, "w") as file:
        file.write(str(money))

def importFile(fileName):
    money = 0
    
    with open(fileName) as file:
        money = file.readline()

    return float(money)

def processBet(money, betAmount, fileName):
    money -= betAmount
    saveFile(money, fileName)
    return money

def processWin(money, betAmount, fileName):
    money += betAmount * (3/2)
    saveFile(money, fileName)
    return money

def processTie(money, betAmount, fileName):
    money += betAmount
    saveFile(money, fileName)
    return money

#def saveFile(money, fileName):
#    with open(fileName, "w") as file:
#        for item in money:
#            file.write(item +"\n")
            

#def importFile(money, fileName):
#    with open(fileName) as file:
#        for line in file:
#            line = line.replace("\n", "")
#            money.append(line)
