from enum import Enum


class EnumPlayerState(str,Enum):
    NOTHING = 'None'

    def __str__(self) -> str:
        return self.value
