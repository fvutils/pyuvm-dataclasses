
from uvm_dataclasses.impl.type_info_component import TypeInfoComponent


class MethodImplComponent(object):

    @staticmethod    
    def init(self, name, parent):
        """Implements dataclass initialization for uvm_component

        Args:
            name (_type_): _description_
            parent (_type_): _description_
        """
        print("--> uvm_comp_init %s \"%s\"" % (name, str(parent)))
        comp_ti = TypeInfoComponent.get(type(self)._typeinfo)
        print("--> comp_ti.init", flush=True)
        comp_ti.init(self, name, parent)
        print("<-- comp_ti.init", flush=True)
        print("<-- uvm_comp_init")
        
    @staticmethod
    def build_phase(self):
        """
        Implements uvm_component build_phase for dataclasses
        """
        comp_ti : TypeInfoComponent = TypeInfoComponent.get(type(self)._typeinfo)
        comp_ti.build_phase(self)


