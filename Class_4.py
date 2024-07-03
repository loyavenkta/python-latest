def update_energy(amount):
    monster.energy  += amount 



class Monster:
    def __init__(self,energy,health):
        self.health = health
        self.energy = self.set_energy(energy)
    def update_health(self, amount):
        self.health += amount

    def set_energy(self,energy):
        new_energy = energy*2
        return new_energy





monster = Monster(health =20,energy = 25)
#update_energy(60)
print(monster.energy)

monster.update_health(40)
print(monster.health)


"""monster.health += 35
print(monster.energy)
print(monster.health)"""