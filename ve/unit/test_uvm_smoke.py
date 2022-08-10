
import cocotb_stub_sim
import uvm_dataclasses as udc
from pyuvm import *
from udc_tests_base import UdcTestsBase


class TestUvmSmoke(UdcTestsBase):

    def test_smoke(self):

        class my_test(uvm_test):

            def build_phase(self):
                print("my_test(1)::build_phase")
            
            async def run_phase(self):
                self.raise_objection()
                print("my_test(1)::run_phase")
                self.drop_objection()

        async def entry(dut):
            await uvm_root().run_test("my_test")
        cocotb_stub_sim.run(entry)

    def test_smoke_2(self):

        class my_test(uvm_test):

            def build_phase(self):
                print("my_test(2)::build_phase")
            
            async def run_phase(self):
                self.raise_objection()
                print("my_test(2)::run_phase")
                self.drop_objection()

        async def entry(dut):
            await uvm_root().run_test("my_test")
        cocotb_stub_sim.run(entry)
        
    def test_tlm_1(self):
        
        @udc.object
        class transaction(uvm_transaction):
            a : int = 0
            b : int = 0
        
        @udc.component
        class producer_c(uvm_component):
            ap : udc.analysis_port[transaction]
            
            async def run_phase(self):
                self.raise_objection()
                t = transaction()
                
                for i in range(10):
                    t.a = i
                    self.ap.write(t)
                    await cocotb.triggers.Timer(1, 'ns')
                self.drop_objection()

        count = 0
        @udc.component
        class consumer_c(uvm_component):
            impl : udc.analysis_imp[transaction]
            
            def write_impl(self, t):
                nonlocal count
                print("Transaction: %d" % t.a)
                count += 1
                
        @udc.component
        class test_c(uvm_test):
            producer : producer_c
            consumer : consumer_c
            
            def connect_phase(self):
                self.producer.ap.connect(self.consumer.impl)
                
        async def entry(dut):
            await uvm_root().run_test("test_c")
        cocotb_stub_sim.run(entry)
        
        self.assertEqual(count, 10)
                

                