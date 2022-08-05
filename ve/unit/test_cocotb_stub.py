
from unittest import TestCase

import asyncio
import cocotb_stub_sim as cocotb


class TestCocotbStub(TestCase):

    def tearDown(self) -> None:
        cocotb.tearDown()
        return super().tearDown()

    def test_smoke(self):

        async def entry(dut):
            print("Hello")

            for i in range(10):
                await cocotb.triggers.Timer(10, "ns")
                print("post-wait: %d" % cocotb.utils.get_sim_time())

        cocotb.run(entry)

    def test_smoke_2(self):

        async def entry(dut):
            print("Hello")

            for i in range(10):
                await cocotb.triggers.Timer(10, "ns")
                print("post-wait: %d" % cocotb.utils.get_sim_time())

        cocotb.run(entry)



