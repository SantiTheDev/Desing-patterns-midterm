# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from BlueSidedRaces import *
from RedSidedRaces import *
from Jobs import *
from IFicha import *


def sideDiceder() -> int:
    print("Choose side"
          "1. blue  2. red ")
    option = int(input())
    return option


def raceDicider(side):
    if int(side) == 1:
        print("Choose race\n"
              "1. Human\n"
              "2. Gnome\n"
              "3. Drwaf\n"
              "4. Dark Elf\n")
        option = int(input())
        return option
    else:
        print("Choose race\n"
              "1. Orc\n"
              "2. Undead\n"
              "3. Tauren\n"
              "4. Undead\n")
        option = int(input())
        return option

def jobDecider():
    print("choose the job\n"
          "1. Rouge\n"
          "2. Warrior\n"
          "3. Mage\n"
          "4. Paladin\n"
          "5. Warlock\n")
    option = int(input())
    return option


def createBlueSide(race, job):
    name = input("Give a name to your character")
    if race == 1:
        if job == 1: return Human(name, Rogue())
        elif job == 2: return Human(name, Warrior())
        elif job == 3: return Human(name, Mage())
        elif job == 4: return Human(name, Paladin())
        elif job == 5: return Human(name, Warklock())
    if race == 2:
        if job == 1: return Drawf(name, Rogue())
        elif job == 2: return Drawf(name, Warrior())
        elif job == 3: return Drawf(name, Mage())
        elif job == 4: return Drawf(name, Paladin())
        elif job == 5: return Drawf(name, Warklock())
    if race == 3:
        if job == 1: return Gnome(name, Rogue())
        elif job == 2: return Gnome(name, Warrior())
        elif job == 3: return Gnome(name, Mage())
        elif job == 4: return Gnome(name, Paladin())
        elif job == 5: return Gnome(name, Warklock())
    if race == 4:
        if job == 1: return DarkElf(name, Rogue())
        elif job == 2: return DarkElf(name, Warrior())
        elif job == 3: return DarkElf(name, Mage())
        elif job == 4: return DarkElf(name, Paladin())
        elif job == 5: return DarkElf(name, Warklock())


def createRedSide(race, job):

    name = input("Give a name to your character")
    if race == 1:
        if job == 1:
            return Orc(name, Rogue())
        elif job == 2:
            return Orc(name, Warrior())
        elif job == 3:
            return Orc(name, Mage())
        elif job == 4:
            return Orc(name, Paladin())
        elif job == 5:
            return Orc(name, Warklock())
    if race == 2:
        if job == 1:
            return Undead(name, Rogue())
        elif job == 2:
            return Undead(name, Warrior())
        elif job == 3:
            return Undead(name, Mage())
        elif job == 4:
            return Undead(name, Paladin())
        elif job == 5:
            return Undead(name, Warklock())
    if race == 3:
        if job == 1:
            return Tauren(name, Rogue())
        elif job == 2:
            return Tauren(name, Warrior())
        elif job == 3:
            return Tauren(name, Mage())
        elif job == 4:
            return Tauren(name, Paladin())
        elif job == 5:
            return Tauren(name, Warklock())
    if race == 4:
        if job == 1:
            return Troll(name, Rogue())
        elif job == 2:
            return Troll(name, Warrior())
        elif job == 3:
            return Troll(name, Mage())
        elif job == 4:
            return Troll(name, Paladin())
        elif job == 5:
            return Troll(name, Warklock())


def createCharacter():
    side = sideDiceder()
    race = raceDicider(side)
    job = jobDecider()
    if side == 1:
        character = createBlueSide(race, job)
    else:
        character = createRedSide(race, job)

    sex = input("gender? ")
    character.set_sex(sex)
    altura = float(input("Heigth "))
    character.set_heigth(altura)
    anchura = float(input("Width"))
    character.set_width(anchura)
    description = input("add a description")
    character.set_description(description)

    return character


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    IFicha = IFicha()
    char = createCharacter()
    IFicha.defineEnemy(char)
    IFicha.add(char)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
