from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.Actor import Actor
from models.EnumDogState import EnumDogState

@dataclass_json
@dataclass
class Dog(Actor):
    state: EnumDogState = EnumDogState.NOTHING
    frame: int = 0