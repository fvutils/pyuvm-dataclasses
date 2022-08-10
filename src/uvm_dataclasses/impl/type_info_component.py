
from pyuvm import uvm_analysis_port, uvm_analysis_export, uvm_subscriber
from uvm_dataclasses.impl.type_info_object import TypeInfoObject


class TypeInfoComponent(TypeInfoObject):
    
    def __init__(self, ti):
        super().__init__(ti)
        self._uvm_component_fields = []
        self._uvm_comp_init = None
        self._analysis_ports = []
        self._analysis_exports = []
        self._analysis_impl = []
        
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
        if hasattr(parent, "__pre_build_phase__"):
            parent.__pre_build_phase__()
            
        print("TypeInfoComponent.build_phase: %d sub-components" % len(self._uvm_component_fields))
        for name,type in self._uvm_component_fields:
            setattr(parent, name, type(name, parent))
            
        # Construct analysis ports, exports, and impl
        for name,type in self._analysis_ports:
            setattr(parent, name, uvm_analysis_port(name, parent))
        for name,type in self._analysis_exports:
            setattr(parent, name, uvm_analysis_export(name, parent))
        for name,type in self._analysis_impl:
            setattr(parent, name, 
                    uvm_subscriber.uvm_AnalysisImp(name, parent, 
                            getattr(parent, "write_%s" % name)))
            
        if hasattr(parent, "__post_build_phase__"):
            parent.__post_build_phase__()
        pass
    
    @staticmethod
    def get(info):
        if not hasattr(info, "_udc_info"):
            setattr(info, "_udc_info", TypeInfoComponent(info))
        return info._udc_info