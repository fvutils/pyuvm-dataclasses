
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from .type_info_util import TypeInfoUtil, UtilKind

class TypeInfoBench(TypeInfoUtil):
    
    def __init__(self, info):
        super().__init__(info, UtilKind.Bench)
        self._top_env_ti = None
        
    def init(self, obj, name, parent):
        print("TypeInfoBench.init configuration=%s" % str(obj.configuration))
        super().init(obj, name, parent)
        
    def build_phase(self, parent):
        print("TypeInfoBench.build_phase")
        print("top_env_ti=%s" % str(self._top_env_ti))
        print("top_env_ti._config_t=%s" % str(self._top_env_ti._config_t))
#        setattr(parent, "configuration", 
#                self._top_env_ti._config_t())
        super().build_phase(parent)
        
        # for agent in self._agents:
        #     print("TODO: initialize agent")
            
        # for subenv in self._subenvs:
        #     print("TODO: initialize sub-env")        
        
    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoObject.ATTR_NAME):
            setattr(info, TypeInfoObject.ATTR_NAME, TypeInfoBench(info))
        return getattr(info, TypeInfoObject.ATTR_NAME)
    