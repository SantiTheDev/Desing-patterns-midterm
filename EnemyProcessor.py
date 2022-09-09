from abc import abstractmethod
from CharacterSide import *


class EnemyProcessor:

    @abstractmethod
    def isEnemy(self, char: Character):
        pass


class BlueEnemyProcessor(EnemyProcessor):

    def isEnemy(self, char: Character):
        if isinstance(char, BlueCharacter):
            print("Alli --> blue side")
            print("Enemy---> red side")


class RedEnemyProcessor(EnemyProcessor):

    def isEnemy(self, char: Character):
        if isinstance(char, RedCharacter):
            print("alli ---> red SIde")
            print("Enemy --> blue Side")
