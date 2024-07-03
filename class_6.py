class Monster:
    health =20
    energy = 20
    """def _init__(self,health,energy):
        self.health = health
        self.energy = energy"""

    def attack(self,amount):
        print("the monster is attacked")
        print(f"{amount}damage was dealth")
        self.energy -= 20
    
    def move(self,speed):
        print("The monster moved")
        print(f"It has a speed of {speed}")

class Shark(Monster):
     def __init__(self,speed):
       self.speed = speed
    def bite(self):
        print("The shark has bitten")

    def move(self):
        print("The shark has moved")
        print(f'the speed of the shark is {self.speed}')

shark = Shark(speed = 120, health = 100, energy = 80)
shark.attack(20)

