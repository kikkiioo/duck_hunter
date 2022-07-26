import dataclasses
import string
from tokenize import Double
from pydantic import DataclassTypeError, dataclasses
from dataclasses_json import dataclass_json

from models.Actor import Actor
from models.EnumDuckState import EnumDuckState

@dataclass_json
@dataclasses
class Duck(Actor):
    state: EnumDuckState.Nothing
    flyingSpeed: Double = 0
    flyingDirection: string = "left"
    endXpos: Double = 0
    endYpos: Double = 0