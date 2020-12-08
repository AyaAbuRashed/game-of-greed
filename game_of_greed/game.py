from game_of_greed.game_logic import GameLogic,Banker

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    game = GameLogic()
    banker = Banker()
    round = 1
    remaining_dice = 6
    score = 0
    to_shelf = 0
    stop = False
    
    def play(self):
        print('Welcome to Game of Greed')
        res = input("Wanna play?")
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
           self.start()
    
    def start(self):
        while Game.score < 10000 and Game.stop == False:
            print(f'Starting round {Game.round}')
            Game.remaining_dice = 6
            self.rolling_again()

    def end(self):
        print(f'Total score is {Game.score} points')
        print(f'Thanks for playing. You earned {Game.score} points')
        Game.stop = True

    def validate_in(self, user_in, roll):
        arr = list(user_in)
        saved = tuple([int(x) for x in arr])
        for x in saved:
            if x not in roll:
                return False
        return True
    
    def valid_cases(self, arr):
        Game.remaining_dice = Game.remaining_dice - len(arr)
        print(f'You have {Game.to_shelf} unbanked points and {Game.remaining_dice} dice remaining')
        next_step = input("(r)oll again, (b)ank your points or (q)uit ")
        if len(arr) == 6:
            Game.remaining_dice = 6            
        if next_step == 'b':
            self.banked()
        elif next_step == 'q':
            self.end()
        elif next_step == 'r':
            Game.to_shelf += Game.banker.shelved
            self.rolling_again()
    
    def banked(self):
        Game.banker.shelf(Game.to_shelf)
        banked = Game.banker.bank()
        Game.to_shelf = 0
        Game.score += banked
        print(f"You banked {banked} points in round {Game.round}")
        Game.round += 1
        print(f'Total score is {Game.score} points')
    
    def rolling_again(self):
        print(f'Rolling {Game.remaining_dice} dice...')
        roll = self.roller(Game.remaining_dice)
        print(','.join([str(i) for i in roll]))
        arr = list(roll)
        validate = Game.game.calculate_score(tuple([int(x) for x in arr]))
        if validate == 0:
            print('Zilch!!! Round over')
            print(f'You banked {validate} points in round {Game.round}')
            print(f'Total score is {Game.score} points')
            Game.round += 1
            Game.remaining_dice = 6
            print(f'Starting round {Game.round}')
            self.rolling_again()    
        else:   
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
                total = Game.game.calculate_score(tuple([int(x) for x in arr]))
                Game.to_shelf += total
                self.valid_cases(arr)




if __name__ == '__main__':
    game = Game()
    game.play()
