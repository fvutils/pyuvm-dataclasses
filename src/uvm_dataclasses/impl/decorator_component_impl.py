
import dataclasses
import pyuvm
from pyuvm import uvm_component

from uvm_dataclasses.impl.type_info_component import TypeInfoComponent
from .decorator_object_impl import DecoratorObjectImpl
from .method_impl_component import MethodImplComponent

class DecoratorComponentImpl(DecoratorObjectImpl):
    IS_SUBCLASS_TYPES = DecoratorObjectImpl.IS_SUBCLASS_TYPES + \
        [(pyuvm.uvm_component, "abc")]
#    TYPE_PROCESSING_HOOKS = DecoratorObjectImpl.TYPE_PROCESSING_HOOKS + \
#        [lambda self, T : DecoratorComponentImpl.process(self, T)]
        
    def __init__(self, args, kwargs):
        super().__init__(args, kwargs)
        
    def pre_decorate(self, T):
        comp_ti = TypeInfoComponent.get(self.get_typeinfo())
        
        # Work back through the type hierarchy to find the
        # last __init__ method with three parameters
        comp_ti._uvm_comp_init = self._find_uvm_component_init(T)
    
    def init_annotated_field(self, key, type, has_init):
        print("init_annotated_field: %s" % key)

        if not has_init:        
            if issubclass(type, uvm_component):
                comp_ti = TypeInfoComponent.get(self.get_typeinfo())
                comp_ti._uvm_component_fields.append((key, type))
                self.set_field_initial(key, None)
            else:
                super().init_annotated_field(key, type, has_init)
        else:
            super().init_annotated_field(key, type, has_init)

    def post_decorate(self, T, Tp):
        print("DecoratorComponentImpl.post_decorate")
        comp_ti = TypeInfoComponent.get(self.get_typeinfo())

        comp_ti._dataclass_init = Tp.__init__
        Tp.__init__ = MethodImplComponent.init
        
        Tp.build_phase = MethodImplComponent.build_phase
    
    pass

    def _find_uvm_component_init(self, c):
        print("_find_uvm_component_init %s" % str(c))
        if hasattr(c, "__init__") and c.__init__.__code__.co_argcount == 3:
            print(" -- match")
            return c.__init__
        else:
            ret = None
            for b in c.__bases__:
                ret = self._find_uvm_component_init(b)
                if ret is not None:
                    break
            return ret

