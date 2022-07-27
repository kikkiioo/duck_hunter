from typing import List
from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.Actor import Actor

@dataclass_json
@dataclass
class Game:
    level : int = 0
    score: int = 0
    shotCount: int = 0
    actors: List[Actor] = dataclass.Field(default_factory= list)