from collections import Counter
from game_of_greed.game_logic import GameLogic,Banker

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        self.game = GameLogic()
        self.banker = Banker()
        self.round = 1
        self.remaining_dice = 6
        self.score = 0
        self.to_shelf = 0
        self.stop = False

    def play(self):
        print('Welcome to Game of Greed')
        res = input("Wanna play?")
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
            self.start()

    def start(self):
        while self.score < 10000 and self.stop == False:
            print(f'Starting round {self.round}')
            self.remaining_dice = 6
            self.rolling_again()

    def end(self):
        print(f'Total score is {self.score} points')
        print(f'Thanks for playing. You earned {self.score} points')
        self.stop = True
        
    def validate_in(self, user_in, roll):
        counting_saved = Counter(tuple([int(x) for x in roll]))
        counting_ins = Counter(tuple([int(x) for x in user_in]))
        yes = True
        for x in counting_ins:
            if counting_ins[x] > counting_saved[x]:
                yes = False
        return yes
        
    def valid_cases(self, arr):
        self.remaining_dice = self.remaining_dice - len(arr)
        print(f'You have {self.to_shelf} unbanked points and {self.remaining_dice} dice remaining')
        next_step = input("(r)oll again, (b)ank your points or (q)uit ")
        if len(arr) == 6 and self.to_shelf > 0:
            self.remaining_dice = 6            
        if next_step == 'b':
            self.banked()
        elif next_step == 'q':
            self.end()
        elif next_step == 'r':
            self.to_shelf += self.banker.shelved
            self.rolling_again()

    def banked(self):
        self.banker.shelf(self.to_shelf)
        banked = self.banker.bank()
        self.to_shelf = 0
        self.score += banked
        print(f"You banked {banked} points in round {self.round}")
        self.round += 1
        print(f'Total score is {self.score} points')

    def zilch(self,validate):
        print('Zilch!!! Round over')
        print(f'You banked {validate} points in round {self.round}')
        print(f'Total score is {self.score} points')
        self.round += 1
        self.remaining_dice = 6
        print(f'Starting round {self.round}')
        self.rolling_again()  

    def rolling_again(self):

        print(f'Rolling {self.remaining_dice} dice...')
        roll = self.roller(self.remaining_dice)
        print(','.join([str(i) for i in roll]))
        arr = list(roll)
        validate = self.game.calculate_score(tuple([int(x) for x in arr]))

        if validate != 0:   
            dice_to_keep = input("Enter dice to keep (no spaces), or (q)uit: ")

            if dice_to_keep == 'q':
                self.end()
            else :
                valid = self.validate_in(dice_to_keep, roll)

                while valid == False:
                    print('Cheater!!! Or possibly made a typo...')
                    print(','.join([str(i) for i in roll]))
                    dice_to_keep = input("Enter dice to keep (no spaces), or (q)uit: ")
                    if dice_to_keep == 'q':
                        self.end()
                        break
                    else:
                        valid = self.validate_in(dice_to_keep, roll)

                arr = list(dice_to_keep)
                total = self.game.calculate_score(tuple([int(x) for x in arr]))
                self.to_shelf += total
                self.valid_cases(arr)

        elif  validate == 0: 
            self.zilch(validate)

if __name__ == '__main__':
    game = Game()
    game.play()