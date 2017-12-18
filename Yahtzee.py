class Scorecard(): 
	def __init__(self, dice, score):
		self.dice = dice
		self.score = 0

	def check(self, num): #the upper levels all use the same scoring function since it is the sum of the value. 
		counter = self.dice.count(num)
		self.score = self.score + counter*num
		return self.score

	def Upperbonus(self):
		if self.score > 62:
			self.score = self.score + 35
		else:
			return self.score

	def dicesum(self): #three of a kind, four of a kind, and chance all have the same scoring output.
		self.score = self.score + sum(self.dice)
		return self.score

	def lower(self): #fullhouse, small straight, large straight and yahtzee all use same function but in runner code will have different integers added because set score values. 
		self.score = self.score + 25 #30, 40 50
		return self.score

	def grandtotal(self):
		return self.score