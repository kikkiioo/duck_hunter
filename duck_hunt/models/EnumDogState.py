import enum
from enum import Enum


class EnumDogState(str, Enum):
    NOTHING = 'None'
    SNIFF = 'Sniff'
    SNIFF1 = 'Sniff1'
    LOOK = 'Look'
    JUMP_UP = 'JumpUp'
    JUMP_DOWN = 'JumpDown'
    CATCHUP = 'CatchUp'
    CATCHDOWN = 'CatchDown'
    GIGGLE = 'Giggle'

    def __str__(self) -> str:
        return self.value

