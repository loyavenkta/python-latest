class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
    def move(self,speed):
        print("THe monster has move")
        print(f"It has move {speed}")

class Scorpion(Monster):
    def __init__(self,poison_damage,scorpion_health,scorpion_energy):
        self.poison_damage = poison_damage
        super().__init__(health =  scorpion_health,energy = scorpion_energy)
    def attack(self):
        print("scorpion attacked")
        print(f"it has damge{self.poison_damage}")


scorpion = Scorpion(poison_damage=50, scorpion_energy=34, scorpion_health=22)
scorpion.attack()
scorpion.move(5)
print(scorpion.health)
print(scorpion.energy)