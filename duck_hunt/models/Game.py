import dataclasses
from pip import List
from pydantic import DataclassTypeError, dataclasses
from dataclasses_json import dataclass_json

from models.Actor import Actor

@dataclass_json
@dataclasses.dataclass
class Game:
    level : int = 0
    score: int = 0
    shotCount: int = 0
    actors: List[Actor] = dataclasses.field(default_factory= list)