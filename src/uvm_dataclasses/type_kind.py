
from enum import Enum, auto


class TypeKind(Enum):
    Object = auto()
    Component = auto()
    Agent = auto()
    Bench = auto()
    Environment = auto()
    