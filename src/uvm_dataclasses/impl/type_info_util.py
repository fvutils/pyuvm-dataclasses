
from enum import Enum, auto
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from .type_info_component import TypeInfoComponent

class UtilKind(Enum):
    Agent = auto()
    Bench = auto()
    Config = auto()
    Env = auto()

class TypeInfoUtil(TypeInfoComponent):
    
    def __init__(self, info, kind):
        print("TypeInfoUtil()")
        super().__init__(info)
        self.kind = kind
        self._config_t = None
        
    def decl_config_field(self, key, type):
        if not hasattr(self._config_t, "__annotations__"):
            setattr(self._config_t, "__annotations__", dict())
        self._config_t.__annotations__[key] = type
    
    @staticmethod
    def getUtilKind(info):
        if info is None:
            return None

        udc_info = TypeInfoObject.get(info, False)
        if isinstance(udc_info, TypeInfoUtil):
            return udc_info.kind
        else:
            return None
    
            
