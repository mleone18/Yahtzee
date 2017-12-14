class Scorecard(): 
	def __init__(self, dice, score):
		self.dice = dice
		self.score = 0

	def checkAces(self):
		self.score = self.score + self.dice.count(1)
		return self.score

	def checkTwos(self):
		twos = self.dice.count(2)
		self.score = self.score + twos*2
		return self.score

	def checkThrees(self):
		threes = self.dice.count(3)
		self.score = self.score + threes*3
		return self.score

	def checkFours(self):
		fours = self.dice.count(4)
		self.score = self.score + fours*4
		return self.score

	def checkFives(self):
		fives = self.dice.count(5)
		self.score = self.score + fives*5
		return self.score

	def checkSixes(self):
		sixes = self.dice.count(6)
		self.score = self.score + sixes*6
		return self.score

	def Upperbonus(self):
		if self.score > 62:
			self.score = self.score + 35
		else:
			return self.score

	def threekind(self):
		self.score = self.score + sum(self.dice)
		return self.score

	def fourkind(self):
		self.score = self.score + sum(self.dice)
		return self.score
		
	def fullhouse(self):
		self.score = self.score + 25
		return self.score

	def smallstraight(self):
		self.score = self.score + 30
		return self.score

	def largestraight(self):
		self.score = self.score + 40
		return self.score

	def YAHTZEE(self):
		self.score = self.score + 50
		return self.score

	def chance(self):
		self.score = self.score + sum(self.dice)
		return self.score

	def grandtotal(self):
		return self.score