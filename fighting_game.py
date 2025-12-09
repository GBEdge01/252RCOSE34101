import random

class enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.is_depending = False
        self.has_depended = False

    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        self.has_depended = False
        self.is_depending = False
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")
    
    def depend(self):
        if self.has_depended == True:
            self.has_depended = False
            print(f"{self.name} fails to depend!")
        else:
            self.is_depending = True
            print(f"{self.name} is guarding!")
        
class player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power        
        self.is_depending = False
        self.has_depended = False

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        self.has_depended = False
        self.is_depending = False
        damage = random.randint(1, self.attack_power)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        
    def depend(self):
        if self.has_depended == True:
            self.has_depended = False
            print(f"{self.name} fails to depend!")
        else:
            self.is_depending = True
            print(f"{self.name} is guarding!")
      
      
      
MyChar = player("Hero", 100, 20)
MyEnemy = enemy("Goblin", 50, 15)
  
  
  
while MyChar.is_alive():
    a = input("Choose your action: (A)ttack or (D)epend: ").strip().upper()
    if a == 'D':
        MyChar.depend()
    elif a == 'A':
        MyChar.is_depending = False
        MyChar.has_depended = False
        if MyEnemy.is_depending:
            MyEnemy.is_depending = False
            print(f"{MyEnemy.name} blocks the attack from {MyChar.name}!")
        else:
            MyChar.attack(MyEnemy)
    else:
        print("Invalid action. Please choose 'A' or 'D'.")
        continue
    if MyEnemy.is_alive():
        b = random.choice(['A', 'D'])
        if b == 'D':
            MyEnemy.depend()
        else:
            MyEnemy.is_depending = False
            MyEnemy.has_depended = False
            if MyChar.is_depending:
                MyChar.is_depending = False
                print(f"{MyChar.name} blocks the attack from {MyEnemy.name}!")
            else:
                MyEnemy.attack(MyChar)
    else:
        print(f"{MyEnemy.name} has been defeated!")
        exit()
    print(f"{MyChar.name} Health: {MyChar.health}, {MyEnemy.name} Health: {MyEnemy.health}\n")