.. PyUVM Dataclasses documentation master file, created by
   sphinx-quickstart on Sun Aug 14 10:40:29 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyUVM Dataclasses's documentation!
=============================================

PyUVM Dataclasses is a Python package that allows you to capture UVM 
testbench structures with the same efficiency that Python's 
`dataclasses` package brings to regular data clases.

.. code:: python3

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


In the example above, note the following:

- PyUVM components and objects are marked with decorators.
- No `build_phase` methods are required in order to construct elements.

- Declaring an analysis_imp automatically calls a local method named `write_<imp>`. 
  If the user doesn't declare this method, a placeholder is created instead


The PyUVM Dataclasses version of this simple producer/consumer example requires
22% less code than the full PyUVM version.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
