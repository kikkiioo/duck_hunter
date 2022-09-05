from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.EnumActorType import EnumActorType


@dataclass_json
@dataclass
class Actor:
    xPos: int = 0
    yPos: int = 0
    actorType: EnumActorType = EnumActorType.NOTHING