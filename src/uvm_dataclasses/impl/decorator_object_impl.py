
import typeworks
from pyuvm import uvm_component, uvm_object

from uvm_dataclasses.impl.type_info_object import TypeInfoObject

class DecoratorObjectImpl(typeworks.ClsDecoratorBase):
    
    def init_annotated_field(self, key, type, has_init):
        print("object.init_annotated_field: %s %s" % (key, str(type)))
        if not has_init:
            obj_ti = TypeInfoObject.get(self.get_typeinfo())
            if issubclass(type, uvm_component):
                # In the context of a uvm_object-derived class,
                # uvm_component handles will always need user attention
                self.set_field_initial(key, None)
            elif issubclass(type, uvm_object):
                print("is_uvmobject")
                obj_ti._uvm_object_fields.append((key, type))
                self.set_field_initial(key, None)
            else:
                super().init_annotated_field(key, type, has_init)
        else:
            super().init_annotated_field(key, type, has_init)
