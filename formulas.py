class Calculations(): 
	def __init__(self, dice, score):
		self.dice = dice
		self.score = score

	def check(self, num): #the upper levels all use the same scoring function since it is the sum of the value. 
		counter = self.dice.count(num)
		self.score += counter*num

	def Upperbonus(self):
		if self.score > 62:
			self.score += 35

	def dicesum(self): #three of a kind, four of a kind, and chance all have the same scoring output.
		self.score += sum(self.dice)

	def lower(self, integ): #fullhouse, small straight, large straight and yahtzee all use same function but in runner code will have different integers added because set score values. 
		self.score += integ #30, 40 50

	def updateDice(self, dice):
		self.dice = dice
