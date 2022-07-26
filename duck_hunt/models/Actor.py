import dataclasses
import pydantic
from dataclasses_json import dataclass_json
from tokenize import Double

@dataclass_json
@dataclasses 
class Actor():
    xPos: Double = 0
    yPos: Double = 0