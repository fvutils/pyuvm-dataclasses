
from typing import List, Tuple
from uvm_dataclasses.impl.type_info_agent import TypeInfoAgent
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from uvm_dataclasses.impl.type_info_util import TypeInfoUtil, UtilKind
from .type_info_component import TypeInfoComponent

class TypeInfoEnvironment(TypeInfoUtil):
    
    def __init__(self, info):
        super().__init__(info, UtilKind.Env)
        self._agents : List[Tuple[str,TypeInfoAgent]] = []
        self._subenvs : List[Tuple[str,TypeInfoEnvironment]] = []
        
    def init(self, obj, name, parent):
        print("TypeInfoEnvironment.init")
        super().init(obj, name, parent)
        
    def build_phase(self, parent):
        print("TypeInfoEnvironment.build_phase")
        self.pre_build_phase(parent)
        
        self.core_build_phase(parent)
        
        for name,agent_ti in self._agents:
            print("TODO: initialize agent")
            agent = parent.get_child(name)
            agent.configuration = getattr(parent.configuration, "%s_config" % name)
            
        for name,subenv_ti in self._subenvs:
            print("TODO: initialize sub-env")
            subenv = parent.get_child(name)
            subenv.configuration = getattr(parent.configuration, "%s_config" % name)
            
        self.post_build_phase(parent)
        
        # Now, propagate the configuration
        parent.configuration._initialize()


    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            print("Create TypeInfoEnvironment")
            setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoEnvironment(info))
        return getattr(info, TypeInfoObject.ATTR_NAME)