import random
from . import enemy

class Room():
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.treasure = False
        self.enemy = False
        self.nothing = True
        self.directions = None


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


def fill_rooms():
    empty_room_list = [rm for rm in room_list if rm.nothing]
    for x in range(2):
        enemy_room = random.choice(empty_room_list)
        enemy_room.enemy = True
        enemy_room.nothing = False
        empty_room_list.remove(enemy_room)
    treasure_room = random.choice(empty_room_list)
    treasure_room.treasure = True
    treasure_room.nothing = False
    empty_room_list.remove(treasure_room)

def enemy_reset(player):
    empty_room_list = [rm for rm in room_list if rm.nothing and rm is not player.current_room] # "is not" compares identity
    for x in range(2):
        enemy_room = random.choice(empty_room_list)
        enemy_room.enemy = True
        enemy_room.nothing = False
        empty_room_list.remove(enemy_room)
    player.enemy_counter = 2


room1 = Room("room1", "1")
room2 = Room("room2", "2")
room3 = Room("room3", "3")
room4 = Room("room4", "4")
room5 = Room("room5", "5")
room6 = Room("room6", "6")
room7 = Room("room7", "7")
room8 = Room("room8", "8")
room9 = Room("room9", "9")
start_room = StartRoom()
boss_room = BossRoom()
merchant_room = MerchantRoom()
exit_room = ExitRoom()
room_list = [room1, room2, room3, room4, room5, room6, room7, room8, room9]

room1.directions = {"E":room2, "S":room4}
room2.directions = {"N":exit_room, "E":room3, "S":room5, "W":room1}
room3.directions = {"S":room6, "W":room2}
room4.directions = {"N":room1, "E":room5, "S":room7, "W":boss_room}
room5.directions = {"N":room2, "E":room6, "S":room8, "W":room4}
room6.directions = {"N":room3, "E":merchant_room, "S":room9, "W":room5}
room7.directions = {"N":room4, "E":room8}
room8.directions = {"N":room5, "E":room9, "S":start_room, "W":room7}
room9.directions = {"N":room6, "W":room8}

fill_rooms()