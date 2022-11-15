import random
# print("hello world")

clearField = [[],[],[],[]]
mineAmount = 3
#populates clearField with 9s
for i in range(4):
    for j in range(4):
        clearField[i].append(0)
# print(clearField)

#randomly chooses 4 unique places for mine
#10,12,13,14 - 21,22,23,24 - 31,32,33,34 - 41,42,43,44
fourRandNums = list(random.sample(range(0,15),mineAmount))
minePositions = []
for i in range(mineAmount):
    possiblePositions = ["00","01","02","03",
                        "10","11","12","13",
                        "20","21","22","23",
                        "30","31","32","33"]

    minePositions.append(possiblePositions[fourRandNums[i]])

# print(minePositions)

#populates clearField with Mines and 9s

def my_function(minePosition):
    #row where the mine should be placed
    x = int(minePosition[0:1])
    #column where the mine should be placed
    y = int(minePosition[1:2])
    clearField[x][y] = "M"


for i in range(mineAmount):
    my_function(minePositions[i])

#print clearField with proper formatting
def printClearField(field):
    print("         A    B    C    D") #print ABCD at top row
    #      |
    print("        -----------------")
    alpha = ["      A|","      B|","      C|","      D|"]
    for i in range(4):
        print(alpha[i], end =" ")
        for j in range(4):
            print(field[i][j], end="")
            print("    ", end="")
        if i != 3: 
            print("\n       |")
    print("")

#fills in array with 0s,1s,2s, etc.

for i in range(4): #row iterator
    for j in range(4): #column iterator

        #=======center=======#
        #if ur not 1st or 4th row or 1st and 4th column, check 3x3
        if (i != 0 and i != 3) and (j != 0 and j != 3):
            #iterate through a 3x3 and add i or j to it
            for k in range(-1,2):
                for l in range(-1,2):
                    if (clearField[k+i][j+l] == "M") and (clearField[i][j] != "M"):
                        clearField[i][j] += 1
        
        #=======corners=======#
        #row,column,row bounds,column bounds
        def cornerHelper(a,b,c,d,e,f):
            if i == a and j == b:
                for k in range(c,d):
                    for l in range(e,f):
                        if (clearField[i + k][j + l] == "M") and (clearField[i][j] != "M"):
                            clearField[i][j] += 1

        #top left-right, then bottom left-right
        cornerHelper(0,0,0,2,0,2)
        cornerHelper(3,0,-1,1,0,2)
        cornerHelper(0,3,0,2,-1,1)
        cornerHelper(3,3,-1,1,-1,1)
        
        #=======edges=======#
        #row,column,row bounds,column bounds
        def edgeHelper(a,b,c,d,e,f):
            if i == a and j == b:
                for k in range(c,d):
                    for l in range(e,f):
                        if (clearField[i + k][j + l] == "M") and (clearField[i][j] != "M"):
                            clearField[i][j] += 1

        #right edge - you want it to do everything, except column j-1
        edgeHelper(1,0,-1,2,0,2)
        edgeHelper(2,0,-1,2,0,2)

        #top edge - except row i-1
        edgeHelper(0,1,0,2,-1,2)
        edgeHelper(0,2,0,2,-1,2)

        #left edge - except column j+1
        edgeHelper(1,3,-1,2,-1,1)
        edgeHelper(2,3,-1,2,-1,1)

        #bottom edge - except row i+i
        edgeHelper(3,1,-1,1,-1,2)
        edgeHelper(3,2,-1,1,-1,2)


# printClearField(clearField)

userField = [[],[],[],[]]
#populates clearField with *'s
for i in range(4):
    for j in range(4):
        userField[i].append("*")

#letter combo AC

def generateNumberFromLetter(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2
    elif letter == "D":
        return 3
    else:
        print("error somewhere")

gameOver = False

print("=====================================")
print("=======Welcome to Midsweeper!========")
print("To play, input row followed by column")
print("Put an F after both to flag the space")
print("=====================================")
print("=====================================")
print("")

printClearField(userField)
while gameOver == False:
    userInput = input("\nEnter your value: ")

    x = generateNumberFromLetter(userInput[0:1])
    y = generateNumberFromLetter(userInput[1:2])

    if clearField[x][y] == "M":
        printClearField(clearField)
        print("\n==========You Lost!==========\n")
        gameOver = True
        break
    userField[x][y] = clearField[x][y]
    printClearField(userField)










