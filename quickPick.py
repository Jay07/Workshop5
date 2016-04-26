import random

quickPickNumber = int(input("How many quick picks?"))

while quickPickNumber > 0:

    sixNumberList = []
    numberOutput = ""

    for i in range(1, 7):
        randomNumber = random.randint(1, 45)
        validRandomNumber = False
        while not validRandomNumber:
            if randomNumber in sixNumberList:
                randomNumber = random.randint(1, 45)
            else:
                validRandomNumber = True
                sixNumberList.append(randomNumber)
        i += 1

    quickPickNumber -= 1
    sixNumberList.sort()

    for pickNumber in sixNumberList:
        pickNumber = str(pickNumber)
        pickNumber = pickNumber.strip(",[]")
        pickNumber = "{:2s}".format(pickNumber)
        numberOutput = numberOutput + " " + pickNumber

    print(numberOutput)