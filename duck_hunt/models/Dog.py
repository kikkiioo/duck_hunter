import dataclasses
from pydantic import DataclassTypeError, dataclasses
from dataclasses_json import dataclass_json

from models.Actor import Actor
from models.EnumDogState import EnumDogState

@dataclass_json
@dataclasses
class Dog(Actor):
    state: EnumDogState.Nothing