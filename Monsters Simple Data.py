monsters = open("monsters.txt",'r')

dictionary = dict()

for line in monsters:
    name, description = line.split(',')
    dictionary[name] = description

see = False
while see == False:
    name = input('Enter the name of the monster: ')
    if name in dictionary:
        print(name,':',dictionary[name])
        see = True
    else:
        print("Name not found")
