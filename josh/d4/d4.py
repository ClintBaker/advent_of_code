# load input data
input = (open("dayFourTestData.txt").read()).split("\n")
# convert to string to pull [][] positions later and len
inputStr = [str(digit) for digit in input]
# get the len of all the characters in string
inputLen = sum(len(n) for n in inputStr)


row = 0
column = 0
totalRolls = 0
pickUp = 0


def checkForRolls():
    global totalRolls
    global pickUp
    
    if inputStr[row][column-1] == '@' and 0 <= column < len(inputStr):
        pickUp += 1

    if inputStr[row][column+1] == '@' and 0 <= column < len(inputStr):
        pickUp += 1

    if inputStr[row-1][column] == '@' and row >= 0:
        pickUp += 1

    if inputStr[row-1][column-1] == '@' and row >= 0 and 0 <= column < len(inputStr):
        pickUp += 1

    if inputStr[row-1][column+1] == '@' and row >= 0 and 0 <= column < len(inputStr):
        pickUp += 1

    if inputStr[row+1][column] == '@' and row >= 0:
        pickUp += 1

    if inputStr[row+1][column-1] == '@' and row >= 0 and 0 <= column < len(inputStr):
        pickUp += 1

    if inputStr[row+1][column+1] == '@' and row >= 0 and 0 <= column < len(inputStr):
        pickUp += 1

    if pickUp < 4:
        totalRolls += 1
        print("LOOOOOOK")
    pickUp = 0     






            


for n in range(inputLen): # for each character in the input
    if inputStr[row][column] == '@':
        checkForRolls()
    print(inputStr[row][column])
    # increment over each column and each row
    column += 1
    if column == len(inputStr):
        column = 0
        row += 1
print(totalRolls)
print(len(inputStr))





# look at each string of "len(split)"
# look at length of each string
# look at each digit in string
# check if the character is @ symbol
# check if current string array values +1 or -1 is an @ symbol
# check if previous string array value current or +1 or -1 is an @ symbol
# check if next string array value current or +1 or -1 is an @ symbol
# IF @ FOUND < 4, do both --> increase counter += 1 and change @ to and "X"