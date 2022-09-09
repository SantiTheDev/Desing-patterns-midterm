from Jobs import Jobs
from CharacterSide import RedCharacter


class Orc(RedCharacter):
    racial = {1: "Fury"}

    def __init__(self, name: str, job: Jobs):
        self.name = name
        self.job = job

    def set_sex(self, sex):
        self.sex = sex

    def set_heigth(self, heigth):
        self.height = heigth

    def set_description(self, description):
        self.description = description

    def set_width(self, width):
        self.width = width

    def __str__(self):
        return str({
            "job": self.job.getName(),
            "name": self.name,
            "sex": self.sex,
            "heigth": self.height,
            "width": self.width,
            "description": self.description
        })


class Undead(RedCharacter):
    racial = {1: "uderwater breating"}

    def __init__(self, name: str, job: Jobs):
        self.name = name
        self.job = job

    def set_sex(self, sex):
        self.sex = sex

    def set_heigth(self, heigth):
        self.height = heigth

    def set_description(self, description):
        self.description = description

    def set_width(self, width):
        self.width = width

    def __str__(self):
        return str({
            "job": self.job.getName(),
            "name": self.name,
            "sex": self.sex,
            "heigth": self.height,
            "width": self.width,
            "description": self.description
        })


class Tauren(RedCharacter):
    racial = {1: "War stomp"}

    def __init__(self, name: str, job: Jobs):
        self.name = name
        self.job = job

    def set_sex(self, sex):
        self.sex = sex

    def set_heigth(self, heigth):
        self.height = heigth

    def set_description(self, description):
        self.description = description

    def set_width(self, width):
        self.width = width

    def __str__(self):
        return str({
            "job": self.job.getName(),
            "name": self.name,
            "sex": self.sex,
            "heigth": self.height,
            "width": self.width,
            "description": self.description
        })


class Troll(RedCharacter):
    racial = {1: "berserking"}

    def __init__(self, name: str, job: Jobs):
        self.name = name
        self.job = job

    def set_sex(self, sex):
        self.sex = sex

    def set_heigth(self, heigth):
        self.height = heigth

    def set_description(self, description):
        self.description = description

    def set_width(self, width):
        self.width = width

    def __str__(self):
        return str({
            "job": self.job.getName(),
            "name": self.name,
            "sex": self.sex,
            "heigth": self.height,
            "width": self.width,
            "description": self.description
        })
