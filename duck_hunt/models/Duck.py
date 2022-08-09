from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.Actor import Actor
from models.EnumDuckState import EnumDuckState

@dataclass_json
@dataclass
class Duck(Actor):
    state: EnumDuckState = EnumDuckState.NOTHING
    flyingSpeed: float = 0
    flyingDirection: str = "left"
    endXpos: int = 0
    endYpos: int = 0