import sys
from . import room

class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = ("Rusty dagger", 1)
        self.armor = ("", 0)
        self.inventory = ["Rusty dagger"]
        self.gold = 0
        self.map = False
        self.torch = False
        self.key = False

        self.max_health = (10 + self.armor[1])
        self.health = self.max_health
        self.damage = self.weapon[1]
        
        self.enemy_counter = 2
        self.current_room = room.start_room

    
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
            print(f'Your {self.gold} coins spill out across the dungeon floor')
        if self.gold == 1:
            print(f'Your one measly coin clanks out across the dungeon floor')
        if self.gold < 1:
            print("Skeletons surround you and laugh at your pathetic, penniless corpse")
        sys.exit()
    
    def explore(self):
        output = ""
        for x in self.current_room.directions.keys():
            output += f'- {x}\n'
        return output
    
    def heal(self):
        self.health = self.max_health
        print("* You have been healed to full health! *")
        print(f'You now have {self.health}/{self.max_health} health\n')
    
    def update_weapon(self, new_weapon):
        self.inventory.remove(self.weapon[0])
        self.weapon = new_weapon
        self.damage = self.weapon[1]
        self.inventory.insert(0, self.weapon[0])
        print(f'\nYour damage increased to {self.damage}!\n')

    def update_armor(self, new_armor):
        if self.armor[0] in self.inventory:
            self.inventory.remove(self.armor[0])
        self.health += (new_armor[1] - self.armor[1])
        self.armor = new_armor
        self.inventory.insert(1, self.armor[0])
        self.max_health = (10 + self.armor[1])
        
        print(f'\nYour max health increased to {self.max_health}!')
        print(f'You curently have {self.health}/{self.max_health} health\n')

    def add_inventory(self, item):
        self.inventory.append(item)

    def display_gold(self):
        print(f'\nYou now have {self.gold} gold!')

    





