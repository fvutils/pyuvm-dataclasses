
import typeworks
from udc_tests_base import UdcTestsBase
from pyuvm import uvm_component, uvm_object
import uvm_dataclasses as udc

class TestTypeRegistration(UdcTestsBase):
    
    def test_smoke(self):
        
        @udc.component
        class my_component(uvm_component):
            pass
        
        typeworks.TypeRgy.elab()
        self.assertEqual(len(typeworks.TypeRgy.get_types(udc.TypeKind.Component)), 1)
        
    def test_one_comp_one_env(self):
        
        @udc.component
        class my_component(uvm_component):
            pass
        
        @udc.environment
        class my_env(uvm_component):
            
            @udc.config
            class config(uvm_object):
                pass
            
            pass
        
        typeworks.TypeRgy.elab()
        self.assertEqual(len(typeworks.TypeRgy.get_types(udc.TypeKind.Component)), 1)
        self.assertEqual(len(typeworks.TypeRgy.get_types(udc.TypeKind.Environment)), 1)
        