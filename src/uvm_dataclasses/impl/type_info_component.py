
from uvm_dataclasses.impl.type_info_object import TypeInfoObject


class TypeInfoComponent(TypeInfoObject):
    
    def __init__(self, ti):
        super().__init__(ti)
        self._uvm_component_fields = []
        self._uvm_comp_init = None
        
        pass
    
    def init(self, obj, name, parent):
        # Initialize the component class first
        print("--> _uvm_comp_init")

        # Initialize uvm-component fields        
        self._uvm_comp_init(obj, name, parent)

        print("<-- _uvm_comp_init")
        print("--> super.init()", flush=True)
        super().init(obj)
        print("<-- super.init()", flush=True)
        pass
    
    def build_phase(self, parent):
        for name,type in self._uvm_component_fields:
            setattr(parent, name, type(name, parent))
        pass
    
    @staticmethod
    def get(info):
        if not hasattr(info, "_udc_info"):
            setattr(info, "_udc_info", TypeInfoComponent(info))
        return info._udc_info