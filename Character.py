from abc import ABC
from Jobs import Jobs


class Character(ABC):

    sex = ""
    description = ""
    width = 0.0
    height = 0.0
    job: Jobs

    def set_job(self, job: Jobs):
        pass

    def set_sex(self, sex):
        pass

    def set_description(self, description):
        pass

    def set_width(self, width):
        pass

    def set_heigth(self, heigth):
        pass
