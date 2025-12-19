class MC():
    def __init__(self, name, klass, health, defense, strength, mana, speed, money, level, inv):
        self.klass = klass
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength
        self.mana = mana
        self.speed = speed
        self.money = money
        self.level = level
        self.inv = inv

    def stats(self):
        print("Your stats:")
        print(f"Name ~ {Name}")
        print(f"Class ~ {klass}")
        print(f"Health ~ {self.health*h}")
        print(f"Defense ~ {self.defense*d}")
        print(f"Strength ~ {self.strength*st}")
        print(f"Mana ~ {self.mana*mn}")
        print(f"Speed ~ {self.speed*spd}")
        print(f"Level ~ {self.level}")
        print(f"Money ~ {self.money}")
        print(f"Inventory ~ {self.inv}")
        
class enemy():
    def __init__(self, type, health, defense, strength, mana, speed, level):
        self.type = type
        self.klass = klass
        self.health = health
        self.defense = defense
        self.strength = strength
        self.mana = mana
        self.speed = speed
        self.level = level

    def fight(self, dead):
        dead = False
        EnSpd = 0
        YSpd = 0
        while dead == False:
            

CC = False
while CC == False:
    print("Classes:")
    print("A) Mage ~ 5x mana, 0.2x strength, 0.5x hp, 1x defense")
    print("B) Warrior ~ 0x mana, 2x strength, 2x hp, 2x defense, 1.5x speed")
    print("C) Tank ~ 3x hp, 3x defense, 0.5x speed")
    klass = input("Choose your class")
    if klass.lower() == "a":
        klass = "Mage"
        CC = True
    elif klass.lower() == "b":
        klass = "Warrior"
        CC = True
    elif klass.lower() == "c":
        klass = "Tank"
        CC = True
    else:
        print("Please type A, B, or C to select class.")
CC = False
if klass == "Mage":
    h = 0.5
    d = 1
    st = 0.2
    mn = 5
    spd = 1
    weapon = "Rusty Scepter"
if klass == "Warrior":
    h = 1.5
    d = 1.5
    st = 1.5
    mn = 0
    spd = 1.5
    weapon = "Dull Blade"
if klass == "Tank":
    h = 3
    d = 3
    st = 1
    mn = 1
    spd =0.5
    weapon = "Huge Old Hammer"
print(f"Okay, your class is {klass}")
Name = input("Choose your name")
print(f"Okay, your name is {Name}")

you = MC(Name, klass, 100, 10, 10, 10, 10, 0, 1, [])
you.stats()
print("You wake up to an empty house, your wife and kids have been stolen by the corrupt government")
print("Your main mission: Save your wife and kids by adventuring out and confronting Bart, the king")
print(f"Now, you go to your friend's home, and they give you a {weapon} to help you on this journey")
FE = input("As you now venture out into the plains, you encounter a green goblin by a chest, do you fight (a) or flee (b)?")
while CC == False:
    if FE.lower() != "a" or "b":
        print("Invalid Option!")
    elif FE.lower == "a":
        print("placeholderfight")
        Gob.fight()
    else:
        print("You fled for saftey, you coward!")












