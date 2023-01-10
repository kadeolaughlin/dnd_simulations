import random as rand

def getminroll(roll):
    minroll = 0
    for die in roll:
        minroll += int(die[0])
    return minroll

def getmaxroll(roll):
    maxroll = 0
    for die in roll:
        if(len(die) == 1):
            maxroll += int(die[0])
        else:
            maxroll += int(die[0]) * int(die[1])
    return maxroll

def gettrueroll(roll):
    trueroll = 0
    for die in roll:
        if(len(die)) == 1:
            trueroll += int(die[0])
        else:
            trueroll += int(die[0]) * rand.randint(1, int(die[1]))
    return trueroll

def getaverageroll(roll):
    averageroll = 0
    for i in range(1000):
        averageroll += gettrueroll(roll)
    averageroll = averageroll // 1000
    return averageroll

def genroll(dice):
    roll = dice.split('+')
    roll = [die.split('d') for die in roll]
    return roll

def metrics(dice):
    roll = genroll(dice)
    minroll = getminroll(roll)
    maxroll = getmaxroll(roll)
    averageroll = getaverageroll(roll)
    rtn = [minroll, maxroll, averageroll]
    return rtn

def rolldice(dice):
    return gettrueroll(genroll(dice))
    

    