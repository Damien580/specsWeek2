class Superhero:
    def __init__(self, name, alias, health, power, weakness):
        self.name = name
        self.alias = alias
        self. health = health
        self.power = power
        self.weakness = weakness
        
    def punch(self, enemy):
        enemy.health -= self.power
        enemy.check_if_dead()
        
    def check_if_dead(self):
        if self.health <= 0:
            print("RIP")
        else:
            print("ALIVE!")

superman = Superhero("Superman", "Clark Kent", 1000, 100, "Kryptonite")
batman = Superhero("Batman", "Bruce Wayne", 100, 25, "No Parents")

print(superman.name)
print(superman.weakness)

print(batman.name)
print(batman.weakness)
