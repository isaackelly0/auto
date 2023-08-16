import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    #create list of 100 heads or tails values
    flips = []
    streakAttempt = 0
    for i in range(100):
        flips.append(random.randint(0,1))
    #check if there is a streak of 6 in a row
    for flip in range(len(flips)):
        if flip != 0:
            currentNum = flips[flip]
            if currentNum == pastNum:
                streakAttempt += 1
                if streakAttempt == 6:
                    numberOfStreaks += 1
                    streakAttempt = 0
            else:
                streakAttempt = 0
            pastNum = flips[flip]
        else:
            pastNum = flips[flip]
            
print('Chance of streak: %s%%' % (numberOfStreaks/100))