from pydantic.dataclasses import dataclass
from dataclasses_json import dataclass_json
from tokenize import Double

@dataclass_json
@dataclass
class Actor:
    xPos: Double = 0.0
    yPos: Double = 0.0