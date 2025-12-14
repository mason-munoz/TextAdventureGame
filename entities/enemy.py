import random

class Enemy:
    def __init__(self):
        self.health = 5
        self.damage = 1

    def random_move(self):
        selector = random.randrange(1, 4)
        if selector == 1:
            return "strike"
        elif selector == 2:
            return "block"
        elif selector == 3:
            return "charge"

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.damage = 3
        self.special_move = "sweep"