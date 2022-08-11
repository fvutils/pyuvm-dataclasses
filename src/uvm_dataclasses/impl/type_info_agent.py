
from re import I
from .type_info_util import TypeInfoUtil, UtilKind

class TypeInfoAgent(TypeInfoUtil):
    
    def __init__(self, info):
        super().__init__(info, UtilKind.Agent)
    
    