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

class wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 50

    def setter(self,name):
        self.name = name
        self.attack = 10
        self.defence = 10
        self.health = 30
        self.experience = 90

    def print_me(self):
        self.print_basics()
        print("Magic: ",self.magic)

class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = 50

    def setter(self,name):
        self.name = name
        self.attack = 30
        self.defence = 50
        self.health = 80
        self.experience = 30

    def print_me(self):
        self.print_basics()
        print("Armour: ",self.armour)

class archer(Character):
    def __init__(self):
        Character.__init__(self)
        self.arrow = 30

    def setter(self,name):
        self.name = name
        self.attack = 40
        self.defence = 20
        self.health = 50
        self.experience = 60

    def print_me(self):
        self.print_basics()
        print("Arrow: ",self.arrow)

user_name = input("Enter your name: ")
user_character = input("Enter the character you want to play Wizard(w) / Knight(k) / archer (a): ").lower()

opponent_type = random.randint(1,3)
if opponent_type == 1:
    opponent = wizard()
    opponent.setter("Gandolf")
    print("Your opponent is: WIZARD")
    opponent.print_me()
elif opponent_type == 2:
    opponent = knight()
    opponent.setter("Arthur")
    print("Your opponent is: KNIGHT")
    opponent.print_me()
else:
    opponent = archer()
    opponent.setter("Robinhood")
    print("Your opponent is: ARCHER")
    opponent.print_me()

print('\n')

if user_character == 'w':
    user_character = wizard()
    user_character.setter(user_name)
    print("You are: WIZARD")
    user_character.print_me()
    print('\n')
    if opponent_type == 1:
        print("Tie Game")
    elif opponent_type == 2:
        print("Your attack is 10 damage")
        print("Your magic can cause 50 damage")
        print("Because your opponent has an armour, magic power times by 4")
        print("Your attack is 210, your opponent health is 180")
        print("You attacked, opponent dies")
        print("You win!")
    else:
        print("Your attack is 10")
        print("Your magic is 50")
        print("Because your opponent doesn't have an armour, nothing changed")
        print("Your attack is 60, your opponent health is 70")
        print("You attacked, opponent health remains 10")
        print("Opponent attack is 40 damage")
        print("Opponent arrow can cause 30 damage")
        print("Opponent attack is 70, your health is 40")
        print("Opponent attacked, you die")
        print("You lost...")
elif user_character == 'k':
    user_character = knight()
    user_character.setter(user_name)
    print("You are: KNIGHT")
    user_character.print_me()
    print('\n')
    if opponent_type == 1:
        print("Your attack is 30 damage")
        print("Your armour can cause 50 damage")
        print("Because your opponent has magic, your armour can't harm him")
        print("Your attack is 30, your opponent health is 40")
        print("You attacked, opponent health remains 10")
        print("Opponent attack is 10 damage")
        print("Your opponent magic can cause 50 damage")
        print("Because you have an armour, your opponent magic power times by 4")
        print("Opponent attack is 210, your health is 180")
        print("Opponent attacked, you die")
        print("You lost...")
    elif opponent_type == 2:
        print("Tie Game")
    else:
        print("Your attack is 30 damage")
        print("Your armour can cause 50 damage")
        print("Your attack is 80, your opponent health is 70")
        print("You attacked, opponent dies")
        print("You win!")
elif user_character == 'a':
    user_character = archer()
    user_character.setter(user_name)
    print("You are: ARCHER")
    user_character.print_me()
    print('\n')
    if opponent_type == 1:
        print("Your attack is 40")
        print("Your arrow can cause 30 damage")
        print("Your attack is 70, your opponent health is 40")
        print("You attacked, opponent dies")
        print("You win!")
    elif opponent_type == 2:
        print("Your attack is 40")
        print("Your arrow can cause 30 damage")
        print("Because your opponent has an armour")
        print("Your attack is 70, your opponent health is 180")
        print("Your attacked, opponent health remains 110")
        print("Opponent attack is 30 damage")
        print("Your opponent armour can cause 50 damage")
        print("Opponent attack is 80, your health is 70")
        print("Opponent attacked, you die")
        print("You lost...")
    else:
        print("Tie Game")
else:
    print("Error, input not found.")
