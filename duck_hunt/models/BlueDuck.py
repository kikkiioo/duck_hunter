import dataclasses
from pip import List
from pydantic import DataclassTypeError, dataclasses
from dataclasses_json import dataclass_json

from models.Duck import Duck

@dataclass_json
@dataclasses    
class BlueDuck(Duck):
    blueScore: int = 0