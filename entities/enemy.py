import random

class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.max_health = 5
        self.health = 5
        self.damage = 1
    
    def reveal_move(self):
        selector = random.randrange(1, 4)
        if selector == 1:
            return ("strike", "\nThe enemy raises their weapon...")
        elif selector == 2:
            return ("block", "\nThe enemy braces themself...")
        elif selector == 3:
            return ("charge", "\nThe enemy takes a few steps back...")
    
    def battle(self, player):
        print("\n! You have encountered a wild enemy !")
        while True:
            reveal = self.reveal_move()
            random_reveal = random.random()
            if random_reveal < 0.5:
                print(reveal[1])
            
            if "Health Potion" in player.inventory and (player.health < player.max_health):
                battle = input(f'\nYou have {player.health} health! What would you like to do?\n - Strike (s)\n - Block (b)\n - Charge (c)\n - Drink health potion (h)\n').lower().strip()
            else:
                battle = input(f'\nYou have {player.health} health! What would you like to do?\n - Strike (s)\n - Block (b)\n - Charge (c)\n').lower().strip()

            if (battle == "strike") or (battle == "s"):
                print("\n")
                player.strike(self, reveal[0])

                
            elif (battle == "block") or (battle == "b"):
                print("\n")
                player.block(self, reveal[0])

            
            elif (battle == "charge") or (battle == "c"):
                print("\n")
                player.charge(self, reveal[0])
            
            elif (player.health < player.max_health) and (battle == "drink" or battle == "drink health potion" or battle == "h") and "Health Potion" in player.inventory:
                player.heal()
                player.inventory.remove("Health Potion")
            
            if self.health <= 0:
                    print(f'\n-- You have killed the enemy! --\n  * You gained 1 gold! *\n')
                    player.enemy_counter -= 1
                    player.enemies_killed += 1
                    player.gold += 1
                    print(f'You now have {player.gold} gold!')
                    break

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Boss"
        self.max_health = 12
        self.health = 12
        self.damage = 3
        self.alive = True
        self.special_move = "sweep"
    
    def reveal_move(self):
        selector = random.randrange(1, 4)
        if selector == 1:
            return ("strike", "\nThe boss raises their weapon...")
        elif selector == 2:
            return ("block", "\nThe boss braces themself...")
        elif selector == 3:
            return ("charge", "\nThe boss takes a few steps back...")
    
    def battle(self, player):
        print("\n! Out of the shadows, the dungeon boss trudges towards you !")
        while True:
            reveal = self.reveal_move()
            random_reveal = random.random()
            if random_reveal < 0.5:
                print(reveal[1])
            
            if "Health Potion" in player.inventory:
                battle = input(f'\nYou have {player.health} health! What would you like to do?\n - Strike (s)\n - Block (b)\n - Charge (c)\n - Drink health potion (h)\n').lower().strip()
            else:
                battle = input(f'\nYou have {player.health} health! What would you like to do?\n - Strike (s)\n - Block (b)\n - Charge (c)\n').lower().strip()

            if (battle == "strike") or (battle == "s"):
                print("\n")
                player.strike(self, reveal[0])

                
            elif (battle == "block") or (battle == "b"):
                print("\n")
                player.block(self, reveal[0])

            
            elif (battle == "charge") or (battle == "c"):
                print("\n")
                player.charge(self, reveal[0])
            
            elif (battle == "drink" or battle == "drink health potion" or battle == "h") and "Health Potion" in player.inventory:
                player.heal()
                player.inventory.remove("Health Potion")
            
            if self.health <= 0:
                    print(f'\n   -- You have killed the boss! --\n  * A golden key drops into your hands *\n')
                    player.inventory.append("Key")
                    self.alive = False
                    break