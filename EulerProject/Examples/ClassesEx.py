import random


class Dice:

    def roll(self):
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)

        values = (dice_one, dice_two)
        return values


dice = Dice()
print(dice.roll())
