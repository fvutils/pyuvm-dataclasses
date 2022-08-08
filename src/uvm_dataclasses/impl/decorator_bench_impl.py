'''
Created on Jul 4, 2022

@author: mballance
'''

from uvm_dataclasses.impl.type_info_component import TypeInfoComponent
from .decorator_component_impl import DecoratorComponentImpl

class DecoratorBenchImpl(DecoratorComponentImpl):
    
    def post_init_annotated_fields(self):
        ti_comp = TypeInfoComponent.get(self.get_typeinfo())
        
        if len(ti_comp._uvm_component_fields) == 0:
            raise Exception("No environment class specified")
        elif len(ti_comp._uvm_component_fields) > 1:
            raise Exception("Expect a single environment class ; %d specified" % (
                len(ti_comp._uvm_component_fields),))
        return super().post_init_annotated_fields()
    
    pass
