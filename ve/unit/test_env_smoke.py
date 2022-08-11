
import cocotb_stub_sim
from pyuvm import *
from udc_tests_base import UdcTestsBase
import uvm_dataclasses as udc

class TestEnvSmoke(UdcTestsBase):

    def test_smoke(self):

        @udc.environment
        class my_env(uvm_component):
            my_impl : udc.analysis_imp[object]

            @udc.config
            class config(uvm_object):
                a : int = 0
                b : int = 1
                
                def __post_init__(self):
                    print("my_env.config.post_init")

            def __pre_build_phase__(self):
                print("pre_build_phase")
                
            def __post_build_phase__(self):
                print("post_build_phase: configuration=%s" % str(self.configuration))
                    
            def connect_phase(self):
                self.my_impl.write(None)
                
        @udc.environment
        class my_super_env(uvm_component):
            e1 : my_env
            e2 : my_env
            
            def post_build_phase(self):
                print("my_super_env.post_init e1=%s" % (str(self.e1),))
                self.configuration.d = 10

            @udc.config
            class config(uvm_object):
                c : int = 2
                d : int = 3
                
                def initialize(self):
                    """
                    User hook to propagate configuration down
                    """
                    self.e1_config.a = self.d+1
                    self.e2_config.a = self.d+2
                
        # Total config looks like this:
        #
        # config
        #   c : int = 2
        #   d : int = 3
        #   e1_config : my_env
        #     a : int = 0
        #     b : int = 1
        #   e2_config : my_env
        #     a : int = 0
        #     b : int = 1

        @udc.bench
        class my_test(uvm_test):
            top_env : my_super_env
            
            # TODO: clock/reset information
            # TODO: knob info -- don't initially need direct support
            # TODO: propagate active/passive info
            # TODO: user-specified vlnv (?)
            # TODO: additional user-specified vlnvs (?)

            # - Create configuration
            # - Complete initialization of configuration
            # - Complete build of environment and link configuration            
            #
            #
            # - Bench build_phase creates top-level configuration
            # - Creates top-level environment
            # - Calls 'set_config' on top-level environment
            # - Invokes user hook to perform top-level config propagation (eg knob -> top-env)
            #   - This should happen in post_build_phase
            # - Invokes config.initialize() to push perform config propagation
            # - Bench build_phase complete
            # -> UVM invokes sub-environment builds
            #    - top-env build_phase has its configuration 
            #    - constructs sub-envs
            #    - calls sub-env set_config with appropriate config sub-handle
            #      - in our case, directly set configuration attribute
            # <- UVM completes sub-environment builds
            # 
            
            def connect_phase(self):
                print("connect_phase: %s" % str(self))

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
