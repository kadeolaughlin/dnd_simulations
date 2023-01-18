import random as rand

class Dice():

#    def __init__(self, roll, hitmodifier):
#        self.hm = hitmodifier
#        t_dice = roll.split('+', -1)
#        for die in t_dice:
#            t_die = die.split('d', 1)
#            if len(t_die) == 1:
#                self.modifier = int(die[0])
#            else:
#                self.dice.append([t_die[0],t_die[1]])

    #roll = XdX, hitmodifier = +X, bonud = XdX/None
    def __init__(self, roll, hitmodifier, bonus):
        self.modifier = 0
        self.dice = []
        self.hm = 0
        self.extra = False
        self.bonus_dice = []
        self.bonus_charge = 0

        self.hm = hitmodifier
        t_dice = roll.split('+', -1)
        for die in t_dice:
            t_die = die.split('d', 1)
            if len(t_die) == 1:
                self.modifier = int(die[0])
            else:
                self.dice.append([t_die[0],t_die[1]])
        
        if(bonus != None):
            self.extra=True
            b_dice = bonus.split('+', -1)
            for die in b_dice:
                b_die = die.split('d', 1)
                if len(b_die) == 1:
                    self.modifier = int(die[0])
                else:
                    self.bonus_dice.append([b_die[0],b_die[1]])
    
    #Print a description of the die
    def print(self):
        rtn = ""
        for roll in self.dice:
            rtn += roll[0]
            rtn += 'd'
            rtn += roll[1]
            rtn += '+'
        rtn += str(self.modifier)
        if(self.bonus_dice != None):
            for roll in self.bonus_dice:
                rtn += '+'
                rtn += roll[0]
                rtn += 'd'
                rtn += roll[1]
        return rtn

    #roll for damage
    def attack_roll(self, crit):
        bonus_roll = 0
        standard_roll = 0
        multiplier = 1
        if(crit):
            multiplier = 2
        if(self.extra and self.bonus_charge > 0):
            if(rand.randint(0,1) == 1):
                for roll in range(self.bonus_charge):
                    if(rand.randint(0,1) == 1):
                        bonus_roll += rand.randint(1,int(self.bonus_dice[0][1]))
                        self.bonus_charge -= 1
                        #print(bonus_roll)
        if(self.extra and bonus_roll == 0 and self.bonus_charge < int(self.bonus_dice[0][0])):
            self.bonus_charge += 1
        for roll in self.dice:
            for i in range(int(roll[0])):
                standard_roll += rand.randint(1,int(roll[1]))
        return multiplier * (standard_roll + bonus_roll) + self.modifier
    
    #roll to hit
    def attack(self):
        ac = rand.randint(10, 20)
        #print(ac)
        damage = 0
        diceroll = rand.randint(1, 20)
        #print('' + str(diceroll) + '+' + str(self.modifier))
        if(diceroll >= 19):
            damage = self.attack_roll(True)
        elif(diceroll + int(self.hm) > ac):
            damage = self.attack_roll(False)
        return damage




die1 = Dice("2d6+3", "6", "6d4")
total1 = 0
total2 = 0
die2 = Dice("2d6+6", "4", None)
for i in range(1000):
    temp_total1 = 0
    temp_total2 = 0
    spacer = ""
    for i in range(2):
        temp_total1 += die1.attack()
    for i in range(3):
        temp_total2 += die2.attack()
    if(temp_total1 < 10):
        spacer = " "
    print(die1.print() + ": " + str(temp_total1) + "    " + spacer + die2.print() + ": " + str(temp_total2))
    total1 += temp_total1
    total2 += temp_total2
print("--------------------------")
print(die1.print() + ": " + str(int(round(total1/1000))) + "    " + die2.print() + ": " + str(int(round(total2/1000))))
#print(die2.print())
#print(die1.print())
#print(die2.print() + ":  " + str(int(round(total/10000))))
#die1.print()