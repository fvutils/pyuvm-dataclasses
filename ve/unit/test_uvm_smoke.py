
import cocotb_stub_sim
from pyuvm import *
from ve.unit.udc_tests_base import UdcTestsBase


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
