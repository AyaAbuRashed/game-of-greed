from game_of_greed.game_logic import GameLogic,Banker

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    def play(self):
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
            round = 1
            remaining_dice = 6
            score = 0
            to_shelf = 0
            rolling_again = True
            while score < 10000 and rolling_again == True:
                print(f'Starting round {round}')
                # print(remaining_dice)
                while rolling_again == True:
                    print(f'Rolling {remaining_dice} dice...')
                    roll = self.roller(remaining_dice)
                    print(','.join([str(i) for i in roll]))
                    dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                    if dice_to_keep == 'q':
                        print(f'Total score is {score} points')
                        print(f'Thanks for playing. You earned {score} points')
                        rolling_again = False
                    else :
                        arr = dice_to_keep.split(",")
                        saved = [int(x) for x in arr]
                        game = GameLogic()
                        banker = Banker()
                        to_shelf += game.calculate_score(tuple(saved))
                        print(f'You have {to_shelf} unbanked points and 5 dice remaining')
                        next_step = input('(r)oll again, (b)ank your points or (q)uit ')
                        if next_step == 'b':
                            banker.shelf(to_shelf)
                            banked = banker.bank()
                            to_shelf = 0
                            score += banked
                            print(f"You banked {banked} points in round {round}")
                            round += 1
                            print(f'Total score is {score} points')
                            break
                        elif next_step == 'q':
                            print(f'Total score is {score} points')
                            print(f'Thanks for playing. You earned {score} points')
                            rolling_again = False
                        elif next_step == 'r':
                           to_shelf += banker.shelved
                           remaining_dice = remaining_dice - 1
                           rolling_again = True




if __name__ == '__main__':
    game = Game()
    game.play()
