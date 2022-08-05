
import uvm_dataclasses as udc
import cocotb_stub_sim
from udc_tests_base import UdcTestsBase
from pyuvm import *

class TestEnvSmoke(UdcTestsBase):

    def test_smoke(self):

#        @udc.environment
        class my_env(uvm_component):
            
            class config_t(object):
                a : int = 0
                b : int = 1
                
        @udc.environment
        class my_super_env(uvm_component):

            e1 : 'my_env'
            e2 : 'my_env'

            class config_t(object):
                c : int = 2
                d : int = 3

        @udc.bench
        class my_test(uvm_test):

            top_env = my_super_env 

            def build_phase(self):
                print("outer::build_phase")
                self.env = my_super_env("env", self)

            class my_test(uvm_test):
                def build_phase(self):
                    print("build_phase")
                    self.env = my_super_env("env", self)
                pass

        class my_test2(my_test):

            def build_phase(self):
                print("my_test2::build_phase")
                super().build_phase()
        
        async def entry(dut):
            print("entry")
            await uvm_root().run_test("my_test2")

        cocotb_stub_sim.run(entry)        

