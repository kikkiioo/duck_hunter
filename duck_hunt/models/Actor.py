from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Actor:
    xPos: int = 0
    yPos: int = 0