class Monster:
    health = 90
    energy = 40


    def attack(monster,amount):
        print("The monster has attack")
        print(f"{amount} damage was dealt")
        print(monster.energy)

    def move(koushik,speed):
        print(f'It has a speed of {speed}')
        print(monster.health)


monster = Monster()
monster.attack(40)
monster.move(10)
