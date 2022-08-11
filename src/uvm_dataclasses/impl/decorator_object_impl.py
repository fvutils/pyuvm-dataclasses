
import typeworks
from pyuvm import uvm_component, uvm_object
from uvm_dataclasses.impl.method_impl_object import MethodImplObject

from uvm_dataclasses.impl.type_info_object import TypeInfoObject
from ..type_kind import TypeKind

class DecoratorObjectImpl(typeworks.ClsDecoratorBase):
    
    def get_type_category(self):
        return TypeKind.Object
    
    def init_annotated_field(self, key, type, has_init):
        print("DecoratorObjectImpl.init_annotated_field: %s %s" % (key, str(type)))
        if not has_init:
            obj_ti = TypeInfoObject.get(self.get_typeinfo())
            if issubclass(type, uvm_component):
                # In the context of a uvm_object-derived class,
                # uvm_component handles will always need user attention
                self.set_field_initial(key, None)
            elif issubclass(type, uvm_object):
                print("issubclass uvm_object")
                if TypeInfoObject.isUdcType(typeworks.TypeInfo.get(type, False)):
                    print("  udc object")
                    obj_ti._udc_object_fields.append((key, 
                        TypeInfoObject.get(typeworks.TypeInfo.get(type))))
                else:
                    print("  plain object")
                    obj_ti._uvm_object_fields.append((key, type))
                self.set_field_initial(key, None)
            else:
                super().init_annotated_field(key, type, has_init)
        else:
            super().init_annotated_field(key, type, has_init)
            
    def post_decorate(self, T, Tp):
        obj_ti = TypeInfoObject.get(self.get_typeinfo())
        
        Tp.__init__ = MethodImplObject.init
