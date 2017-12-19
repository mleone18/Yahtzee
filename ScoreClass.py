class Score:
    def __init__(self, dice):
        self.dice = dice
        
    def combos(self):
        print("These are your options:")
        if 1 in self.dice:
            points1 = self.dice.count(1)
            print("You can use aces to get " + str(points1) + " points")
        if 2 in self.dice:
            points2 = 2 * self.dice.count(2)
            print("You can use twos to get " + str(points2) + " points")
        if 3 in self.dice:
            points3 = 3 * self.dice.count(3)
            print("You can use threes to get " + str(points3) + " points")
        if 4 in self.dice:
            points4 = 4 * self.dice.count(4)
            print("You can use fours to get " + str(points4) + " points")
        if 5 in self.dice:
            points5 = 5 * self.dice.count(5)
            print("You can use fives to get " + str(points5) + " points")
        if 6 in self.dice:
            points6 = 6 * self.dice.count(6)
            print("You can use sixes to get " + str(points6) + " points")
        if self.dice.count(1) >= 3 or self.dice.count(2) >= 3 or self.dice.count(3) >= 3 or self.dice.count(4) >= 3 or self.dice.count(5) >= 3 or self.dice.count(6) >= 3:
            points7 = sum(self.dice)
            print("You can use three of a kind to get " + str(points7) + " points")
        if self.dice.count(1) >= 4 or self.dice.count(2) >= 4 or self.dice.count(3) >= 4 or self.dice.count(4) >= 4 or self.dice.count(5) >= 4 or self.dice.count(6) >= 4:
            points8 = sum(self.dice)
            print("You can use four of a kind to get " + str(points8) + " points")
        if self.dice.count(1) >= 5 or self.dice.count(2) >= 5 or self.dice.count(3) >= 5 or self.dice.count(4) >= 5 or self.dice.count(5) >= 5 or self.dice.count(6) >= 5:
            points9 = 50
            print("You can use a YAHTZEE to get " + str(points9) + " points")
        if list(set(sorted(self.dice))) == [1, 2, 3, 4] or list(set(sorted(self.dice))) == [2, 3, 4, 5] or list(set(sorted(self.dice))) == [3, 4, 5, 6] or list(set(sorted(self.dice))) == [1, 2, 3, 4, 5] or list(set(sorted(self.dice))) == [2, 3, 4, 5, 6]:
            points10 = 30
            print("You can use a small straight to get " + str(points10) + " points")
        if list(set(sorted(self.dice))) == [1, 2, 3, 4, 5] or list(set(sorted(self.dice))) == [2, 3, 4, 5, 6]:
            points11 = 40
            print("You can use a large straight to get " + str(points11) + " points")
        if CHANCE:
            points12 = sum(self.dice)
            print("You can use chance to get " + str(points12) + " points")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        