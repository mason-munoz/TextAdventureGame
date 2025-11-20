import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.damage = 1
        self.gold = 0
        self.inventory = ["Rusty dagger"]

    
    def strike(self, enemy):
        enemy_move = enemy.random_move()
        if enemy_move == "block":
            self.health -= enemy.damage
            print("The enemy blocked the strike and hit you!")
            print(f'* You took {enemy.damage} damage *\n')
        elif enemy_move == "charge":
            enemy.health -= self.damage
            print("The enemy tried charging but you struck them down!")
            print(f'* The enemy took {self.damage} damage *\n')
        elif enemy_move == "strike":
            print("The enemy striked as well! Your weapons clashed!\n")
        
        if self.health <= 0:
            self.death()
        
            
        
    def block(self, enemy):
        enemy_move = enemy.random_move()
        if enemy_move == "charge":
            self.health -= enemy.damage
            print("The enemy charged through your defense!")
            print(f'* You took {enemy.damage} damage *\n')
        elif enemy_move == "strike":
            enemy.health -= self.damage
            print("You blocked the enemy strike and counter-attacked!")
            print(f'* The enemy took {self.damage} damage *\n')
        elif enemy_move == "block":
            print("You both blocked!\n")

        if self.health <= 0:
            self.death()
        


    def charge(self, enemy):
        enemy_move = enemy.random_move()
        if enemy_move == "strike":
            self.health -= enemy.damage
            print("You charged the enemy but they struck you down!")
            print(f'* You took {enemy.damage} damage *\n')
        elif enemy_move == "block":
            enemy.health -= self.damage
            print("The enemy tried blocking but you charged through!")
            print(f'* The enemy took {self.damage} damage *\n')
        elif enemy_move == "charge":
            print("You charged at each other, but missed!\n")

        if self.health <= 0:
            self.death()
        


    def check_inventory(self):
        print(f'\n{self.name}\'s inventory: ')
        for item in self.inventory:
            print(f'- {item}')
        print(f'- {self.gold} gold')

    
    def death(self):
        print("You have died!")
        if self.gold > 1:
            print(f'* Your {self.gold} coins spill out across the dungeon floor *')
        if self.gold == 1:
            print(f' * Your one measly coin clanks out across the dungeon floor *')
        if self.gold < 1:
            print("* Skeletons surround you and laugh at your pathetic, penniless corpse *")
        sys.exit()


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



