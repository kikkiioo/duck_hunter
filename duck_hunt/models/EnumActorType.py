from enum import Enum


class EnumActorType(str, Enum):
    NOTHING = 'None'
    DOG = 'Dog'
    DUCK = 'Duck'

    def __str__(self) -> str:
        return self.value