
import cocotb_stub_sim
from pyuvm import *
from udc_tests_base import UdcTestsBase
import uvm_dataclasses as udc

class TestEnvSmoke(UdcTestsBase):

    def test_smoke(self):

        @udc.environment
        class my_env(uvm_component):
            
            def __init__(self, name, parent):
                super().__init__(name, self)
            
            def __post_init__(self):
                print("my_env.post_init")
            
            class config_t(object):
                a : int = 0
                b : int = 1
                
        @udc.environment
        class my_super_env(my_env):

            e1 : my_env
            e2 : my_env
            
            def __post_init__(self):
#                super().__post_init__()
                print("my_super_env.post_init")
#                uvm_component.__init__(self, "abc", self)
                print("e1=%s" % str(self.e1))

            class config_t(object):
                c : int = 2
                d : int = 3

        @udc.bench
        class my_test(uvm_test):

            top_env = my_super_env 

            def build_phase(self):
                print("outer::build_phase")
#                self.env = my_super_env("env", self)
                print("--> create env", flush=True)
                self.env = my_super_env()
                print("<-- create env", flush=True)
                print("--> call super env", flush=True)
                uvm_component.__init__(self.env, "env", self)
                print("<-- call super env", flush=True)

            class my_test(uvm_test):
                def build_phase(self):
                    print("build_phase")
                    self.env = my_super_env("env", self)
                pass

        async def entry(dut):
            print("entry")
            await uvm_root().run_test("my_test")

        cocotb_stub_sim.run(entry)        

    def test_component_inst(self):
        
        @udc.object
        class my_obj1(uvm_object):
            a : int = 4
            b : int = 5
            
        @udc.object
        class my_obj2(uvm_object):
            c : my_obj1
            d : my_obj1
        
        @udc.component
        class my_component(uvm_component):
            a : int = 1
            b : int = 2
            c : my_obj2
            
            def __post_init__(self):
                print("my_component.post_init a=%d b=%d" % (self.a, self.b))
                print("my_component: c=%s" % str(self.c))

            def connect_phase(self):
                print("%s: connect_phase" % self.get_full_name())
            
        @udc.component
        class my_test(uvm_test):
            c1 : my_component
            c2 : my_component
           
#            def __post_init__(self):
#               print("my_test.post_init c1=%s" % str(self.c1))
           
        async def entry(dut):
            await uvm_root().run_test("my_test")
        cocotb_stub_sim.run(entry)
