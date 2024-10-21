import random
class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.health = 0
        self.experience = 0

    def print_basics(self):
        print("Name: ",self.name)
        print("Attack: ",self.attack)
        print("Defence",self.defence)
        print("Health: ",self.health)
        print("Experience: ",self.experience)

    def print_me(self):
        self.print_basics()

    def print_plot(self):
        print("Once upon a time, there was a princess...")

class wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 100

    def print_me(self):
        self.print_basics()
        print("Magic: ",self.magic)

class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = random.randint(0,100)

    def setter(self,name):
        self.name = name
        self.attack = random.randint(0,100)
        self.defence = random.randint(0,100)
        self.__health = random.randint(0,100)
        self.experience = random.randint(0,100)

    def health_getter(self):
        return self.__health

    def print_me(self):
        self.print_basics()
        print("Armour: ",self.armour)

Chandler = knight()
Chandler.setter("Chandler")
Chandler.print_me()
print("Health: ",Chandler.health_getter())
