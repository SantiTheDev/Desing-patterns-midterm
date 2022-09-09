from Character import Character
from CharacterSide import RedCharacter  # or BlueCharacter
from EnemyProcessor import BlueEnemyProcessor, RedEnemyProcessor


class IFicha():

    def defineEnemy(self, character: Character):
        if isinstance(character, RedCharacter):
            RedEnemyProcessor().isEnemy(character)
        else:
            BlueEnemyProcessor().isEnemy(character)

    def add(self, character: Character):
        print(f"character{character.__str__()} added")
