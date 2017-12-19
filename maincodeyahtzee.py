from DiceClass import Die #acess the dice rolling file and import its roll class
from formulas import Calculations #from the scorecard file, import the class that has the score calculations
from ScoreClass import Score #from the scoreclass file, import the class that determines which calculation to use based on the user's choice.

play = input('Would you like to play Yahtzee?')
if play == "no" or play == "No":
	play = input('Would you like to play Yahtzee?')


die = Die()
die.reroll()
myscore = Score(die.numbers)
myscore.combos()

