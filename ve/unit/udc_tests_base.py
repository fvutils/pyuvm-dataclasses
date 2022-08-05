
from unittest import TestCase
import cocotb_stub_sim as cocotb


class UdcTestsBase(TestCase):

    def tearDown(self) -> None:
        cocotb.tearDown()
        return super().tearDown()



