class Monster:
    def __init__(self,health,energy,**kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

        self._id = 5

    def attack(self,amount):
        print("Ht monster has attacked")
        print(f"The anmount of damage {amount}")
    def move(self,speed):
        print("THe monster has move")
        print(f"It has move {speed}")

monster = Monster(20,10)
# private attribute
print(monster._id)
# hasattr and setattr
print(hasattr(monster,'health'))
# setattr
print(setattr(monster,'weapon',"Sword"))
