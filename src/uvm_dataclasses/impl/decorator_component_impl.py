
import dataclasses
import pyuvm
from pyuvm import uvm_component
import typeworks

from uvm_dataclasses.impl.type_info_component import TypeInfoComponent
from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from ..type_kind import TypeKind
from .decorator_object_impl import DecoratorObjectImpl
from .method_impl_component import MethodImplComponent
from .analysis_port_t import AnalysisPortKind, AnalysisPortT

class DecoratorComponentImpl(DecoratorObjectImpl):
    IS_SUBCLASS_TYPES = DecoratorObjectImpl.IS_SUBCLASS_TYPES + \
        [(pyuvm.uvm_component, "abc")]
#    TYPE_PROCESSING_HOOKS = DecoratorObjectImpl.TYPE_PROCESSING_HOOKS + \
#        [lambda self, T : DecoratorComponentImpl.process(self, T)]
        
    def __init__(self, args, kwargs):
        super().__init__(args, kwargs)
        
    def get_type_category(self):
        return TypeKind.Component
        
    def pre_decorate(self, T):
        comp_ti = TypeInfoComponent.get(self.get_typeinfo())
        print("Component.pre_decorate comp_ti=%s" % str(comp_ti))
        
        # Work back through the type hierarchy to find the
        # last __init__ method with three parameters
        comp_ti._uvm_comp_init = self._find_uvm_component_init(T)
        
        super().pre_decorate(T)
    
    def init_annotated_field(self, key, type, has_init, init):
        if not has_init:
            print("type=%s" % str(type))
            if issubclass(type, uvm_component):
                comp_ti = TypeInfoComponent.get(self.get_typeinfo())
                if TypeInfoObject.isUdcType(typeworks.TypeInfo.get(type, False)):
                    comp_ti._udc_component_fields.append((key, 
                            TypeInfoObject.get(typeworks.TypeInfo.get(type))))
                else:
                    comp_ti._uvm_component_fields.append((key, type))
                self.set_field_initial(key, None)
            elif issubclass(type, AnalysisPortT):
                comp_ti = TypeInfoComponent.get(self.get_typeinfo())
                if type.Kind == AnalysisPortKind.Port:
                    comp_ti._analysis_ports.append((key, type))
                elif type.Kind == AnalysisPortKind.Impl:
                    comp_ti._analysis_impl.append((key, type))
                elif type.Kind == AnalysisPortKind.Export:
                    comp_ti._analysis_exports.append((key, type))
                else:
                    raise Exception("Unknown analysis-port kind %s" % type.Kind)
                self.set_field_initial(key, None)
            else:
                super().init_annotated_field(key, type, has_init, init)
        else:
            super().init_annotated_field(key, type, has_init, init)
            
    def post_init_annotated_fields(self):
        comp_ti = TypeInfoComponent.get(self.get_typeinfo())
        super().post_init_annotated_fields()

        # Provide fallback implementation for missing write functions        
        for name,type in comp_ti._analysis_impl:
            if not hasattr(self.T, "write_%s" % name):
                setattr(self.T, "write_%s" % name, 
                        lambda self,t,name=name: self.logger.warn("Analysis impl write_%s not implemented" % name))

    def post_decorate(self, T, Tp):
        comp_ti = TypeInfoComponent.get(self.get_typeinfo())

        comp_ti._dataclass_init = Tp.__init__

#        if Tp.__init__.__code__.co_argcount == 3:
#            raise Exception("Something went wrong ; dataclass.__init__ shouldn't have three params")
        Tp.__init__ = MethodImplComponent.init
        
        Tp.build_phase = MethodImplComponent.build_phase

    def _find_uvm_component_init(self, c):
        """
        Searches base classes for an __init__ matching the signature
        required for class uvm_component
        """
        if hasattr(c, "__init__") and hasattr(c.__init__, "__code__") and c.__init__.__code__.co_argcount == 3:
            print(" -- match")
            return c.__init__
        else:
            ret = None
            for b in c.__bases__:
                ret = self._find_uvm_component_init(b)
                if ret is not None:
                    break
            return ret

