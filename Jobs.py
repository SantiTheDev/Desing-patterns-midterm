from abc import ABC


class Jobs(ABC):

    skills = {}
    jobDescription = ""
    Passives = {}
    weapons = {}
    gear = {}

    def getName(self):
        return self.__class__.__name__


class Rogue(Jobs):
    skills = {1: "backstab", 2: "Shadowstep"}
    jobDescription = """rogues are lightly armored meleers who use stealth to get in
                        close and then hit their target with precision strikes."""
    weapons = {1: "daggers", 2: "one handed swords", 3: "maces", 4: "axes"}
    Passives = {1: "Stealth"}
    gear = {1: "light armor", 2: "cloth armor"}

    def __str__(self):
        return str({
            "skills": self.skills,
            "description": self.jobDescription,
            "weapons": self.weapons,
            "Passives": self.Passives,
            "gear": self.gear
        })


class Warrior(Jobs):

    skills = {1: "slam"}
    jobDescription = """Warriors combine strength, leadership, and a vast knowledge of arms
                        and armor to wreak havoc in glorious combat"""
    weapons = {1: "daggers", 2: "one handed swords", 3: "two handed swords", 4: "maces", 5: "axes", 6: "shields"}
    Passives = {1: "War machine"}
    gear = {1: "light armor", 2: "cloth armor", 3: "mail armor", 4: "plate armor"}

    def __str__(self):
        return str({
            "skills": self.skills,
            "description": self.jobDescription,
            "weapons": self.weapons,
            "Passives": self.Passives,
            "gear": self.gear
        })


class Mage(Jobs):

    skills = {1: "frostball"}
    jobDescription = """is a damage-dealing spell-caster that specializes in burst damage and area of effect spells. 
    Mages are well known for their formidable damage output, as well as their range of crowd control abilities."""
    weapons = {1: "daggers", 2: "one handed swords", 3: "staves"}
    Passives = {1: "Arcane Power"}
    gear = {1: "cloth armor"}

    def __str__(self):
        return str({
            "skills": self.skills,
            "description": self.jobDescription,
            "weapons": self.weapons,
            "Passives": self.Passives,
            "gear": self.gear
        })


class Paladin(Jobs):

    skills = {1: "holy strike"}
    jobDescription = """ is a holy knight, a hybrid class with the ability to play a 
    variety of different roles — healing ,tanking , and DPS."""
    weapons = {1: "daggers", 2: "one handed swords", 3: "two handed swords", 4: "maces", 5: "axes", 6: "shields"}
    Passives = {1: "beacon of ligth"}
    gear = {1: "light armor", 2: "cloth armor", 3: "mail armor", 4: "plate armor"}

    def __str__(self):
        return str({
            "skills": self.skills,
            "description": self.jobDescription,
            "weapons": self.weapons,
            "Passives": self.Passives,
            "gear": self.gear
        })


class Warklock(Jobs):

    skills = {1: "shadowball"}
    jobDescription = """ is a damage-dealing spell-caster class, known for their wide range of debuffs and damage over 
    time effects.Warlocks are also recognisable by their demonic minions, used to deal damage to foes, as well as to 
    provide both offensive and defensive utility."""
    weapons = {1: "daggers", 2: "one handed swords", 3: "staves"}
    Passives = {1: "Demonic Shield"}
    gear = {1: "cloth armor"}

    def __str__(self):
        return str({
            "skills": self.skills,
            "description": self.jobDescription,
            "weapons": self.weapons,
            "Passives": self.Passives,
            "gear": self.gear
        })
