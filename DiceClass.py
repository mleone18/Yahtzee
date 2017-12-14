from random import randint

class Die():
        def __init__(self):
            self.numbers = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            print(self.numbers)
            
        def reroll(self):
            x = 1
            while x < 3:
                ans = str(input("What number dice do you want to reroll? (1-5) (Separate numbers with a space) (Leave blank for no reroll)"))   
                ans2 = list(map(int, ans.split()))  
                i = 0
                while i < len(ans2):
                    self.numbers[i-1] = randint(1,6)
                    i += 1
                x += 1
                print(self.numbers)

