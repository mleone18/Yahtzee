from formulas import Calculations
class Score:
    def __init__(self, dice):
        self.dice = dice
        self.bools = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.bools2 = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        
    def combos(self):
        print("These are your options:")
        if 1 in self.dice and self.bools[0] == False:
            points1 = self.dice.count(1)
            self.bools2[0] = True
            print("You can use aces to get " + str(points1) + " points")
        if 2 in self.dice and self.bools[1] == False:
            points2 = 2 * self.dice.count(2)
            self.bools2[1] = True
            print("You can use twos to get " + str(points2) + " points")
        if 3 in self.dice and self.bools[2] == False:
            points3 = 3 * self.dice.count(3)
            self.bools2[2] = True
            print("You can use threes to get " + str(points3) + " points")
        if 4 in self.dice and self.bools[3] == False:
            points4 = 4 * self.dice.count(4)
            self.bools2[3] = True
            print("You can use fours to get " + str(points4) + " points")
        if 5 in self.dice and self.bools[4] == False:
            points5 = 5 * self.dice.count(5)
            self.bools2[4] = True
            print("You can use fives to get " + str(points5) + " points")
        if 6 in self.dice and self.bools[5] == False:
            points6 = 6 * self.dice.count(6)
            self.bools2[5] = True
            print("You can use sixes to get " + str(points6) + " points")
        if self.dice.count(1) >= 3 and self.bools[6] == False or self.dice.count(2) >= 3 and self.bools[6] == False or self.dice.count(3) >= 3 and self.bools[6] == False or self.dice.count(4) >= 3 and self.bools[6] == False or self.dice.count(5) >= 3 and self.bools[6] == False or self.dice.count(6) >= 3 and self.bools[6] == False:
            points7 = sum(self.dice)
            self.bools2[6] = True
            print("You can use three of a kind to get " + str(points7) + " points")
        if self.dice.count(1) >= 4 and self.bools[7] == False or self.dice.count(2) >= 4 and self.bools[7] == False or self.dice.count(3) >= 4 and self.bools[7] == False or self.dice.count(4) >= 4 and self.bools[7] == False or self.dice.count(5) >= 4 and self.bools[7] == False or self.dice.count(6) >= 4 and self.bools[7] == False:
            points8 = sum(self.dice)
            self.bools2[7] = True
            print("You can use four of a kind to get " + str(points8) + " points")
        if self.dice.count(1) >= 5 and self.bools[8] == False or self.dice.count(2) >= 5 and self.bools[8] == False or self.dice.count(3) >= 5 and self.bools[8] == False or self.dice.count(4) >= 5 and self.bools[8] == False or self.dice.count(5) >= 5 and self.bools[8] == False or self.dice.count(6) >= 5 and self.bools[8] == False:
            points9 = 50
            self.bools2[8] = True
            print("You can use a yahtzee to get " + str(points9) + " points")
        if list(set(sorted(self.dice)))[:5] == [1, 2, 3, 4] and self.bools[9] == False or list(set(sorted(self.dice)))[:5] == [2, 3, 4, 5] and self.bools[9] == False or list(set(sorted(self.dice)))[:-5] == [2, 3, 4, 5] and self.bools[9] == False or list(set(sorted(self.dice)))[:-5] == [3, 4, 5, 6] and self.bools[9] == False or list(set(sorted(self.dice))) == [1, 2, 3, 4, 5] and self.bools[9] == False or list(set(sorted(self.dice))) == [2, 3, 4, 5, 6] and self.bools[9] == False:
            points10 = 30
            self.bools2[9] = True
            print("You can use a small straight to get " + str(points10) + " points")
        if list(set(sorted(self.dice))) == [1, 2, 3, 4, 5] and self.bools[10] == False or list(set(sorted(self.dice))) == [2, 3, 4, 5, 6] and self.bools[10] == False:
            points11 = 40
            self.bools2[10] = True
            print("You can use a large straight to get " + str(points11) + " points")
        if self.bools[11] == False:
            points12 = sum(self.dice)
            self.bools2[11] = True
            print("You can use chance to get " + str(points12) + " points")
        if sorted(self.dice)[0] == sorted(self.dice)[1] and sorted(self.dice)[2] == sorted(self.dice)[3] and sorted(self.dice)[3] == sorted(self.dice)[4] and self.bools[12] == False or sorted(self.dice)[0] == sorted(self.dice)[1] and sorted(self.dice)[1] == sorted(self.dice)[2] and sorted(self.dice)[3] == sorted(self.dice)[4] and self.bools[12] == False:
            points13 = 25
            self.bools2[12] = True
            print("You can use a full house to get " + str(points13) + " points")
        c = Calculations(self.dice) #being taken from calculations class, taking self.numbers from Score class.
        while True:
            print("Type 'stop' to end the game")
            ans = str(input("What would you like to do?" ))            
            if ans.lower() == "aces" and self.bools2[0] == True:
                self.bools[0] = True
                c.check(1)
                break
            elif ans.lower() == "twos" and self.bools2[1] == True:
                self.bools[1] = True
                c.check(2)
                break
            elif ans.lower() == "threes" and self.bools2[2] == True:
                self.bools[2] = True
                c.check(3)
                break
            elif ans.lower() == "fours" and self.bools2[3] == True:
                self.bools[3] = True
                c.check(4)
                break
            elif ans.lower() == "fives" and self.bools2[4] == True:
                self.bools[4] = True
                c.check(5)
                break
            elif ans.lower() == "sixes" and self.bools2[5] == True:
                self.bools[5] = True
                c.check(6)
                break
            elif ans.lower() == "three of a kind" and self.bools2[6] == True:
                self.bools[6] = True
                c.dicesum()
                break
            elif ans.lower() == "four of a kind" and self.bools2[7] == True:
                self.bools[7] = True
                c.dicesum()
                break
            elif ans.lower() == "yahtzee" and self.bools2[8] == True:
                self.bools[8] = True
                c.lower()
                break
            elif ans.lower() == "small straight" and self.bools2[9] == True:
                self.bools[9] = True
                c.lower()
                break
            elif ans.lower() == "large straight" and self.bools2[10] == True:
                self.bools[10] = True
                c.lower()
                break
            elif ans.lower() == "chance" and self.bools2[11] == True:
                self.bools[11] = True
                c.dicesum()
                break
            elif ans.lower() == "full house" and self.bools2[12] == True:
                self.bools[12] = True
                c.lower()
                break
            elif ans.lower() == "stop":
                print("You finished with a score of " + c.score + " points.")
                break
            else:
                print("I don't know what " + ans + " means, try again.")
        self.bools2 = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        print('Score: ' + str(c.score))
        

            
            
            
            
            
            
            
            
            
            
        