import sys
from datetime import datetime
from . import room

class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = ("Rusty dagger", 1)
        self.armor = ("", 0)
        self.inventory = ["Rusty dagger"]
        self.gold = 0

        self.max_health = (10 + self.armor[1])
        self.health = self.max_health
        self.damage = self.weapon[1]
        self.enemies_killed = 0
        
        self.enemy_counter = 2
        self.current_room = room.start_room
        self.start_time = datetime.now()
        self.end_time = 0
        self.total_time = 0

    
    def strike(self, enemy, enemy_move):
        if enemy_move == "block":
            self.health -= enemy.damage
            if enemy.name == "Boss":
                print("The boss blocked the strike and slammed you!")
            else:
                print("The enemy blocked the strike and hit you!")
            print(f'\n! You took {enemy.damage} damage !')
        elif enemy_move == "charge":
            enemy.health -= self.damage
            if enemy.name == "Boss":
                print("The boss tried charging but you swept their feet!")
                print(f'\n* The boss took {self.damage} damage *')
            else:
                print("The enemy tried charging but you struck them down!")
                print(f'\n* The enemy took {self.damage} damage *')
            if enemy.health > 0:
                if enemy.name == "Boss":
                    print(f'- The boss has {enemy.health}/{enemy.max_health} health -')
                else:
                    print(f'- The enemy has {enemy.health}/{enemy.max_health} health -')
        elif enemy_move == "strike":
            if enemy.name == "Boss":
                print("\nThe boss striked as well! Your weapons clashed!")
            else:
                print("\nThe enemy striked as well! Your weapons clashed!")
        
        if self.health <= 0:
            self.death()
        
            
        
    def block(self, enemy, enemy_move):
        if enemy_move == "charge":
            self.health -= enemy.damage
            if enemy.name == "Boss":
                print("The boss charged through your defense!")
            else:
                print("The enemy charged through your defense!")
            print(f'\n! You took {enemy.damage} damage !')
        elif enemy_move == "strike":
            enemy.health -= self.damage
            if enemy.name == "Boss":
                print("You blocked the enemy boss strike and counter-attacked!")
                print(f'\n* The boss took {self.damage} damage *')
            else:
                print("You blocked the enemy strike and counter-attacked!")
                print(f'\n* The enemy took {self.damage} damage *')
            if enemy.health > 0:
                if enemy.name == "Boss":
                    print(f'- The boss has {enemy.health}/{enemy.max_health} health -')
                else:
                    print(f'- The enemy has {enemy.health}/{enemy.max_health} health -')
        elif enemy_move == "block":
            print("\nYou both blocked!")

        if self.health <= 0:
            self.death()
        


    def charge(self, enemy, enemy_move):
        if enemy_move == "strike":
            self.health -= enemy.damage
            if enemy.name == "Boss":
                print("You charged the boss but they struck you down!")
            else:
                print("You charged the enemy but they struck you down!")
            print(f'\n! You took {enemy.damage} damage !')
        elif enemy_move == "block":
            enemy.health -= self.damage
            if enemy.name == "Boss":
                print("The boss tried blocking but you charged through!")
                print(f'\n* The boss took {self.damage} damage *')
            else:
                print("The enemy tried blocking but you charged through!")
                print(f'\n* The enemy took {self.damage} damage *')
            if enemy.health > 0:
                if enemy.name == "Boss":
                    print(f'- The boss has {enemy.health}/{enemy.max_health} health -')
                else:
                    print(f'- The enemy has {enemy.health}/{enemy.max_health} health -')
        elif enemy_move == "charge":
            print("\nYou charged at each other, but missed!")

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
        print("\n* You have been healed to full health! *")
        print(f'\nYou now have {self.health}/{self.max_health} health')
    
    def update_weapon(self, new_weapon):
        self.inventory.remove(self.weapon[0])
        self.weapon = new_weapon
        self.damage = self.weapon[1]
        self.inventory.insert(0, self.weapon[0])
        print(f'\nYour damage increased to {self.damage}!')

    def update_armor(self, new_armor):
        if self.armor[0] in self.inventory:
            self.inventory.remove(self.armor[0])
        self.health += (new_armor[1] - self.armor[1])
        self.armor = new_armor
        self.inventory.insert(1, self.armor[0])
        self.max_health = (10 + self.armor[1])
        
        print(f'\nYour max health increased to {self.max_health}!')
        print(f'You curently have {self.health}/{self.max_health} health')

    def add_inventory(self, item):
        self.inventory.append(item)

    def display_gold(self):
        print(f'\nYou now have {self.gold} gold!')
    
    def victory(self):
        self.end_time = datetime.now()
        self.total_time = (self.end_time - self.start_time)
        total_seconds = self.total_time.total_seconds()
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds - int(total_seconds)) * 1000)

        print("\n--- Congratulations! You have mastered the dungeon and successfully escaped! ---")
        print(f"\n-- Here are your ending stats: --\n     * Runtime: {minutes:02d}:{seconds:02d}.{milliseconds:03d} *\n     * Health: {self.health}/{self.max_health}      *\n     * Gold: {self.gold}            *\n     * Enemies killed: {self.enemies_killed}  *\n")
        input('~ Press any key to continue ~')
       
        print("\nThis was my first Python project, created by me (Mason Munoz).")
        print("I created this game to sharpen my Python skills and specifically, object-oriented programming.")
        print("No AI was used in its creation--hence, the bugs that probably still exist.")
        print("\n--- Thanks for playing! ---")
        input()
        sys.exit()


    





