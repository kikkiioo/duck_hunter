import dataclasses
from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json
from models.Actor import Actor


@dataclass_json
@dataclass
class Game:
    actors: list[Actor] = dataclasses.field(default_factory = list)
    level : int = 1
    score: int = 0
    shotCount: int = 0
    isNextLevel: bool = False
    isGameOver: bool = False
    frame: int = 0
    animation_duration: float = 0.0
    animation_start_time: float = 0.0
