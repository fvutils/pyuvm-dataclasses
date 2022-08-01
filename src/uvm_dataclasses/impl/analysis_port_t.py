
from enum import Enum, auto
from mmap import PROT_WRITE

class AnalysisPortKind(Enum):
    Port = auto()
    Impl = auto()
    Export = auto()

class AnalysisPortT(object):
    T = None
    Kind = None

    pass