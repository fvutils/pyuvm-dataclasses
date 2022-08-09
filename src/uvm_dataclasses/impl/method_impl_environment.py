

from uvm_dataclasses.impl.method_impl_component import MethodImplComponent
from uvm_dataclasses.impl.type_info_environment import TypeInfoEnvironment


class MethodImplEnvironment(object):
    
    @staticmethod
    def init(self, name, parent):
        env_ti = TypeInfoEnvironment.get(type(self)._typeinfo)
        MethodImplComponent.init(self, name, parent)
        
        print("TODO: create config %s" % str(env_ti.config_t))
        setattr(self, "configuration", env_ti.config_t())
        
        