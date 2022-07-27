from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.Duck import Duck

@dataclass_json
@dataclass
class BlueDuck(Duck):
    blueScore: int = 0