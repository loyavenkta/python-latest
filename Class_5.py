class Monster:
    def __init__(self,health):
        self.health = health
    def get_damage(self,amount):
        self.health -= amount


class hero:
    def __init__(self,damage,monster):
        self.damage = damage
        self.monster = monster
    def attack(self):
        self.monster.get_damage(self.damage)

monster = Monster(health = 50)
game = hero( damage = 20, monster = monster)
print(monster.health)
game.attack()
print(monster.health)



"""print(game.damage)
print(game.monster)"""