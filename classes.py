import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(0, self.attack_power)
        opponent.health = max(opponent.health - damage, 0)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        if self.health == self.max_health:
            print(f"{self.name} is already at full health!")
            return
        heal_amount = min(5, self.max_health - self.health)
        self.health += heal_amount
        print(f"{self.name} regenerates {heal_amount} health! Current health: {self.health}/{self.max_health}")


# Warrior class (inherits from Character)
class Grunter(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25) 

    def special_ability(self, opponent):
        print('\nSelect Special Ability')
        print('1. Smash Attack')
        print('2. Body Rage')

        abilities = {
            "1": self.smash_attack,
            "2": self.body_rage
        }
        abilities.get(input("Choose an action: "), self.smash_attack)(opponent)
    
    def smash_attack(self, opponent):
        opponent.health = max(opponent.health - 25, 0)
        opponent.attack_power = max(opponent.attack_power - 3, 2)
        print(f"{self.name} has unleashed the Smash Attack, reducing {opponent.name}'s health to {opponent.health} and their attack to {opponent.attack_power}")
    
    def body_rage(self, opponent):
        self.health = min(self.health + 5, 165)
        self.attack_power = min(self.attack_power + 5, 50)
        print(f"{self.name} has made their body feel more rage, leading to higher health ({self.health}) and a stronger attack ({self.attack_power})")

# Mage class (inherits from Character)
class Mofa(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  

    def special_ability(self, opponent):
        print('\nSelect Special Ability')
        print('1. Warp')
        print('2. Slam')

        abilities = {
            "1": self.warp,
            "2": self.slam
        }
        abilities.get(input("Choose an action: "), self.warp)(opponent)
    
    def warp(self, opponent):
        opponent.health = max(opponent.health - 25, 0)
        print(f"{self.name} has warped the body of {opponent.name}, reducing their health to {opponent.health}")
    
    def slam(self, opponent):
        opponent.health = max(opponent.health - 35, 0)
        opponent.attack_power = max(opponent.attack_power - 4, 3)
        print(f"{self.name} has slammed {opponent.name}, reducing their health to {opponent.health} and attack to {opponent.attack_power}")

# Archer class
class Geki(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=40)
    
    def special_ability(self, opponent):
        print('\nSelect Special Ability')
        print('1. Head Shot')
        print('2. Duqi Grenades')

        abilities = {
            "1": self.head_shot,
            "2": self.duqi_grenade
        }
        abilities.get(input("Choose an action: "), self.head_shot)(opponent)
        
    def head_shot(self, opponent):
        opponent.health = max(opponent.health - 40, 0)
        print(f"{self.name} has taken a head shot at {opponent.name}, lowering their health to {opponent.health}")
    
    def duqi_grenade(self, opponent):
        opponent.attack_power = max(opponent.attack_power - 5, 4)
        print(f"{self.name} has thrown a Duqi Grenade at {opponent.name}, lowering their attack to {opponent.attack_power}")

# Paladin class
class Medic(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)
    
    def special_ability(self, opponent):
        print('\nSelect Special Ability')
        print('1. Super Heal')
        print('2. Shield')

        abilities = {
            "1": self.super_heal,
            "2": self.shield
        }
        abilities.get(input("Choose an action: "), self.super_heal)()
    
    def super_heal(self):
        heal_amount = min(10, self.max_health - self.health)
        self.health += heal_amount
        print(f"{self.name} regenerates {heal_amount} health with their super heal ability! {self.name}'s current health is now {self.health}")
    
    def shield(self, opponent):
        opponent.attack_power = max(opponent.attack_power - 5, 4)
        print(f"{self.name} has unleashed their shield, reducing the strength of {opponent.name}'s attack to {opponent.attack_power}")

# EvilWizard class (inherits from Character)
class Feibang(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  
    
    def special_ability(self, opponent):
        self.regenerate()
    
    def regenerate(self):
        heal_amount = min(10, self.max_health - self.health)
        self.health += heal_amount
        print(f"{self.name} regenerates {heal_amount} health! Current health: {self.health}")
