'''
Created on Jul 4, 2022

@author: mballance
'''

import pyuvm
import typing

from uvm_dataclasses.impl.type_info_component import TypeInfoComponent

from .decorator_component_impl import DecoratorComponentImpl


class DecoratorEnvironmentImpl(DecoratorComponentImpl):
    
    def pre_decorate(self, T):
        if not hasattr(T, "config_t"):
            raise Exception("No 'config_t' class defined")
        return super().pre_decorate(T)
    
    def pre_init_annotated_fields(self):
        # Add a configuration field 
        self.add_field_decl("configuration", self.T.config_t, False, None)
        return super().pre_init_annotated_fields()

    def init_annotated_field(self, key, type, has_init):
        return super().init_annotated_field(key, type, has_init)
    
    def post_init_annotated_fields(self):
        comp_ti = TypeInfoComponent.get(self.get_typeinfo())
        print("Component: %d uvm_component fields" % len(comp_ti._uvm_component_fields))
        return super().post_init_annotated_fields()
