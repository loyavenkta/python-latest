# Dunder Method __init__
class Monster:
    health = 90
    energy = 40
    def __init__(self,health,energy):
        print("The Monster was created")
        self.health = health
        self.energy = energy
    def __len__(self):
        return self.energy
    def __abs__(self):
        return self.energy


    
    
    
    
    
    
    def attack(monster,amount):
        print("The monster has attack")
        print(f"{amount} damage was dealt")
        print(monster.energy)

    def move(koushik,speed):
        print(f'It has a speed of {speed}')
        print(monster.health)

monster1 = Monster(10,20)
print(len(monster1))
print(abs(monster1))
"""monster2 = Monster(40,50)
print(monster1.health)
print(monster2.health)"""