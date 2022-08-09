from enum import Enum

class EnumDuckState(str, Enum):
    NOTHING = 'None'
    RIGHTFLY = 'RightFly'
    LEFTFLY = 'LeftFly'
    DIE = 'Die'

    def __str__(self) -> str:
        return self.value