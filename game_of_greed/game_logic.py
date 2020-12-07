from collections import Counter
import random

class GameLogic():
    # def __init__(self,value):
    #     self.value=value
    @staticmethod
    def calculate_score(diceRoll):
        score = 0
        counting = Counter(diceRoll)
        dice_count = counting.most_common()
        if len(dice_count) == 6 :
            score = 1500
            return score
            
        if len(dice_count) == 3 :
            if dice_count[0][1] == 2 and dice_count[1][1] == 2 and dice_count[2][1] == 2:
                score = 1500
                return score


        for x in dice_count:
            if x[1] < 3:
                if x[0] == 1:
                    score += x[1] *100
                elif x[0] == 5:
                    score += x[1] *50
         
            if x[1] == 3:
                if x[0] == 1:
                    score += 1000
                # elif x[0] == 5:
                #     score += 500
                else: 
                    score += x[0]*100
            if x[1] == 4:
                if x[0] == 1:
                    score += 2000
                else: 
                    score += x[0]*200
            if x[1] == 5:
                if x[0] == 1:
                    score += 3000
                else: 
                    score += x[0]*300 
            if x[1] == 6:
                if x[0] == 1:
                    score += 4000
                else: 
                    score += x[0]*400

        return score 

    @staticmethod
    def roll_dice(num):
        arr = [random.randint(1,6) for i in range(num)]
        return tuple(arr)

class Banker:

    def __init__(self):
        self.shelved = 0
        self.balance= 0
 
    def shelf(self,num):
        self.shelved += num
   
    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
                    


            
                
