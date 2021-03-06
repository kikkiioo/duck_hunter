from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.Actor import Actor
from models.EnumPlayerState import EnumPlayerState

@dataclass_json
@dataclass 
class Player(Actor):
    state: EnumPlayerState.Nothing
    shotCount: int = 0
    hitCount: int = 0
    successShotCount: int = 0