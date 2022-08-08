
- objects -- base decorator. Applies to any pyuvm object-derived class
  - trait (decorator) inheritance from vsc.randclass
  - sub-object construction in __init__/__post_init__

- component -- 
  - trait (decorator) inheritance from vsc.randclass
  - class must implement a three-parameter __init__ in order to be used directly

  - Bulk of the 'action' takes place in build_phase

  - non-component sub-object construction in __init__/__post_init__
  - component sub-object construction in build_phase
    - Insert a layer of inheritance hierarchy to support user-supplied build
      - If existing class defines build_phase, need extra layer
      - If not, then just define a build_phase
    - 

- environment -- frameworks-specific decorator
  - trait (decorator) inheritance from udc.component
  - Specialization of component
  - Assemble configuration type from sub-environment configurations
  - Create 

- agent
  - trait (decorator) inheritance from udc.component
  - trait (decorator) inheritance from tblink.interface
  - Captures signal list
  - Captures HDL parameter set
  - Captures API for interacting with BFM
  - Captures config class
    - Must insert built-in methods
  - Implements placeholder for <driver> <-> <bfm> interaction
    - Must be aware that won't
  - Drives generation of BFM HDL shell(s)

- bench
  - trait (decorator) inheritance from udc.component
  - Need bench class to be the root uvm_test
    - Derivative tests inherit from bench class
    - 
  - Captures accepted command-line knobs
  - Captures top-level environment
    - Maybe decorate a field with a designator? env : top_env[abc]
  - 


