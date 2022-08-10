
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from uvm_dataclasses.impl.type_info_util import TypeInfoUtil, UtilKind
from .type_info_component import TypeInfoComponent

class TypeInfoEnvironment(TypeInfoUtil):
    
    def __init__(self, info):
        super().__init__(info, UtilKind.Env)
        self._agents = []
        self._subenvs = []
        
    def init(self, obj, name, parent):
        print("TypeInfoEnvironment.init")
        super().init(obj, name, parent)
        
    def build_phase(self, parent):
        print("TypeInfoEnvironment.build_phase")
        super().build_phase(parent)
        
        for agent in self._agents:
            print("TODO: initialize agent")
            
        for subenv in self._subenvs:
            print("TODO: initialize sub-env")

    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoEnvironment(info))
        return getattr(info, TypeInfoObject.ATTR_NAME)