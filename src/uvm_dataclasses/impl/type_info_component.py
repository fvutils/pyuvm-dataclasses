
from typing import List, Tuple
from pyuvm import uvm_analysis_port, uvm_analysis_export, uvm_subscriber
from uvm_dataclasses.impl.type_info_object import TypeInfoObject


class TypeInfoComponent(TypeInfoObject):
    
    def __init__(self, ti):
        super().__init__(ti)
        self._uvm_component_fields : List[Tuple[str,type]] = []
        self._udc_component_fields : List[Tuple[str,TypeInfoComponent]] = []
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
    
    def pre_build_phase(self, parent):
        if hasattr(parent, "__pre_build_phase__"):
            parent.__pre_build_phase__()
        if hasattr(parent, "pre_build_phase"):
            parent.pre_build_phase()
            
    def core_build_phase(self, parent):
        print("TypeInfoComponent.build_phase: %d sub-components" % len(self._uvm_component_fields))

        # TODO: these should be TypeInfoComponent
        for name,type in self._uvm_component_fields:
            setattr(parent, name, type(name, parent))
            
        for name,comp_ti in self._udc_component_fields:
            setattr(parent, name, comp_ti.T(name, parent))
            
        # Construct analysis ports, exports, and impl
        for name,type in self._analysis_ports:
            setattr(parent, name, uvm_analysis_port(name, parent))
        for name,type in self._analysis_exports:
            setattr(parent, name, uvm_analysis_export(name, parent))
        for name,type in self._analysis_impl:
            setattr(parent, name, 
                    uvm_subscriber.uvm_AnalysisImp(name, parent, 
                            getattr(parent, "write_%s" % name)))

    def post_build_phase(self, parent):            
        if hasattr(parent, "__post_build_phase__"):
            parent.__post_build_phase__()
        if hasattr(parent, "post_build_phase"):
            parent.post_build_phase()
            
    def build_phase(self, parent):
        self.pre_build_phase(parent)
        self.core_build_phase(parent)
        self.post_build_phase(parent)
    
    @staticmethod
    def get(info):
        if not hasattr(info, "_udc_info"):
            setattr(info, "_udc_info", TypeInfoComponent(info))
        return info._udc_info