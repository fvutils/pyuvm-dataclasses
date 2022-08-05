'''
Created on Jul 4, 2022

@author: mballance
'''
import pyuvm as uvm
import uvm_dataclasses as udc
#import vsc
from unittest.case import TestCase
import cocotb_stub_sim as cocotb

from uvm_dataclasses.types import param_base

class TestAgentSmoke(TestCase):

    def test_component(self):

        @udc.component
        class my_inner_component(uvm.uvm_object):
            pass

        @udc.component
        class my_component(uvm.uvm_component):

            # Components are never passed through the constructor
            # Let's assume default is to create
            c1 : my_inner_component
            c2 : my_inner_component

            pass

    def test_param_agent(self):

        class my_agent_transaction(object):
            pass

        @udc.agent
        class my_agent(param_base[dict(ADDR_WIDTH=10, DATA_WIDTH=20)]):
            analysis_ap1 : udc.analysis_port['transaction']
            analysis_ap2 : udc.analysis_port['transaction']

            # This is needed to drive creation of the .core file
            vlnv = "tblink_bfms::apb::initiator"

            class config_t(udc.agent_config_t):
                pass

            ports = (
                udc.input("clk", is_clock=True),
                udc.input("reset", is_reset=True),
                udc.output("addr", "ADDR_WIDTH"),
                udc.output("data", "DATA_WIDTH"),
                udc.output("valid"),
                udc.input("ready")
            )

            transaction_t = my_agent_transaction
#            class transaction(object):
#                pass

            class config_t(object):
                pass

            # Internal method: called to provide this level
            # of hierarchy with its configuration instance
            def initialize(self, config):
                pass

            # Called to allow this hierarchy level to apply
            # configuration values
            def configure(self):
                pass

            pass

        class my_env(object):
#            a1 : my_agent[20, 30]

            def configure(self):
                pass

            pass

        @udc.bench
        class my_bench(object):
            top_env = my_env
            vlnv = "::my_bench"

            # Need three-part config
            # - Incoming configuration as selected by constraints
            # - Configuration overrides at this level
            # - Configuration overrides from above
            # -> Final configuration

            # Called to propagate configuration data
            # down the tree and configure active/passive
            def configure(self):
                pass


        pass

    def test_ap(self):

        class my_t(uvm.uvm_transaction):
            pass

        @udc.component
        class my_c(uvm.uvm_component):
            ap1 : udc.analysis_port[my_t]
            ap2 : udc.analysis_imp[my_t]
    
    def test_smoke(self):

        @udc.agent
        class my_agent(uvm.uvm_component):
            
            @vsc.randclass
            class config(object):
                a : int = 1
                b : int = 2
                c : vsc.rand_uint8_t

            @vsc.randclass
            class transaction(uvm.uvm_object):
                pass
            pass
        
        @udc.environment
        class my_env(uvm.uvm_component):
            
            @udc.object
            class config(object):
                pass
            
            a1 : my_agent
            a2 : my_agent
            
        @udc.bench
        class my_tb(uvm.uvm_component):
            env : my_env

            @udc.object
            class knobs(object):
                pass
                
            
        