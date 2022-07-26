import dataclasses
from pydantic import DataclassTypeError, dataclasses
from dataclasses_json import dataclass_json

from models.Actor import Actor
from models.EnumPlayerState import EnumPlayerState

@dataclass_json
@dataclasses 
class Player(Actor):
    state: EnumPlayerState.Nothing
    shotCount: int = 0
    hitCount: int = 0
    successShotCount: int = 0