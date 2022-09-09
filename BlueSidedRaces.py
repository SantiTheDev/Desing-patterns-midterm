from Jobs import Jobs
from CharacterSide import BlueCharacter


class Human(BlueCharacter):
    racial = {}

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


class Drawf(BlueCharacter):
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


class Gnome(BlueCharacter):
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


class DarkElf(BlueCharacter):
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
