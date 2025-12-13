import random
from . import enemy
from . import merchant

class Room():
    def __init__(self, name):
        self.name = name
        self.treasure = False
        self.enemy = False
        self.nothing = False
        self.directions = None

        rng = random.random()
        if rng < 0.3:
            self.treasure = True
        elif rng < 0.5:
            self.enemy = True
        else:
            self.nothing = True

class BossRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = False

        self.name = "Boss Room"
        self.boss = enemy.Boss
        self.directions = {"E": room4}

class StartRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = True

        self.name = "Start Room"
        self.directions = {"N": room8}
        

class MerchantRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = False

        self.name = "Merchant Room"
        self.directions = {"W": room6}

class ExitRoom():
    def __init__(self):
        self.enemy = False
        self.treasure = False
        self.nothing = False

        self.name = "Exit Room"
        self.directions = {"S": room2}
        self.description = "A heavy wooden door stands before you with light piercing through the cracks."


room1 = Room("room1")
room2 = Room("room2")
room3 = Room("room3")
room4 = Room("room4")
room5 = Room("room5")
room6 = Room("room6")
room7 = Room("room7")
room8 = Room("room8")
room9 = Room("room9")
start_room = StartRoom()
boss_room = BossRoom()
merchant_room = MerchantRoom()
exit_room = ExitRoom()

room1.directions = {"E":room2, "S":room4}
room2.directions = {"N":exit_room, "E":room3, "S":room5, "W":room1}
room3.directions = {"S":room6, "W":room2}
room4.directions = {"N":room1, "E":room5, "S":room7, "W":boss_room}
room5.directions = {"N":room2, "E":room6, "S":room8, "W":room4}
room6.directions = {"N":room3, "E":merchant_room, "S":room9, "W":room5}
room7.directions = {"N":room4, "E":room8}
room8.directions = {"N":room5, "E":room9, "S":start_room, "W":room7}
room9.directions = {"N":room6, "W":room8}
