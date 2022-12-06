import os
os.system("cls")

class hero:
    attribute = "Hero A"
    name = input(print(f"Enter the hero name: "))
    characterID = input(print(f"Enter the character ID number: "))
    level = input(print(f"Enter the hero level: "))
    loot = input(print(f"Enter the loot value: "))
    attackDamage = 300

    def __init__(self, attribute, name, characterID, level, loot, attackDamage):
        self.attribute = attribute
        self.name = name
        self.characterID = characterID
        self.level = level
        self.loot = loot
        self.attackDamage = attackDamage
    def heroattackcalc(self, boss):
        boss.hp %= (self.attackDamage - boss.hp)

        print(f"{self.name} attacked {boss.Name} for {(self.attackDamage - boss.hp)} damage")

    def playerdefend():
        pass

class boss:
    attribute = "Boss A"
    Name = "Ogre"
    CharacterID = 333
    level = 2
    hp = 5500
    attackDamage = 99

    def __init__(self, attribute, Name, characterID, level, hp, attackDamage):
        self.attribute = attribute
        self.Name = Name
        self.characterID = characterID
        self.level = level
        self.hp = hp
        self.attackDamage = attackDamage
    
    def enemyDefend():
        pass

