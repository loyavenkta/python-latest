class Monster:
    def __init__(self,health,energy,**kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self,amount):
        print("Ht monster has attacked")
        print(f"The anmount of damage {amount}")
    def move(self,speed):
        print("THe monster has move")
        print(f"It has move {speed}")
class Fish:
    def __init__(self,speed,has_scales):
        self.speed =speed
        self.has_scales = has_scales

    def swim(self):
        print(f"The fish has swimming of {self.spee}")

class Shark(Monster,Fish):
    def __init__(self,bite_strength,health,energy,speed,has_scales):
        self.bite_strength = bite_strength
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales )

shark = Shark(bite_strength= 50, health = 200, energy =55, speed =120, has_scales = True)
#print(Shark.mro())
shark.attack(10)
print(shark.health)
print(shark.energy)
print(shark.bite_strength)
print(shark.has_scales)