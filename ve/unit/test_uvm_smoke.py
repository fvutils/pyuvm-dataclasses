
import cocotb_stub_sim
import uvm_dataclasses as udc
import vsc
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
        
    def test_obj_1(self):
        @udc.object
        class transaction(uvm_transaction):
            a : vsc.rand_int32_t = 0
            b : vsc.rand_int32_t = 0
            
        t = transaction()
        
    def test_comp_1(self):
        
        @udc.object
        class transaction(uvm_transaction):
            a : vsc.rand_int32_t = 0
            b : vsc.rand_int32_t = 0
            
        @udc.component
        class producer(uvm_component):
            ap : udc.analysis_port[transaction]
            
            async def run_phase(self):
                self.raise_objection()
                t = transaction()
                
                for i in range(10):
                    t.randomize()
                    t.a = i
                    self.ap.write(t)
                    await cocotb.triggers.Timer(1, 'ns')
                self.drop_objection()
        
        p = producer("p", None)
        
        
    def test_tlm_1(self): # 36
        
        @udc.object
        class transaction(uvm_transaction):
            a : vsc.rand_int32_t = 0
            b : vsc.rand_int32_t = 0
            
            @vsc.constraint
            def ab_c(self):
                self.b > 0
                self.b <= 16
        
        @udc.component
        class producer_c(uvm_component):
            ap : udc.analysis_port[transaction]
            
            async def run_phase(self):
                self.raise_objection()
                t = transaction()
                
                for i in range(10):
                    t.randomize()
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
                print("Transaction: %d (%d)" % (t.a, t.b))
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

    def test_tlm_1_pre(self): # 46
        
        # 22% reduction in code
        
        class transaction(uvm_transaction):
            
            def __init__(self):
                self.a = 0
                self.b = 0
        
        class producer_c(uvm_component):
            
            def __init__(self, name, parent):
                super().__init__(name, parent)
                
            def build_phase(self):
                self.ap = uvm_analysis_port("ap", self)
            
            async def run_phase(self):
                self.raise_objection()
                t = transaction()
                
                for i in range(10):
                    t.a = i
                    self.ap.write(t)
                    await cocotb.triggers.Timer(1, 'ns')
                self.drop_objection()

        count = 0
        class consumer_c(uvm_subscriber):
            
            def __init__(self, name, parent):
                super().__init__(name, parent)
            
            def write(self, t):
                nonlocal count
                print("Transaction: %d" % t.a)
                count += 1
                
        class test_c(uvm_test):
            
            def __init__(self, name, parent):
                super().__init__(name, parent)
                
            def build_phase(self):
                self.producer = producer_c("producer", self)
                self.consumer = consumer_c("consumer", self)
            
            def connect_phase(self):
                self.producer.ap.connect(self.consumer.analysis_export)
                
        async def entry(dut):
            await uvm_root().run_test("test_c")
        cocotb_stub_sim.run(entry)
        
        self.assertEqual(count, 10)                

                