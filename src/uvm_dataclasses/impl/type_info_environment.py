
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from uvm_dataclasses.impl.type_info_util import TypeInfoUtil, UtilKind
from .type_info_component import TypeInfoComponent

class TypeInfoEnvironment(TypeInfoUtil):
    
    def __init__(self, info):
        super().__init__(info, UtilKind.Env)
        self._config_t = None
        self._agents = []
        self._subenvs = []

    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoEnvironment(info))
        return getattr(info, TypeInfoObject.ATTR_NAME)